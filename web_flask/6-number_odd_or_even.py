""" start Flask and renders /number routes """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ returns Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """ display “C ” followed by the value of the text variable """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """ display python followed by the value of the text variable """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number', strict_slashes=False)
@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """ display number followed by the value of the n variable """
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template', strict_slashes=False)
@app.route('/number_template/<n>', strict_slashes=False)
def number(n):
    """ display number followed by the value of the n variable """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even', strict_slashes=False)
@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def odd_or_even(n):
    """ display number followed by whether it's even or odd """
    if isinstance(n, int):
        if n % 2 == 0:
            result = 'even'
        else:
            result = 'odd'
        return render_template('5-number.html', n=n, result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
