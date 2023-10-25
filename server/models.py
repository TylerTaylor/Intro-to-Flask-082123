from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

# metadata = MetaData()
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# Doctor -> has many appointments
# Patient -> has many appointments
# Appointment -> belongs to a doctor, belongs to a patient

# Doctor -< Appointments
# Patient -< Appointments

class Doctor(db.Model, SerializerMixin):
    __tablename__ = 'doctors'

    serialize_rules = ('-appointments.doctor', )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # the relationship method maps our doctor to its related appointments
    appointments = db.relationship('Appointment', back_populates='doctor', cascade='all, delete-orphan')

    # has many patients THROUGH appointments
    patients = association_proxy('appointments', 'patient')

    def __repr__(self):
        return f'<Doctor {self.id}: {self.name}>'
    
class Patient(db.Model, SerializerMixin):
    __tablename__ = 'patients'

    serialize_rules = ('-appointments.patient', )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    appointments = db.relationship('Appointment', back_populates='patient', cascade='all, delete-orphan')

    # has many doctors THROUGH appointments
    doctors = association_proxy('appointments', 'doctor')

    def __repr__(self):
        return f'<Patient {self.id}: {self.name}>'

class Appointment(db.Model, SerializerMixin):
    __tablename__ = 'appointments'

    serialize_rules = ('-doctor.appointments', '-doctor.patients', '-patient.appointments', '-patient.doctors')

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)

    # Foreign key to store the doctor id
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))

    # Foreign key to store the patient id
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))

    # the relationship method maps our appointment to its doctor
    doctor = db.relationship('Doctor', back_populates='appointments')

    # the relationship method maps our appointment to its patient
    patient = db.relationship('Patient', back_populates='appointments')

    def __repr__(self):
        return f'<Appointment {self.id}>'