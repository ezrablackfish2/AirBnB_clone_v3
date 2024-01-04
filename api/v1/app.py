#!/usr/bin/python3
"""
starts a Flask web application
"""


from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views


app = Flask(__name__)


CORS(app, resurce={r"/api/v1/*": {"origins": "0.0.0.0"}})


app.register_blueprint(app_views)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown_engine(exception):
    """ remove object """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """ hurray"""

    response = {"error": "Not Found"}
    return jsonify(response), 404

if __name__ == '__main__':
        app.run(host='0.0.0.0', port='5000')
