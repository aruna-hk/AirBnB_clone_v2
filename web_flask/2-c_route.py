#!/usr/bin/python3

""" flask webapp """

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ root directory serving"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ /hbnb directory serving"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ parametized url """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """ parametized url """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    """ run the app"""

    app.run(host="0.0.0.0", port=5000)
