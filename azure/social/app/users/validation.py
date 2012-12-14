from wtforms import Form, validators
from wtforms.fields import TextField, PasswordField

class RegisterForm(Form):
    email = TextField('Email', [validators.Length(max=120), validators.Email(), validators.Required()])
    password = PasswordField('Password', [
        validators.Length(min=5, message=u'Password should be more than 5 characters.'),
        validators.Length(max=80, message=u'Password should be less than 80 characters.'),
        validators.Required()
    ])
    name = TextField('Name', [validators.Length(max=50), validators.Required()])