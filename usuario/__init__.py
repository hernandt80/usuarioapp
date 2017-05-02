from flask import Flask, flash, url_for
from flask import render_template
from flask import request, redirect

from flask_sqlalchemy import SQLAlchemy

import form
import registration
import models

app = Flask(__name__, template_folder= 'htmls')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@localhost/postgres'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'USER'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(15), unique=False)

    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.username)


@app.route('/hello')
def hello_world():
    return 'Hello World!!!!'


#http://127.0.0.1:5000/params?params1=Hernan
#http://127.0.0.1:5000/params?params1=Hernan&params2=Latota
@app.route('/params')
def params():
    param_uno = request.args.get('params1', 'Msg default: no se seteo params1')
    param_dos = request.args.get('params2', 'Msg default: no se seteo params2')
    return 'Los parametros son: {} y {}'.format(param_uno, param_dos)


#http://127.0.0.1:5000/usuarios/hernan
@app.route('/usuarios/')
@app.route('/usuarios/<name>/')
@app.route('/usuarios/<name>/<int:edad>')
def usuarios(name = 'valor default', edad = 0):
    return 'El nombre y la edad son: {} {}'.format(name, edad)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/user/<name>', methods = ['GET', 'POST'])
def user(name='Hernan'):
    age = 36
    my_list = [1, 2, 3, 4]

    comment_form = form.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        print comment_form.username.data
        print comment_form.email.data
        print comment_form.comment.data

    return render_template('usuario.html', nombre=name, edad=age,
                           lista=my_list, form = comment_form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    formulario = registration.RegistrationForm(request.form)

    if request.method == 'POST' and formulario.validate():
        usuario = User(formulario.username.data,
                            formulario.email.data,
                            formulario.password.data)

        db.session.add(usuario)
        db.session.commit()

        return render_template('usuario.html', user=usuario)

    return render_template('register.html', form=formulario)


@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    search = request.form.get('nameSearch')

    if request.method == 'POST' and search != '':
        listaUsuarios = User.query.filter_by(username=request.form['nameSearch'])
    else:
        listaUsuarios = User.query.all()

    return render_template('buscar.html', list=listaUsuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():

    formulario = registration.LoginForm(request.form)

    if request.method == 'POST' and formulario.validate():
        usuario = User.query.filter_by(username=formulario.username.data,
                                       password=formulario.password.data)

        if usuario.first() is not None:
            return render_template('usuario.html', user=usuario.first())
        else:
            return render_template('login.html', form=formulario, mensaje='Usuario no encontrado')
    else:
        return render_template('login.html', form=formulario)


if __name__ == '__main__':
    app.run(debug=True)


from database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()