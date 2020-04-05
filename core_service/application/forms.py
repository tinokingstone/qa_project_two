from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Rand_obj_f(FlaskForm):

	submit = SubmitField('Play')
