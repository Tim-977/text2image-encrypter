from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class InputTextForm(FlaskForm):
    text = StringField('Put your text here', validators=[DataRequired()])
    submit = SubmitField('Encode')

