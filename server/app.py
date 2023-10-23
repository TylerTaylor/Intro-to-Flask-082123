#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Code here

# run python app.py
if __name__ == '__main__':
    app.run(port=5555, debug=True)