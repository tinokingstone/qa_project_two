from datetime import datetime
from application import db
from sqlalchemy import MetaData, Column

class rand_obj(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	rand_item = db.Column(db.String(120), unique=False, nullable=False)

	def __repr__(self):
		return f"User('{self.id}', '{self.rand_item}')"
