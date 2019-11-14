#coding=utf_8
import flask
import datetime
import bson.objectid as bson
import app.domain.category.category_schema as schema
import app.utils.errors as error
import app.utils.mongoCategory as db
import app.utils.connection_catalog as conn


def getCategory (categoryId):
    try:
        result = db.category.find_one({"_id": bson.ObjectId(categoryId)})
        if (not result):
            raise error.InvalidArgument("_id", "Document does not exists")
        return result
    except Exception:
        raise error.InvalidArgument("_id", "Invalid object id")

def addCategory(params):

    """
    Agrega una categoría.\n
    params: dict<propiedad, valor> Categoria\n
    return dict<propiedad, valor> Categoria
    """
    """
    @api {post} /v1/category/ Crear Categorías
    @apiName Crear categorías
    @apiGroup Categorias

    @apiUse AuthHeader

    @apiExample {json} Body
        {
            "nameCategory": "{nombre de la categoría}",
            "categoryParent": "{id de la categoría padre}"
        }

    @apiSuccessExample {json} Respuesta
        HTTP/1.1 200 OK
        {
           "_id": "{id de categoría}",
            "nameCategory": "{nombre de la categoría}",
            "categoryParent": "{id de la categoría padre}",
            "isParent": "{indica si la categoria tiene categorías hijas o subcategoría}",
            "subCategory": "{lista de subcategorías perteneciente a categoría}",
            "articlesCategory": "{lista de artículos pertenecientes a dicha categoría}",
            "updated": "{fecha ultima actualización}",
            "creation": "{fecha creación}",
            "validation": "{activo}"
        }

    @apiUse Errors

    """
  
    category = schema.newCategory()
    # Actualizamos los valores validos a actualizar
    category.update(params)
    category["updated"] = datetime.datetime.utcnow()
    schema.validateSchema(category)
    category["_id"] = db.category.insert_one(category).inserted_id
    
    # Agrega subcategoría en la categoría padre, y actualiza
    if ("categoryParent" in params):
        categoryParent = getCategory(params["categoryParent"])
        categoryParent["isParent"] = True
        listSubcategory=categoryParent["subCategory"]
        listSubcategory.append(category)
        categoryParent["subCategory"]=listSubcategory
        categoryParent["updated"] = datetime.datetime.utcnow()
        db.category.replace_one({"_id":bson.ObjectId(params["categoryParent"])},categoryParent)
    return category
    

def delCategory(categoryId):
    """
    Marca una categoría como invalido\n
    categoryId: string ObjectId
    """
    """
    Elimina una categoría : delcategory(categoryId: string)

    @api {delete} /v1/category/:categoryId Eliminar categoría
    @apiName Eliminar Categoria
    @apiGroup Categorias

    @apiUse AuthHeader
            

    @apiSuccessExample {json} 200 Respuesta
    HTTP/1.1 200 OK
    "La categoria {nameCategory} ha sido eliminada" 

    @apiUse Errors

    """
    category = getCategory(categoryId)
    # eliminamos la categoría de su categoría padre
    if (category["categoryParent"]!=""):

        categoryParent=getCategory(category["categoryParent"])
        listSubcategory=categoryParent["subCategory"]
        listSubcategory.remove(category)
        categoryParent["subCategory"]=listSubcategory
        if (categoryParent["subCategory"]==[]):
            categoryParent["isParent"]=False
        categoryParent["updated"]=datetime.datetime.utcnow()
        db.category.replace_one({"_id":bson.ObjectId(category["categoryParent"])},categoryParent)    
    category["updated"] = datetime.datetime.utcnow()
    category["validation"] = False
    #si la categoría es padre eliminamos las categorías hijas
    if (category["isParent"]==True):
        listSubcategory=category["subCategory"]
        for element in listSubcategory:
            element["validation"]=False
            element["updated"]=datetime.datetime.utcnow()
            db.category.replace_one({"_id":bson.ObjectId(element["_id"])}, element)
           
    db.category.save(category)
    return "La categoría {} ha sido eliminada ".format(category["nameCategory"])
def addArticleCategory(categoryId, articleId):
    """
    Agrega a una categoría un artículo del catalogo.\n
    categoryId: string object\n
    articleId: string object
            
    """
    """
    Agrega artículo a categoría 

    @api {PUT} /v1/category/:categoryId/add/articles/:articleId Agrega artículo a categoría
    @apiName Agregar Artículo a categoría
    @apiGroup Categorias

    @apiUse AuthHeader
            

    @apiSuccessExample {json} 200 Respuesta
    HTTP/1.1 200 OK
    "El artículo articulo_id:{articleId}, name:{name} se agregó a la categoría {nameCategory}"

    @apiUse Errors

    """
    
    category = getCategory(categoryId)
    article = conn.get_article(articleId, flask.request.headers.get("Authorization"))
    category["articlesCategory"].append(article)
    category["updated"]=datetime.datetime.utcnow()
    db.category.replace_one({"_id":bson.ObjectId(categoryId)},category)
    return "El artículo articulo_id: {}, name: {} se agregó a {}.".format(articleId, article["name"], category["nameCategory"])
   

def delArticleCategory(categoryId, articleId):
    """
    Elimina de una categoría un artículo del catalogo.\n
    categoryId: string object\n
    articleId: string object
              
    """
    """
    Elimina un artículo a categoría : delArticleCategory(categoryId: string ,articleId: string)

    @api {PUT} /v1/category/:categoryId/delete/articles/:articleId Elimina artículo de la categoría
    @apiName Elimina Artículo de la categoría
    @apiGroup Categorias

    @apiUse AuthHeader

    @apiSuccessExample {json} 200 Respuesta
    HTTP/1.1 200 OK
    "El artículo articulo_id: {articleId}, name: {name} se eliminó de la  {nameCategory}"

    @apiUse Errors

    """
    category =  getCategory(categoryId)
    article = conn.get_article(articleId, flask.request.headers.get("Authorization"))
    category["articlesCategory"].remove(article)
    category["updated"]=datetime.datetime.utcnow()
    db.category.replace_one({"_id":bson.ObjectId(categoryId)},category)
    return "El artículo articulo_id: {}, name: {} se eliminó a {}".format(articleId, article["name"], category["nameCategory"])