#!/usr/bin/python3
"""Here I am, documenting a module.
starts a web flask app that listens on 0.0.0.0 port 5000
route /: display "Hello HBNB!" """

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns Hello HBNB!"""
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
