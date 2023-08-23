#!/usr/bin/python3
"""views index for flask api"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def status():
    """gives back status of the server"""
    return jsonify({"status": "OK"})
