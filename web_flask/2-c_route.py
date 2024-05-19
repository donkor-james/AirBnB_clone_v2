#!/usr/bin/python3
"""
 starts Flask application and render /c routes
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the text variable"""
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
