
import http.client
import socket
import app.utils.configCategory as config
import app.utils.errors as errors
import app.utils.json_serializer as json

def get_article(articleId, authKey):
 
  if (not isinstance(authKey, str) or len(authKey) == 0):
    raise errors.InvalidAuth()

  headers = {"Authorization".encode("utf-8"): authKey.encode("utf-8")}

  conn = http.client.HTTPConnection(
    socket.gethostbyname(config.get_connection_catalog_server_url()),
    config.get_connection_catalog_server_port(),
  )
  
  conn.request('GET',"/v1/articles/" + articleId, {}, headers)
  response = conn.getresponse()

  if (response.status != 200):
    raise errors.InvalidAuth()

  result = json.body_to_dic(response.read().decode('utf-8'))
  if (len(result) == 0):
    raise errors.InvalidAuth()

  return result
