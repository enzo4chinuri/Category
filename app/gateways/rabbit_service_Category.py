#coding=utf_8
import pika
import threading
import traceback
import datetime
import bson
import numbers
import app.utils.configCategory as configCategory
import app.utils.json_serializer as json
import app.utils.schema_validator as validator
import app.utils.security as security
import app.utils.mongoCategory as db


EVENT = {
    "type": {
    "required":True,
    "type": str   
     }, # fin type
     "message":{
         "required": True
     } #fin message 
}# fin EVENT


MSG_DELETE_ARTICLE={
    "articleId":{
        "required":True,
        "type":str
    }
}
MSG_UPDATE_ARTICLE={
    "articleId":{
        "required":True,
        "type":str
    },
    "name": {
        "required":True,
        "type":str
    },
    "image": {
        "required":True,
        "type":str
    }, 
    "price": {
        "required":True,
        "type":numbers.Real
    },
    "stock": {
        "required":True,
        "type":numbers.Integral
    },
    "updated": {
        "required":True
        
    },
    "created":{
        "required":True
    },
    "enabled":{
        "required":True
    }

           
}

def init():
    """
    Inicializa los servicios Rabbit
    """
    initAuth()
    initCatalog()

def initAuth():
    """
    Inicializa RabbitMQ para escuchar eventos logout.
    """
    
    authConsumer = threading.Thread(target = listenAuth)
    authConsumer.setDaemon(True)
    authConsumer.start()
    
def initCatalog():

    """
    Inicializa RabbitMQ para escuchar eventos de catalog específicos.
    """
    catalogConsumer=threading.Thread(target=listenCatalog)
    catalogConsumer.setDaemon(True)
    catalogConsumer.start()
 
def listenAuth():
    """
    Básicamente eventos de logout enviados por auth.

    @api {fanout} auth/logout Logout

    @apiGroup RabbitMQ GET

    @apiDescription Escucha de mensajes logout desde auth. Invalida sesiones en cache.

    @apiExample {json} Mensaje
      {
        "type": "Logout",
        "message" : "tokenId"
      }
    """
    EXCHANGE = "auth"

    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=configCategory.get_rabbit_server_url())
        )
        channel = connection.channel()

        channel.exchange_declare(exchange=EXCHANGE, exchange_type='fanout')

        result = channel.queue_declare('', exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange=EXCHANGE, queue=queue_name)

        def callback(ch, method, properties, body):
            event = json.body_to_dic(body.decode('utf-8'))
            if(len(validator.validateSchema(EVENT, event)) > 0):
                return

            if (event["type"] == "logout"):
                security.invalidateSession(event["message"])

        print("RabbitMQ Auth conectado")

        channel.basic_consume(queue_name, callback, auto_ack=True)

        channel.start_consuming()
    except Exception:
        print("RabbitMQ Auth desconectado, intentando reconectar en 10'")
        threading.Timer(10.0, initAuth).start()

def listenCatalog():
    """
        Básicamente eventos de eliminación de un artículo enviados por catalog.

        @api {direct} catalog/delete-article Article Delete

        @apiGroup RabbitMQ GET

        @apiDescription Escucha de mensajesde eliminación de artículos desde catalog. 

        @apiExample {json} Mensaje
        {
        "type": "Delete_article",
        "message" : "articleId"
        }
    """
    """
        Básicamente eventos de modificacion de un artículo enviados por catalog.

        @api {direct} catalog/update-article Update Article

        @apiGroup RabbitMQ GET

        @apiDescription Escucha de mensajes de modificación de artículos desde catalog. 

        @apiExample {json} Mensaje
        {
            "type": "Update_article",
            "message": {
                "articleId": article["_id"],
                "name": article["name"],
                "description": article["description"],
                "image": article["image"],
                "price": article["price"],
                "stock": article["stock"],
                "updated": article["updated"],
                "created": article["created"],
                "enabled": article["enabled"]
            }
        }
                            
    """
    try:    
        connection = pika.BlockingConnection(
            pika.ConnectionParameters( host=configCategory.get_rabbit_server_url())
        )
        channel =connection.channel()
        channel.exchange_declare(exchange='category', exchange_type='direct')
        channel.queue_declare(queue='category')
        channel.queue_bind(exchange='category', queue='category', routing_key='category')
    
        def callback(ch, method, properties, body):
            event = json.body_to_dic(body.decode('utf-8'))
            if (len(validator.validateSchema(EVENT, event))> 0):
                return 

            if (event["type"]=="Delete_article"):
                message=event["message"]
                if (len(validator.validateSchema(MSG_DELETE_ARTICLE, message))> 0):
                    return
                articleId= message["articleId"]
                
            
                results =  db.category.find({"validation":True})
                for r in results:
                    listArticle= r["articlesCategory"]
                    for element in listArticle:
                        if (element["_id"]==articleId):
                            listArticle.remove(element)
                            r["articlesCategory"]=listArticle
                            r["updated"]=datetime.datetime.utcnow()
                            db.category.replace_one({"_id": bson.ObjectId(r["_id"])}, r)
  

            if (event["type"]=="Updated_article"):
                message=event["message"]
                if (len(validator.validateSchema(MSG_UPDATE_ARTICLE, message))> 0):
                    return
                articleId=message["articleId"]
                new_element={
                    "_id":message["articleId"],
                    "name":message["name"],
                    "description":message["description"],
                    "image":message["image"],
                    "price": message["price"],
                    "stock": message["stock"],
                    "updated":message["updated"],
                    "created":message["created"],
                    "enabled":message["enabled"]              
                }

                results =  db.category.find({"validation":True})
                for r in results:
                    listArticle= r["articlesCategory"]
                    for element in listArticle:
                        if (element["_id"]==articleId):
                            n = listArticle.index(element)
                            listArticle.remove(element)
                            listArticle.insert(n, new_element)
                            r["articlesCategory"]=listArticle
                            r["updated"]=datetime.datetime.utcnow()
                            db.category.replace_one({"_id": bson.ObjectId(r["_id"])}, r)

                           
        print("RabbitMQ Catalog conectado")
        channel.basic_consume(queue='category', on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
        
       
    except Exception:
        traceback.print_exc()
        print("RabbitMQ Catalog desconectado, intentado reconectar en 10 minutos.")    
        threading.Timer(10.0, initCatalog).start()    