from datetime import datetime
from application import db
from sqlalchemy import MetaData, Column

class rand_obj(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        first = db.Column(db.String(120), unique=False, nullable=True)
        last = db.Column(db.String(120), unique=False, nullable=True)
        gender = db.Column(db.String(120), unique=False, nullable=True)
        age = db.Column(db.String(120), unique=False, nullable=True)
        img = db.Column(db.String(120), unique=False, nullable=True)
        agility = db.Column(db.String(120), unique=False, nullable=True)
        endurance = db.Column(db.String(120), unique=False, nullable=True)
        charisma = db.Column(db.String(120), unique=False, nullable=True)
        rand_item = db.Column(db.String(120), unique=False, nullable=True)
        intelligence = db.Column(db.String(120), unique=False, nullable=True)
        strength = db.Column(db.String(120), unique=False, nullable=True)
        weapon = db.Column(db.String(120), unique=False, nullable=True)
        start_point = db.Column(db.String(120), unique=False, nullable=True)
        end_point = db.Column(db.String(120), unique=False, nullable=True)

        def __repr__(self):
                return f"User('{self.id}', '{self.first}', '{self.last}', '{self.gender}', '{self.age}', '{self.rand_obj}', '{self.img}', '{self.agility}', '{self.charisma}', '{self.rand_item}', '{self.intelligence}', '{self.strength}', '{self.weapon}', '{self.start_point}', '{self.end_point}')"
