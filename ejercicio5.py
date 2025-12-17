from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head><title>Inicio</title></head>
        <body>
            <h1>Servidor Flask</h1>
            <p>HTML estático</p>
        </body>
    </html>
    """

@app.route("/saludo")
def saludo():
    return jsonify({"msg": "Hola"})

if __name__ == "__main__":
    app.run(debug=True)