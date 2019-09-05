#!/usr/bin/python3
"""
starts a Flask web application /states_list: display a HTML
page: (inside the tag BODY)
"""

from flask import Flask, render_template
import models

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def cityState(id=None):
    """lists all State objects present in DBStorage"""

    states = models.storage.all('State')
    if id:
        id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardb(statesList):
    """ Closes dbstorage"""

    models.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
