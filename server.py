"""A tornado server to serve ThePetEmporium"""

#Importing tornado to colaborate with flask
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from ThePetEmporium import hello

http_server = HTTPServer(WSGIContainer(hello))
http_server.listen(5000)
IOLoop.instance().start()
