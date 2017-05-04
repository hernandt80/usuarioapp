from wtforms.fields.html5 import EmailField
from wtforms import Form, BooleanField, StringField, PasswordField, TextField, validators


class CommentForm(Form):
    username = StringField('Username', [validators.length(min=4, max=25, message='Usuario Invalido!')])
    email = EmailField('Correo electronico', [validators.length(min=4, max=25, message='Email Invalido!')])
    comment = TextField('Comentario', [validators.length(min=4, max=25, message='Comentario Invalido!')])


class RegistrationForm(Form):
    username = StringField('', [validators.Length(min=4, max=25, message='El nombre de usuario debe tener entre 4 y 25 caracteres!')])
    email = StringField('', [validators.Length(min=6, max=35, message='El email debe tener entre 6 y 25 caracteres!')])
    password = PasswordField('', [validators.DataRequired(message='Debe ingresar un password!'),
                                  validators.EqualTo('confirm', message='El passwords no es el mismo!')])
    confirm = PasswordField('')
    accept_tos = BooleanField('Acepta las condiciones', [validators.DataRequired(message='Debe aceptar las condiciones!')])


class LoginForm(Form):
    username = StringField('', [validators.Length(min=4, max=25, message='Debe ingresar el nombre de usuario!')])
    password = PasswordField('', [validators.DataRequired(message='Debe ingresar el password!')])