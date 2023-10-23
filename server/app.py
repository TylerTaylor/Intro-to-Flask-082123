#!/usr/bin/env python3

from flask import Flask, make_response #, request
from flask_migrate import Migrate

# import db from models
from models import db

app = Flask(__name__)

# make the connection to the DB through SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create our migration using our db
migrate = Migrate(app, db)

# initialize the flask app
db.init_app(app)

# Code here
@app.route('/')
def index():
    # print("")
    # print("")
    # print(request.headers)
    resp = make_response("<h1>Hello World</h1>", 200)
    print(resp)

    return resp
    # return "<h1>Hello World</h1>"

@app.route('/users/<int:username>')
def user(username):
    print(username)
    return f"<h1>Welcome {username}!</h1>"

# run python app.py
if __name__ == '__main__':
    app.run(port=5555, debug=True)