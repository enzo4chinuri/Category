import numbers
import app.domain.category.cud_service as cud
import app.utils.errors as error
import app.utils.schema_validator as schemaValidator
 # validaciones que se refieren a las propiedades
CATEGORY_UPDATE_SCHEMA = {
    "nameCategory":{
        "type":str,
        "minLen":1,
        "maxLen":60
    }, #fin de nameCateogry 

    "categoryParent":{
        "type":str,
        "minLen":1,
        "maxLen":60
    },# fin categoryParent

    "isParent":{
        "type":bool
    },#fin de isParent

    "articlesCategory":{
        "type":list
     }, #fin de articlesCategory
     "subCategory":{
         type:list
     }#fin de Subcategory

 }# fin de CATEGORY_UPDATE_SCHEMA

def validateAddCategoryParams(params):
    """
    valida los parametros para crear un objeto cateogría.\n
    params:dict<propiedad, valor> Category
    """
    if ("_id" in params):
        raise error.InvalidArgument("_id", "Inválido")

    return schemaValidator.validateAndClean(CATEGORY_UPDATE_SCHEMA, params)

def validateCategoryExist(categoryId):
    category=cud.getCategory(categoryId)
    if("valido" not in category or not category["valido"]):
        raise error.InvalidArgument("id", "Inválido")
def validateEditCategoryParams(categoryId,params):      
    """
    Valida los parametros para actualizar un objeto.\n
    params: dict<propiedad, valor> Article
    """
    if (not categoryId):
        raise error.InvalidArgument("_id", "Inválido")

    return schemaValidator.validateAndClean(CATEGORY_UPDATE_SCHEMA, params)