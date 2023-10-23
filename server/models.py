from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Shoe(db.Model):
    # create the table name
    __tablename__ = 'shoes'

    # create the columns
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    size = db.Column(db.Float)
    name = db.Column(db.String)
    color = db.Column(db.String)
    type = db.Column(db.String)

    def __repr__(self):
        return f"Brand: {self.brand}"

class Tree(db.Model):
    __tablename__ = 'trees'

    id = db.Column(db.Integer, primary_key=True)
    leaves = db.Column(db.Integer)
    evergreen = db.Column(db.Boolean)
    fruit = db.Column(db.Boolean)
    type = db.Column(db.String)



