#!/usr/bin/python3
""" create new view for states """

from flask import abort, jsonify, request
from models.state import State
from api.v1.views import app_views
from models import storage

@app_views.route("/states", methods=["GET"], strict_slashes=False)
def get_all_states():
    """ retrieve the list of state objects.
    """

    states = storage.all(State.values()
    state_list = [state.to_dict() for state in states]
    return jsonify(state_list)

@app_views.route("/states/<state_id>",methods=["GET"], strict_slashes=False)
def get_state(state_id):
""" retireve the State """

    state = storage.get(State, state_id)
    if state:
        return jsonify(state.to_dict())
    else:
    abort(404)
