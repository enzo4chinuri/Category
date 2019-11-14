#coding = utf_8
import datetime
import numbers
import app.utils.errors as errors
import app.utils.schema_validator as validator
# validaciones generales de esquema, se valida
CATEGORY_DB_SCHEMA = {
    "nameCategory":{
        "required": True,
        "type":str,
        "minLen":1,
        "maxLen":60

    },# fin de nameCategory

    "categoryParent":{
        "required": False,
        "type": str,
        "minLen":1,
        "maxLen":60
    },# fin de categoryParent
    
    "isParent":{
        "required":False,
        "type": bool
        
    }, # fin de  isParent

    "articlesCategory":{
        "required":False,
        "type": list

    }, # fin de articlesCategory
    "subCategory":{
        "required":False,
        "type":list
    }
    

}# FIN CATEGORY_DB_SCHEMA

def newCategory():
    """
    Crea una nueva categoría en blanco.\n
    return dict<propiedad, valor> Articulo
    """
    return{
        "nameCategory":"",
        "categoryParent":"",
        "isParent": False,
        "articlesCategory":[],
        "subCategory":[],
        "updated": datetime.datetime.utcnow(),
        "validation":True,
        "creation": datetime.datetime.utcnow()
    }

def validateSchema(document):
    err = validator.validateSchema(CATEGORY_DB_SCHEMA, document)

    if (len(err) > 0):
        raise errors.MultipleArgumentException(err)