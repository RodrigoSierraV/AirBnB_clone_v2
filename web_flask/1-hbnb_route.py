#!/usr/bin/python3
"""
script that starts a Flask web application:

application must be listening on 0.0.0.0, port 5000
Routes:
/: Hello HBNB!
/hbnb: display HBNB
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return 'HBNB'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
