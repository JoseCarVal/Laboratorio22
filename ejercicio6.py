from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/sumar", methods=["POST"])
def sumar():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")

    resultado = a + b

    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)