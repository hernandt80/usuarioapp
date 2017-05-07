# Import flask dependencies
from flask import Blueprint, request, render_template

# Import module forms
from usuario.base.forms import CommentForm

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_base = Blueprint('base', __name__, url_prefix='/base')


@mod_base.route('/hello')
def hello_world():
    return 'Hello World!!!!'


@mod_base.route('/params')
def params():
    #http://127.0.0.1:5000/params?params1=Hernan
    #http://127.0.0.1:5000/params?params1=Hernan&params2=Latota
    param_uno = request.args.get('params1', 'Msg default: no se seteo params1')
    param_dos = request.args.get('params2', 'Msg default: no se seteo params2')
    return 'Los parametros son: {} y {}'.format(param_uno, param_dos)


@mod_base.route('/usuarios/')
@mod_base.route('/usuarios/<name>/')
@mod_base.route('/usuarios/<name>/<int:edad>')
def usuarios(name = 'valor default', edad = 0):
    #http://127.0.0.1:5000/usuarios/hernan
    return 'El nombre y la edad son: {} {}'.format(name, edad)


@mod_base.route('/user/<name>', methods = ['GET', 'POST'])
def user(name='Hernan'):
    age = 36
    my_list = [1, 2, 3, 4]

    comment_form = CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        print comment_form.username.data
        print comment_form.email.data
        print comment_form.comment.data

    return render_template('usuario.html', nombre=name, edad=age, lista=my_list, form = comment_form)
