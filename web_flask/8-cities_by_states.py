#!/usr/bin/python3
""" routes that returns the cities of a state """
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """ teardown method """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """ returns list of cities """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
