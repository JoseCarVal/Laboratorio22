import json

libros = []
next_id = 1


def application(environ, start_response):
    global next_id

    method = environ["REQUEST_METHOD"]
    path = environ.get("PATH_INFO", "")

    # GET /libros
    if path == "/libros" and method == "GET":
        start_response("200 OK", [("Content-Type", "application/json")])
        return [json.dumps(libros).encode("utf-8")]

    # POST /libros
    if path == "/libros" and method == "POST":
        try:
            length = int(environ.get("CONTENT_LENGTH", 0))
            body = environ["wsgi.input"].read(length)
            data = json.loads(body)

            libro = {
                "id": next_id,
                "titulo": data["titulo"],
                "autor": data["autor"],
                "anio": data["anio"]
            }

            libros.append(libro)
            next_id += 1

            start_response("201 Created", [("Content-Type", "application/json")])
            return [json.dumps(libro).encode("utf-8")]

        except:
            start_response("400 Bad Request", [("Content-Type", "text/plain")])
            return [b"JSON invalido"]

    # GET /libros/<id>
    if path.startswith("/libros/") and method == "GET":
        try:
            libro_id = int(path.split("/")[-1])

            for libro in libros:
                if libro["id"] == libro_id:
                    start_response("200 OK", [("Content-Type", "application/json")])
                    return [json.dumps(libro).encode("utf-8")]

            start_response("404 Not Found", [("Content-Type", "text/plain")])
            return [b"Libro no encontrado"]

        except:
            start_response("400 Bad Request", [("Content-Type", "text/plain")])
            return [b"ID invalido"]

    # Ruta no encontrada
    start_response("404 Not Found", [("Content-Type", "text/plain")])
    return [b"Ruta no encontrada"]