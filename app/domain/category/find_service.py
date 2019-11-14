#coding=utf_8
import re
import app.utils.errors as error
import app.utils.mongoCategory as db
import bson.objectid as bson
import app.domain.category.cud_service as cud


def newShowCategory(categoryId, nameCategory): 
    return{ "categoryId":categoryId,
            "name_Category":nameCategory
        }

def searchCategory(text):

    """
    Busca category por nombre o descripción.\n
    test string Texto a buscar
    """
    """
    @api {get} /v1/category/search/: Buscar Categoría Por Criterio
    @apiName Buscar Categoría Por Criterio
    @apiGroup Categorias
    @apiDescription Busca categoría por nombre o descripción

    @apiSuccessExample {json} Respuesta
        HTTP/1.1 200 OK
        [
            {
                "_id": "{id de categoría}"
                "nameCategory": "{nombre de la categoría}",
                "categoryParent": "{id de la categoría padre}",
                "isParent": "{indica si la categoria tiene categorías hijas o subcategoría}",
                "articlesCategory": "{lista de los artículos en categoría}",
                "subCategory": "{lista de las subCategorías que tiene la categoría}",
                "updated": "{fecha ultima actualización}",
                "creation": "{fecha creación}",
                "valido": "{activo}"
            },

            ...
        ]

    @apiUse Errors
    """
    try:
        regx = re.compile(text, re.IGNORECASE)
        results = []

        cursor = db.category.find({
            "$and": [{
                "validation": True
            }, {
                "$or": [{
                    "nameCategory": regx
                }, {
                    "categoryParent": regx
                }]
            }]
        })
        for doc in cursor:
            results.append(doc)
        return results
    except Exception:
        raise error.InvalidRequest("Invalid search criterio")

def queryCategory(page_num):
    """
    Consulta todas las categorías existentes y sus subcategorías. 
    """
    """
    @api {get} /v1/category: Consultar Categorías
    @apiName Consultar Categorías
    @apiGroup Categorias
    @apiDescription Busca las categorías vigentes y sus subcategorías

    @apiSuccessExample {json} Respuesta
        HTTP/1.1 200 OK
        [
            {
                "category": {"_id": "{identificador de la categoría}",
                    "nameCategory": "{nombre de la categoría}"
                    }

                ["Categorías Hijas":
                    "subCategory":{"_id":"{identificador de la categoría}",
                    "nameCategory": "{nombre de la categoría}"
                    } 
                ]
            },

            ...
        ]

    @apiUse Errors
    """
    #valores para paginar
    page_size=1
    skips = page_size*(page_num-1)
    resultsCategory = []
    search= db.category.find({"$and":[{"validation": True},{"categoryParent":""}]}).limit(page_size).skip(skips).sort("nameCategory", db.pymongo.ASCENDING)
    for r in search:
        rC={
            "category":newShowCategory(r["_id"],r["nameCategory"])
        }
        
        resultsCategory.append(rC)
        resultsCategory.append(querySubCategory(r))
    return resultsCategory
    


def querySubCategory(category):
    results = ["categorías hijas:"]
    if(category["isParent"]==True):
        for element in category["subCategory"]:
            if (element["validation"]==True):
                el={
                "subCategory": newShowCategory(element["_id"],element["nameCategory"])
                }
                results.append(el)
                querySubCategory(element)
        return results
    else:
        return {"categorías hijas":[]}




def queryArticleCategory(categoryId):
    
    """
    Consulta los artículos de una categoría
    """

    """
    @api {get} /v1/category/:categoryId/articles: Consultar Productos De Categoría
    @apiName Consultar Productos De Categoría 
    @apiGroup Categorias
    @apiDescription Busca los productos vigentes de una categoría  

    @apiSuccessExample {json} Respuesta
        HTTP/1.1 200 OK
        
            {
                "category":{
                    "_id": "{id de la categoría}",
                    "nameCategory": "{nombre de la categoría}"
                    },
                "articles":[{
                    "_id":"{id del artículo}",
                    "name":"{nombre del artículo}"
                    },
                    ...
                ]  
            }
        
        

    @apiUse Errors
    """
    
    category=cud.getCategory(categoryId)
    listArticles =[]
    
    for element in category["articlesCategory"]:
        showArticle={
            "_id":element["_id"],
            "name":element["name"]
        } 
        listArticles.append(showArticle)
    if (category["isParent"]==True):
        for r in category["subCategory"]:
            subCategory=cud.getCategory(r["_id"])
            for el in subCategory["articlesCategory"]:
                showArticleHija={
                    "_id":element["_id"],
                    "name":element["name"]
                } 
                listArticles.append(showArticleHija)
    results={
    "category": newShowCategory(category["_id"], category["nameCategory"]),
    "Articles": listArticles
    }
    return results
