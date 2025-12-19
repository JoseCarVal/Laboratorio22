import json

def application(environ, start_response):
    if environ["REQUEST_METHOD"] == "POST" and environ["PATH_INFO"] == "/suma":
        try:
            length = int(environ.get("CONTENT_LENGTH", 0))
            body = environ["wsgi.input"].read(length)
            data = json.loads(body)

            a = data["a"]
            b = data["b"]
            resultado = a + b

            response = json.dumps({"resultado": resultado})

            start_response("200 OK", [("Content-Type", "application/json")])
            return [response.encode("utf-8")]

        except:
            start_response("400 Bad Request", [("Content-Type", "text/plain")])
            return [b"JSON invalido"]

    start_response("404 Not Found", [("Content-Type", "text/plain")])
    return [b"Ruta no encontrada"]