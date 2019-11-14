# coding=utf_8
import flask
import app.domain.category.cud_service as cud
import app.domain.category.find_service as find_service
import app.domain.category.rest_validations as restValidator
import app.utils.errors as errors
import app.utils.json_serializer as json
import app.utils.security as security

def init(app):

    """
    Inicializa las rutas para Categorías\n
    app:Flask
    """

    @app.route('/v1/category', methods = ['POST'])
    def addCategory():
        try:
            security.validateAdminRole(flask.request.headers.get("Authorization"))
            params = json.body_to_dic(flask.request.data)
            params = restValidator.validateAddCategoryParams(params)
            result = cud.addCategory(params)
           
            return json.dic_to_json(result)
        except Exception as err:
            return errors.handleError(err)

    @app.route('/v1/category/<categoryId>', methods =['DELETE'])
    def delCategory(categoryId):
        try:
            security.validateAdminRole(flask.request.headers.get("Authorization"))
            return cud.delCategory(categoryId)

        except Exception as err:
            return errors.handleError(err)

    @app.route('/v1/category/<categoryId>', methods =['GET'])
    def getCategory(categoryId):
        try:
            security.validateAdminRole(flask.request.headers.get("Authorization"))
            return json.dic_to_json(cud.getCategory(categoryId))
        except Exception as err:
            return errors.handleError(err)

    @app.route('/v1/category/<categoryId>/add/articles/<articleId>' , methods=['PUT'])
    def add_article_category(categoryId, articleId):
        try:
            security.validateAdminRole(flask.request.headers.get("Authorization"))
            return cud.addArticleCategory(categoryId, articleId)
            
        except Exception as err:
            return errors.handleError(err)

    @app.route('/v1/category/<categoryId>/delete/articles/<articleId>' , methods=['PUT'])
    def del_article_category(categoryId, articleId):
        
        try:
            security.validateAdminRole(flask.request.headers.get("Authorization"))
            return cud.delArticleCategory(categoryId, articleId)
        except Exception as err:
            return errors.handleError(err)
    
    @app.route('/v1/category/<int:page_num>', methods= ['GET'])
    def query_category(page_num):
        try:
            security.validateAdminRole(flask.request.headers.get("Authorization"))
            return json.dic_to_json(find_service.queryCategory(page_num))
        except Exception as err:
            return errors.handleError(err)

    @app.route('/v1/category/<categoryId>/articles', methods= ['GET'])
    def query_articles_category(categoryId):
        try:   
            security.validateAdminRole(flask.request.headers.get("Authorization"))
            return json.dic_to_json(find_service.queryArticleCategory(categoryId))
        except Exception as err:
            return errors.handleError(err)    