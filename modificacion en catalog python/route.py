# coding=utf_8

import flask

import app.domain.articles.crud_service as crud
import app.domain.articles.find_service as find
import app.domain.articles.rest_validations as restValidator
import app.utils.errors as errors
import app.utils.json_serializer as json
import app.utils.security as security
import app.gateways.rabbit_service as rabbit_service


def init(app):
    """
    Inicializa las rutas para Articulos\n
    app: Flask
    """

    @app.route('/v1/articles', methods=['POST'])
    def addArticle():
        try:
            security.validateAdminRole(flask.request.headers.get("Authorization"))

            params = json.body_to_dic(flask.request.data)

            params = restValidator.validateAddArticleParams(params)

            result = crud.addArticle(params)

            return json.dic_to_json(result)
        except Exception as err:
            return errors.handleError(err)

    @app.route('/v1/articles/<articleId>', methods=['POST'])
    def updateArticle(articleId):
        try:
            security.validateAdminRole(flask.request.headers.get("Authorization"))

            params = json.body_to_dic(flask.request.data)

            params = restValidator.validateEditArticleParams(articleId, params)

            result = crud.updateArticle(articleId, params)

            return json.dic_to_json(result)
        except Exception as err:
            return errors.handleError(err)

    @app.route('/v1/articles/<articleId>', methods=['GET'])
    def getArticle(articleId):
        try:
            return json.dic_to_json(crud.getArticle(articleId))
        except Exception as err:
            return errors.handleError(err)

    @app.route('/v1/articles/<articleId>', methods=['DELETE'])
    def delArticle(articleId):
        try:
            security.validateAdminRole(flask.request.headers.get("Authorization"))
            crud.delArticle(articleId)
            rabbit_service.send_msg_delete_article(articleId)
            return ""
        except Exception as err:
            return errors.handleError(err)

    @app.route('/v1/articles/search/<criteria>', methods=['GET'])
    def searchArticles(criteria):
        try:
            return json.dic_to_json(find.searchArticles(criteria))
        except Exception as err:
            return errors.handleError(err)
