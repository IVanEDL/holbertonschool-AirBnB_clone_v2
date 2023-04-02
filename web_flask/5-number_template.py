#!/usr/bin/python3
"""Here I am, documenting a module.
starts a web flask app that listens on 0.0.0.0 port 5000
route /: display "Hello HBNB!"
route /hbnb: display "HBNB"
route /c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space)
route /python/<text>: display “Python ”, followed by the value of the text var
(replace underscore _ symbols with a space) (defaults in 'is cool')
route /number/<n>: display “n is a number” only if n is an integer
route /number_template/<n>: display a HTML page only if n is an integer"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """returns c followed by a statement"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """returns Python followed by a statement"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_html(n):
    return render_template('5-number.html', n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
