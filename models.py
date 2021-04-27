from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    name = StringField('Какой это город?', validators=[DataRequired()])
    submit = SubmitField('Ответить')
