#!/usr/bin/python3
"""Here I am, documenting a module.
starts a web flask app that listens on 0.0.0.0 port 5000
route /: display "Hello HBNB!" 
route /hbnb: display "HBNB" """

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
