#!/usr/bin/env python3

from flask import Flask, make_response, request
from flask_migrate import Migrate

from flask_restful import Api, Resource

# import db from models
from models import db, Doctor, Patient, Appointment

app = Flask(__name__)

api = Api(app)

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

@app.route('/doctors', methods=['GET', 'POST'])
def doctors():

    if request.method == 'GET':

        doctors = Doctor.query.all()

        response_body = [doctor.to_dict() for doctor in doctors]

        return make_response(response_body, 200)
    
    elif request.method == 'POST':
        form_data = request.get_json()

        new_doctor = Doctor(name = form_data.get('name'))

        db.session.add(new_doctor)
        db.session.commit()

        return make_response(new_doctor.to_dict(), 201)


@app.route('/patients')
def patients():
    patients = Patient.query.all()

    resp = [patient.to_dict() for patient in patients]

    return make_response(resp, 200)

@app.route('/patients/<int:id>')
def patient_by_id(id):
    patient = Patient.query.filter(Patient.id == id).first()

    if patient:
        resp = patient.to_dict()
        status_code = 200
    else:
        resp = {"message": "Patient not found"}
        status_code = 404
    
    return make_response(resp, status_code)

@app.route('/appointments')
def appointments():
    appointments = Appointment.query.all()

    resp = [appointment.to_dict() for appointment in appointments]

    return make_response(resp, 200)

@app.route('/appointments/<int:id>')
def appointment_by_id(id):
    appointment = Appointment.query.filter(Appointment.id == id).first()

    if appointment:
        resp = appointment.to_dict()
        status_code = 200
    else:
        resp = {"message": "Appointment not found"}
        status_code = 404

    return make_response(resp, status_code)


# Using Flask-RESTful api

class Patients(Resource):
    def get(self):
        patients = Patient.query.all()
        resp = [patient.to_dict() for patient in patients]
        return make_response(resp, 200)
    
    def post(self):
        form_data = request.get_json()

        new_patient = Patient(name = form_data.get('name'))

        db.session.add(new_patient)
        db.session.commit()

        return make_response(new_patient.to_dict(), 201)
    
api.add_resource(Patients, '/patients')

class PatientById(Resource):
    def get(self, id):
        patient = Patient.query.filter_by(id = id).first()

        if patient:
            resp = patient.to_dict()
            status_code = 200
        else:
            resp = { "message" : f"Patient {id} not found"}
            status_code = 404

        return make_response(resp, status_code)

api.add_resource(PatientById, '/patients/<int:id>')

class Doctors(Resource):
    def get(self):
        doctors = Doctor.query.all()

        resp = [doctor.to_dict() for doctor in doctors]

        return make_response(resp, 200)
    
api.add_resource(Doctors, '/doctors')

class DoctorById(Resource):
    def get(self, id):
        doctor = Doctor.query.filter(Doctor.id == id).first()

        if doctor:
            resp = doctor.to_dict()
            status_code = 200
        else:
            resp = {"message": f"Doctor {id} not found!"}
            status_code = 404

        return make_response(resp, status_code)

api.add_resource(DoctorById, '/doctors/<int:id>')

# run python app.py
if __name__ == '__main__':
    app.run(port=5555, debug=True)