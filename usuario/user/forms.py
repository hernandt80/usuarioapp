from wtforms import Form, BooleanField, StringField, PasswordField, validators


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