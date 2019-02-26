from flask import Flask, jsonify, request, g

app = Flask(__name__)

@app.before_request
def authenticate():
    if request.authorization:
        g.user = request.authorization["username"]
    else:
        g.user = "Anonymous"

@app.route("/api")
def my_microservice():
    response = jsonify({"Hello": g.user})
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0")