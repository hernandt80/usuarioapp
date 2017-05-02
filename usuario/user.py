from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class CommentForm(Form):
    username = StringField('Username',
        [validators.length(min=4, max=25, message='Usuario Invalido!')])
    email = EmailField('Correo electronico',
        [validators.length(min=4, max=25, message='Email Invalido!')])
    comment = TextField('Comentario',
        [validators.length(min=4, max=25, message='Comentario Invalido!')])
