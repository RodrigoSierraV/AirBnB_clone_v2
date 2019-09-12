#!/usr/bin/python3
"""
starts a Flask web application /states_list: display a HTML
page: (inside the tag BODY)
"""

from flask import Flask, render_template
import models

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """lists all State objects present in DBStorage"""

    states = models.storage.all('State')
    amenities = models.storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardb(statesList):
    """ Closes dbstorage"""

    models.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
