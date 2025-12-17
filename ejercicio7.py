def application(environ, start_response):
    path = environ.get("PATH_INFO", "/")

    if path == "/":
        status = "200 OK"
        response = b"Inicio"

    elif path == "/saludo":
        status = "200 OK"
        response = b"Hola mundo desde WSGI"

    else:
        status = "404 Not Found"
        response = b"404 - No encontrado"

    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)

    return [response]