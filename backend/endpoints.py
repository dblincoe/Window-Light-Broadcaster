import json

from flask import Flask, abort, jsonify, request
from flask.logging import create_logger

application = Flask(__name__)
LOG = create_logger(application)


@application.route("/current-string", methods=["GET"])
@application.route("/api/current-string", methods=["GET"])
def get_current_string():
    if request.method == "GET":
        c_string = "This is a testy"

        LOG.info(f"Current String Fetched: {c_string}")

        response = jsonify({"c_string": c_string})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    else:
        LOG.error("This should be a POST request")
