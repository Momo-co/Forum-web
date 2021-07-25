from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class BasicForm(FlaskForm):
    post = StringField('Forum')
    comment = StringField('Comment')
    edit_post = StringField('Edit Post')
    modify_comment = StringField('Edit Comment')
    submit_comment = SubmitField('Enter Comment')
    submit_post = SubmitField('Post')
    change_post = SubmitField('Change Post')
    change_comment = SubmitField('Change Comment')