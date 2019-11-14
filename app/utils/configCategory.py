# coding=utf_8

import configparser

config = configparser.ConfigParser()
config.read("config.ini")

# configuracion puerto del servidor de microservicio category
def get_server_port():
    return int(get_property("ServerPort", 5000))
#configuracion del puerto del servidor de base de datos
def get_database_server_url():
    return get_property("DatabaseServerUrl", "localhost")
def get_database_server_port():
    return int(get_property("DatabaseServerPort", 27017))

def get_security_server_url():
    return get_property("SecurityServerUrl", "localhost")
def get_security_server_port():
    return int(get_property("SecurityServerPort", 3000))

def get_connection_catalog_server_url():
    return get_property("CatalogServerUrl", "localhost")
def get_connection_catalog_server_port():
    return int(get_property("CatalogServerPort", 3002))

#configuracion del puerto del servidor de rabbit
def get_rabbit_server_url():
    return get_property("RabbitServerUrl", "localhost")


def get_property(name, default):
    if ("DEFAULT" in config):
        if (name in config["DEFAULT"]):
            return config["DEFAULT"][name]
    return default