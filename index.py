from flask import Flask, jsonify, request, g, request_finished
from flask.signals import signals_available

if not signals_available:
    raise RuntimeError("pip install blinker")

app = Flask(__name__)

@app.before_request
def authenticate():
    if request.authorization:
        g.user = request.authorization["username"]
    else:
        g.user = "Anonymous"

def finished(sender, response, **extra):
    print("About to send a response")
    print(response)

@app.route("/api")
def my_microservice():
    response = jsonify({"Hello": g.user})
    return response

request_finished.connect(finished)


if __name__ == "__main__":
    app.run(host="0.0.0.0")