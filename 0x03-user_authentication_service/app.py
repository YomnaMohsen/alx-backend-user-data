#!/usr/bin/env python3
"""main module
"""
from flask import Flask, jsonify, abort, request


app = Flask(__name__)
if __name__ == "__main__":

    app.run(host="0.0.0.0", port="5000")
