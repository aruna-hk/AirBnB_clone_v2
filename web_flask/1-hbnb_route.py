#!/usr/bin/python3

""" flask webapp """


def hello():
    """ root directory serving"""
    return "Hello HBNB!"


def hbnb():
    """ root directory serving"""
    return "HBNB"


if __name__ == "__main__":
    """ run the app"""

    from flask import Flask
    app = Flask(__name__)
    app.add_url_rule("/", "hello", hello, strict_slashes=False)
    app.add_url_rule("/hbnb", "hbnb", hbnb, strict_slashes=False)
    app.run(host="0.0.0.0", port=5000)
