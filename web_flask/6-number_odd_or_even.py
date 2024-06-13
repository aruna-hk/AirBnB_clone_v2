#!/usr/bin/python3

""" flask webapp """

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ root directory serving"""
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ /hbnb directory serving"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ parametized url """
    return "c {}".format(text.replace('_', ' '))


@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """ parametized url """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/int:<n>", strict_slashes=False)
def num(n):
    """ parametized url """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_temp(n):
    """ filling in template"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def evenOrodd(n):
    """ filling in template"""
    pos = "odd"

    if n % 2 == 0:
        pos = "even"
    return render_template("6-number_odd_or_even.html", n=n, pos=pos)


if __name__ == "__main__":
    """ run the app"""

    app.run(host="0.0.0.0", port=5000)
