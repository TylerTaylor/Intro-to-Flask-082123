from app import app
from models import db, Doctor, Patient, Appointment
import datetime

with app.app_context():

    print("Deleting existing objects...")

    Doctor.query.delete()
    Patient.query.delete()
    Appointment.query.delete()

    d1 = Doctor(name = "Greg")
    d2 = Doctor(name = "Phil")
    d3 = Doctor(name = "Mantis")
    d4 = Doctor(name = "Who")
    d5 = Doctor(name = "Pepper")
    
    db.session.add_all([d1, d2, d3, d4, d5])
    db.session.commit()

    p1 = Patient(name = "Jess")
    p2 = Patient(name = "John")
    p3 = Patient(name = "Chris")
    p4 = Patient(name = "Nic")
    p5 = Patient(name = "Eleanor")

    db.session.add_all([p1, p2, p3, p4, p5])
    db.session.commit()

    a1 = Appointment(date = datetime.datetime(2024, 1, 5), doctor_id = d1.id, patient_id = p1.id)
    db.session.add(a1)

    db.session.commit()

    print("Everything added!")