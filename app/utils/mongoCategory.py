# conding = utf_8
import pymongo
import app.utils.configCategory as configCategory

client=pymongo.MongoClient(configCategory.get_database_server_url(), configCategory.get_database_server_port())

db = client['category']

category = db.category 