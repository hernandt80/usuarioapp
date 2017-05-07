from flask import Blueprint, request, render_template

from usuario.user.forms import LoginForm, RegistrationForm
from usuario.user.models import User, database

mod_user = Blueprint('user', __name__, url_prefix='/user')


@mod_user.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')


@mod_user.route('/register', methods=['GET', 'POST'])
def register():
    formulario = RegistrationForm(request.form)

    if request.method == 'POST' and formulario.validate():
        usuario = User(formulario.username.data,
                            formulario.email.data,
                            formulario.password.data)

        database.session.add(usuario)
        database.session.commit()

        return render_template('usuario.html', user=usuario)

    return render_template('register.html', form=formulario)


@mod_user.route('/buscar', methods=['GET', 'POST'])
def buscar():
    search = request.form.get('nameSearch')

    if request.method == 'POST' and search != '':
        listaUsuarios = User.query.filter_by(username=request.form['nameSearch'])
    else:
        listaUsuarios = User.query.all()

    return render_template('buscar.html', list=listaUsuarios)


@mod_user.route('/login', methods=['GET', 'POST'])
def login():
    formulario = LoginForm(request.form)

    if request.method == 'POST' and formulario.validate():
        usuario = User.query.filter_by(username=formulario.username.data,
                                       password=formulario.password.data).one()

        if usuario is not None:
            return render_template('usuario.html', user=usuario)
        else:
            return render_template('login.html', form=formulario)

    else:
        return render_template('login.html', form=formulario)
