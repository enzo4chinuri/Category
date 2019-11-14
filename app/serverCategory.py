from flask import Flask
import os.path
import flask 
from flask_cors import CORS
import app.domain.category.route as categoryRoutes
import app.utils.configCategory as config
import app.gateways.rabbit_service_Category as rabbit_service_Category
class MainApp:

    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app, supports_credentials=True, automatic_options=True)
        self.generate_api_doc()
        self.init_routes()
        self._init_category()
        self._init_rabbit()


    def init_routes(self):
        @self.app.route('/<path:path>')
        def api_index(path):
            return flask.send_from_directory('../public', path)
        @self.app.route('/')
        def index():
            return flask.send_from_directory('../public', "index.html")
    #funcion que genera api doc
    def generate_api_doc(self):
        os.system("apidoc -i ./ -o ./public")
       
    def _init_category(self):
        categoryRoutes.init(self.app)
    
    def _init_rabbit(self):
        rabbit_service_Category.init()

    def get_app(self):
        return self.app


    def start(self):
        self.app.run(debug = True)  

    