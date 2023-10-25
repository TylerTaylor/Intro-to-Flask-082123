#!/usr/bin/env python3

from flask import Flask, make_response #, request
from flask_migrate import Migrate

# import db from models
from models import db, Doctor, Patient, Appointment

app = Flask(__name__)

# make the connection to the DB through SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create our migration using our db
migrate = Migrate(app, db)

# initialize the flask app
db.init_app(app)

@app.route('/doctors/<int:id>')
def doctor_by_id(id):
    doctor = Doctor.query.filter_by(id = id).first()

    if doctor:
        response_body = doctor.to_dict()
        status_code = 200
    else:
        response_body = {"message" : f"{doctor.id} not found"}
        status_code = 404
    
    return make_response(response_body, status_code)

@app.route('/doctors')
def doctors():
    doctors = Doctor.query.all()

    response_body = [doctor.to_dict() for doctor in doctors]

    # response_body = '<h2>Look at all these doctors</h2>'

    # for doctor in doctors:
    #     response_body += f'<p>{doctor.name}</p>'

    return make_response(response_body, 200)

# run python app.py
if __name__ == '__main__':
    app.run(port=5555, debug=True)