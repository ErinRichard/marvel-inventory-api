from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField

# DataRequired and Email are classes, so we will need to instantiated them
from wtforms.validators import DataRequired, Email

# email, password, submit_button
# Validators is set to a list because we could have more than one
class UserSignupForm(FlaskForm):
    email = StringField('Email:', validators = [DataRequired(), Email()])
    first_name = StringField('First Name:', validators = [DataRequired()])
    last_name = StringField('Last Name:', validators = [DataRequired()])
    password = PasswordField('Password:', validators = [DataRequired()])
    submit_button = SubmitField('Submit')