#!/usr/bin/python3
"""
starts a Flask web application /states_list: display a HTML
page: (inside the tag BODY)
"""

from flask import Flask, render_template
from models import *

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def statesList():
    """lists all State objects present in DBStorage"""

    states = models.storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardb(statesList):
    """ Closes dbstorage"""

    models.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
