from wsgiref.simple_server import make_server
from ejercicio7app import application

server = make_server("localhost", 8000, application)
print("Servidor WSGI corriendo en http://localhost:8000")
server.serve_forever()