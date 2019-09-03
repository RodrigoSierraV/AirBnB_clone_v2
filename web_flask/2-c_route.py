#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def hbnb_text(text):
    if '_' in text:
        return 'C {}'.format(text.replace('_', ' '))
    return 'C {}'.format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
