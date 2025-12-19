from wsgiref.simple_server import make_server
from ejercicio6app import application

server = make_server("localhost", 8000, application)
print("Servidor de suma en http://localhost:8000/suma")
server.serve_forever()
