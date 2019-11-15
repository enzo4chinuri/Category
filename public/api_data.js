define({ "api": [
  {
    "type": "PUT",
    "url": "/v1/category/:categoryId/add/articles/:articleId",
    "title": "Agrega artículo a categoría",
    "name": "Agregar_Art_culo_a_categor_a",
    "group": "Categorias",
    "success": {
      "examples": [
        {
          "title": "200 Respuesta",
          "content": "HTTP/1.1 200 OK\n\"El artículo articulo_id:{articleId}, name:{name} se agregó a la categoría {nameCategory}\"",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/domain/category/cud_service.py",
    "groupTitle": "Categorias",
    "examples": [
      {
        "title": "Header Autorización",
        "content": "Authorization=bearer {token}",
        "type": "String"
      }
    ],
    "error": {
      "examples": [
        {
          "title": "401 Unauthorized",
          "content": "HTTP/1.1 401 Unauthorized",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/v1/category/:page:",
    "title": "Consultar Categorías",
    "name": "Consultar_Categor_as",
    "group": "Categorias",
    "description": "<p>Busca las categorías vigentes y sus subcategorías</p>",
    "success": {
      "examples": [
        {
          "title": "Respuesta",
          "content": "HTTP/1.1 200 OK\n[\n    {\n        \"category\": {\"_id\": \"{identificador de la categoría}\",\n            \"nameCategory\": \"{nombre de la categoría}\"\n            }\n\n        [\"Categorías Hijas\":\n            \"subCategory\":{\"_id\":\"{identificador de la categoría}\",\n            \"nameCategory\": \"{nombre de la categoría}\"\n            } \n        ]\n    },\n\n    ...\n]",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/domain/category/find_service.py",
    "groupTitle": "Categorias",
    "error": {
      "examples": [
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/v1/category/:categoryId/articles:",
    "title": "Consultar Productos De Categoría",
    "name": "Consultar_Productos_De_Categor_a",
    "group": "Categorias",
    "description": "<p>Busca los productos vigentes de una categoría</p>",
    "success": {
      "examples": [
        {
          "title": "Respuesta",
          "content": "HTTP/1.1 200 OK\n\n    {\n        \"category\":{\n            \"_id\": \"{id de la categoría}\",\n            \"nameCategory\": \"{nombre de la categoría}\"\n            },\n        \"articles\":[{\n            \"_id\":\"{id del artículo}\",\n            \"name\":\"{nombre del artículo}\"\n            },\n            ...\n        ]  \n    }",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/domain/category/find_service.py",
    "groupTitle": "Categorias",
    "error": {
      "examples": [
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "post",
    "url": "/v1/category/",
    "title": "Crear Categorías",
    "name": "Crear_categor_as",
    "group": "Categorias",
    "examples": [
      {
        "title": "Body",
        "content": "{\n    \"nameCategory\": \"{nombre de la categoría}\",\n    \"categoryParent\": \"{id de la categoría padre}\"\n}",
        "type": "json"
      },
      {
        "title": "Header Autorización",
        "content": "Authorization=bearer {token}",
        "type": "String"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Respuesta",
          "content": "HTTP/1.1 200 OK\n{\n   \"_id\": \"{id de categoría}\",\n    \"nameCategory\": \"{nombre de la categoría}\",\n    \"categoryParent\": \"{id de la categoría padre}\",\n    \"isParent\": \"{indica si la categoria tiene categorías hijas o subcategoría}\",\n    \"subCategory\": \"{lista de subcategorías perteneciente a categoría}\",\n    \"articlesCategory\": \"{lista de artículos pertenecientes a dicha categoría}\",\n    \"updated\": \"{fecha ultima actualización}\",\n    \"creation\": \"{fecha creación}\",\n    \"validation\": \"{activo}\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/domain/category/cud_service.py",
    "groupTitle": "Categorias",
    "error": {
      "examples": [
        {
          "title": "401 Unauthorized",
          "content": "HTTP/1.1 401 Unauthorized",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "PUT",
    "url": "/v1/category/:categoryId/delete/articles/:articleId",
    "title": "Elimina artículo de la categoría",
    "name": "Elimina_Art_culo_de_la_categor_a",
    "group": "Categorias",
    "success": {
      "examples": [
        {
          "title": "200 Respuesta",
          "content": "HTTP/1.1 200 OK\n\"El artículo articulo_id: {articleId}, name: {name} se eliminó de la  {nameCategory}\"",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/domain/category/cud_service.py",
    "groupTitle": "Categorias",
    "examples": [
      {
        "title": "Header Autorización",
        "content": "Authorization=bearer {token}",
        "type": "String"
      }
    ],
    "error": {
      "examples": [
        {
          "title": "401 Unauthorized",
          "content": "HTTP/1.1 401 Unauthorized",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "delete",
    "url": "/v1/category/:categoryId",
    "title": "Eliminar categoría",
    "name": "Eliminar_Categoria",
    "group": "Categorias",
    "success": {
      "examples": [
        {
          "title": "200 Respuesta",
          "content": "HTTP/1.1 200 OK\n\"La categoria {nameCategory} ha sido eliminada\"",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./app/domain/category/cud_service.py",
    "groupTitle": "Categorias",
    "examples": [
      {
        "title": "Header Autorización",
        "content": "Authorization=bearer {token}",
        "type": "String"
      }
    ],
    "error": {
      "examples": [
        {
          "title": "401 Unauthorized",
          "content": "HTTP/1.1 401 Unauthorized",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "direct",
    "url": "catalog/delete-article",
    "title": "Article Delete",
    "group": "RabbitMQ_GET",
    "description": "<p>Escucha de mensajesde eliminación de artículos desde catalog.</p>",
    "examples": [
      {
        "title": "Mensaje",
        "content": "{\n\"type\": \"Delete_article\",\n\"message\" : \"articleId\"\n}",
        "type": "json"
      }
    ],
    "version": "0.0.0",
    "filename": "./app/gateways/rabbit_service_Category.py",
    "groupTitle": "RabbitMQ_GET",
    "name": "DirectCatalogDeleteArticle"
  },
  {
    "type": "direct",
    "url": "catalog/update-article",
    "title": "Update Article",
    "group": "RabbitMQ_GET",
    "description": "<p>Escucha de mensajes de modificación de artículos desde catalog.</p>",
    "examples": [
      {
        "title": "Mensaje",
        "content": "{\n    \"type\": \"Update_article\",\n    \"message\": {\n        \"articleId\": article[\"_id\"],\n        \"name\": article[\"name\"],\n        \"description\": article[\"description\"],\n        \"image\": article[\"image\"],\n        \"price\": article[\"price\"],\n        \"stock\": article[\"stock\"],\n        \"updated\": article[\"updated\"],\n        \"created\": article[\"created\"],\n        \"enabled\": article[\"enabled\"]\n    }\n}",
        "type": "json"
      }
    ],
    "version": "0.0.0",
    "filename": "./app/gateways/rabbit_service_Category.py",
    "groupTitle": "RabbitMQ_GET",
    "name": "DirectCatalogUpdateArticle"
  },
  {
    "type": "fanout",
    "url": "auth/logout",
    "title": "Logout",
    "group": "RabbitMQ_GET",
    "description": "<p>Escucha de mensajes logout desde auth. Invalida sesiones en cache.</p>",
    "examples": [
      {
        "title": "Mensaje",
        "content": "{\n  \"type\": \"Logout\",\n  \"message\" : \"tokenId\"\n}",
        "type": "json"
      }
    ],
    "version": "0.0.0",
    "filename": "./app/gateways/rabbit_service_Category.py",
    "groupTitle": "RabbitMQ_GET",
    "name": "FanoutAuthLogout"
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./public/main.js",
    "group": "c__Microservicios_ecommerce_category_public_main_js",
    "groupTitle": "c__Microservicios_ecommerce_category_public_main_js",
    "name": ""
  }
] });
