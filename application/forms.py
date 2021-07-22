from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class BasicForm(FlaskForm):
    post = StringField('Forum')
    submit_post = SubmitField('Post')