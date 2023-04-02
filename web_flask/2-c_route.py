#!/usr/bin/python3
"""Here I am, documenting a module.
starts a web flask app that listens on 0.0.0.0 port 5000
route /: display "Hello HBNB!" 
route /hbnb: display "HBNB" 
route /c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space)"""

from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
