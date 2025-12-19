def application(environ, start_response):
    path = environ.get("PATH_INFO", "/")

    if path == "/":
        start_response("200 OK", [("Content-Type", "text/plain")])
        return [b"Inicio"]

    elif path == "/saludo":
        start_response("200 OK", [("Content-Type", "text/plain")])
        return [b"Hola mundo desde WSGI"]

    else:
        start_response("404 Not Found", [("Content-Type", "text/plain")])
        return [b"404 - Recurso no encontrado"]
    