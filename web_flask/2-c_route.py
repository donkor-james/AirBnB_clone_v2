#!/usr/bin/python3
"""a script starts flask  renders routes from /c urls """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ returns HBNB """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
	""" return c followed by text in the <text> variable """
	if "_" in text:
		text = text.replace("_", " ")
	return "C {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
