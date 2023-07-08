from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class InputTextForm(FlaskForm):
    text = StringField('Text here', validators=[DataRequired()])

