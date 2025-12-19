import json
import os
import mimetypes

equipos = []
next_id = 1
BASE_DIR = os.path.dirname(__file__)
STATIC_DIR = os.path.join(BASE_DIR, "static")


def serve_static(path, start_response):
    file_path = os.path.join(STATIC_DIR, path.replace("/static/", ""))

    if not os.path.isfile(file_path):
        start_response("404 Not Found", [("Content-Type", "text/plain")])
        return [b"Archivo no encontrado"]

    mime, _ = mimetypes.guess_type(file_path)
    mime = mime or "application/octet-stream"

    with open(file_path, "rb") as f:
        content = f.read()

    start_response("200 OK", [("Content-Type", mime)])
    return [content]


def application(environ, start_response):
    global next_id

    method = environ["REQUEST_METHOD"]
    path = environ.get("PATH_INFO", "")

    # -------- ARCHIVOS ESTATICOS --------
    if path.startswith("/static/"):
        return serve_static(path, start_response)

    # -------- LISTAR EQUIPOS --------
    if path == "/equipos" and method == "GET":
        start_response("200 OK", [("Content-Type", "application/json")])
        return [json.dumps(equipos).encode("utf-8")]

    # -------- REGISTRAR EQUIPO --------
    if path == "/equipos" and method == "POST":
        try:
            length = int(environ.get("CONTENT_LENGTH", 0))
            body = environ["wsgi.input"].read(length)
            data = json.loads(body)

            equipo = {
                "id": next_id,
                "nombre": data["nombre"],
                "ciudad": data["ciudad"],
                "nivelAtaque": int(data["nivelAtaque"]),
                "nivelDefensa": int(data["nivelDefensa"])
            }

            equipos.append(equipo)
            next_id += 1

            start_response("201 Created", [("Content-Type", "application/json")])
            return [json.dumps(equipo).encode("utf-8")]

        except:
            start_response("400 Bad Request", [("Content-Type", "text/plain")])
            return [b"Datos invalidos"]

    # -------- CONSULTAR POR ID --------
    if path.startswith("/equipos/") and method == "GET":
        try:
            equipo_id = int(path.split("/")[-1])

            for equipo in equipos:
                if equipo["id"] == equipo_id:
                    start_response("200 OK", [("Content-Type", "application/json")])
                    return [json.dumps(equipo).encode("utf-8")]

            start_response("404 Not Found", [("Content-Type", "text/plain")])
            return [b"Equipo no encontrado"]

        except:
            start_response("400 Bad Request", [("Content-Type", "text/plain")])
            return [b"ID invalido"]

    # -------- ERROR 404 --------
    start_response("404 Not Found", [("Content-Type", "text/plain")])
    return [b"Ruta no encontrada"]