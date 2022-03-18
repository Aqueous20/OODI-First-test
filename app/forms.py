from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms import TextAreaField

class BOOKING(FlaskForm):
    firstname = StringField('firstname',validators = [DataRequired()])
    lastname = StringField('lastname',validators = [DataRequired()])
    address = StringField('address',validators = [DataRequired()])
    email = StringField('email',validators = [DataRequired(),Email()])
    phonenumber = StringField('phonenumber',validators = [DataRequired()])
    Equipment_needed = TextAreaField('Equipment_needed',validators = [DataRequired()])