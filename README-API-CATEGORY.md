<a name="top"></a>
# Category en Python Service v0.1.0

Microservicio de Category

- [Categorias](#categorias)
	- [Agrega artículo a categoría](#agrega-artículo-a-categoría)
	- [Buscar Categoría Por Criterio](#buscar-categoría-por-criterio)
	- [Buscar Categoría](#buscar-categoría)
	- [Consultar Categorías](#consultar-categorías)
	- [Consultar Productos De Categoría](#consultar-productos-de-categoría)
	- [Crear Categorías](#crear-categorías)
	- [Elimina artículo de la categoría](#elimina-artículo-de-la-categoría)
	- [Eliminar categoría](#eliminar-categoría)
	
- [RabbitMQ_GET](#rabbitmq_get)
	- [Article Delete](#article-delete)
	- [Logout](#logout)
	


# <a name='categorias'></a> Categorias

## <a name='agrega-artículo-a-categoría'></a> Agrega artículo a categoría
[Back to top](#top)



	PUT /v1/category/:categoryId/add/articles/:articleId



### Examples

Header Autorización

```
Authorization=bearer {token}
```


### Success Response

200 Respuesta

```
HTTP/1.1 200 OK
"El artículo articulo_id:{articleId}, name:{name} se agregó a la categoría {nameCategory}"
```


### Error Response

401 Unauthorized

```
HTTP/1.1 401 Unauthorized
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
## <a name='buscar-categoría-por-criterio'></a> Buscar Categoría Por Criterio
[Back to top](#top)

<p>Busca categoría por nombre o descripción</p>

	GET /v1/category/search/:





### Success Response

Respuesta

```
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
```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
## <a name='buscar-categoría'></a> Buscar Categoría
[Back to top](#top)



	GET /v1/category/:categoryId





### Success Response

Respuesta

```
HTTP/1.1 200 OK
{
    "_id": "{id de categoría}"
    "nameCategory": "{nombre de la categoría}",
    "categoryParent": "{id de la categoría padre}",
    "isParent": "{indica si la categoria tiene categorías hijas o subcategoría}",
    "articlesCategory": "{lista de artículos que se asocia a una categoría}",
    "subCategory": "{lista de categorías hijas que tiene la categoría}",
    "updated": "{fecha de ultima actualización}",
    "creation": "{fecha de creación}",
    "validation": "{valor booleano que indica si la categoría está activa}"
}
```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
## <a name='consultar-categorías'></a> Consultar Categorías
[Back to top](#top)

<p>Busca las categorías vigentes y sus subcategorías</p>

	GET /v1/category:





### Success Response

Respuesta

```
HTTP/1.1 200 OK
[
    {
        "category": {"_id": "{identificador de la categoría}",
            "nameCategory": "{nombre de la categoría}"
            }

        "subCategory":[ {"_id":"{identificador de la categoría}",
            "nameCategory": "{nombre de la categoría}"
            } ]
    },

    ...
]
```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
## <a name='consultar-productos-de-categoría'></a> Consultar Productos De Categoría
[Back to top](#top)

<p>Busca los productos vigentes de una categoría</p>

	GET /v1/category/:categoryId/articles:





### Success Response

Respuesta

```
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
```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
## <a name='crear-categorías'></a> Crear Categorías
[Back to top](#top)



	POST /v1/category/



### Examples

Body

```
{
    "nameCategory": "{nombre de la categoría}",
    "categoryParent": "{id de la categoría padre}"
}
```
Header Autorización

```
Authorization=bearer {token}
```


### Success Response

Respuesta

```
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
```


### Error Response

401 Unauthorized

```
HTTP/1.1 401 Unauthorized
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
## <a name='elimina-artículo-de-la-categoría'></a> Elimina artículo de la categoría
[Back to top](#top)



	PUT /v1/category/:categoryId/delete/articles/:articleId



### Examples

Header Autorización

```
Authorization=bearer {token}
```


### Success Response

200 Respuesta

```
HTTP/1.1 200 OK
"El artículo articulo_id: {articleId}, name: {name} se eliminó de la  {nameCategory}"
```


### Error Response

401 Unauthorized

```
HTTP/1.1 401 Unauthorized
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
## <a name='eliminar-categoría'></a> Eliminar categoría
[Back to top](#top)



	DELETE /v1/category/:categoryId



### Examples

Header Autorización

```
Authorization=bearer {token}
```


### Success Response

200 Respuesta

```
HTTP/1.1 200 OK
"La categoria {nameCategory} ha sido eliminada"
```


### Error Response

401 Unauthorized

```
HTTP/1.1 401 Unauthorized
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
# <a name='rabbitmq_get'></a> RabbitMQ_GET

## <a name='article-delete'></a> Article Delete
[Back to top](#top)

<p>Escucha de mensajesde eliminación de artículos desde catalog.</p>

	DIRECT catalog/delete-article



### Examples

Mensaje

```
{
"type": "Delete_article",
"message" : "articleId"
}
```




## <a name='logout'></a> Logout
[Back to top](#top)

<p>Escucha de mensajes logout desde auth. Invalida sesiones en cache.</p>

	FANOUT auth/logout



### Examples

Mensaje

```
{
  "type": "Logout",
  "message" : "tokenId"
}
```




