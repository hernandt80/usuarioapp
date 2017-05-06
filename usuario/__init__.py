from flask import Flask, render_template, request
from models import db, User
import forms


#Configuracion aplicacion
app = Flask(__name__, template_folder= 'htmls')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@localhost/postgres'
db.init_app(app)

@app.route('/hello')
def hello_world():
    return 'Hello World!!!!'


@app.route('/params')
def params():
    #http://127.0.0.1:5000/params?params1=Hernan
    #http://127.0.0.1:5000/params?params1=Hernan&params2=Latota
    param_uno = request.args.get('params1', 'Msg default: no se seteo params1')
    param_dos = request.args.get('params2', 'Msg default: no se seteo params2')
    return 'Los parametros son: {} y {}'.format(param_uno, param_dos)


@app.route('/usuarios/')
@app.route('/usuarios/<name>/')
@app.route('/usuarios/<name>/<int:edad>')
def usuarios(name = 'valor default', edad = 0):
    #http://127.0.0.1:5000/usuarios/hernan
    return 'El nombre y la edad son: {} {}'.format(name, edad)


@app.route('/')
def index():
    #return render_template('index.html')
    return render_template('home.html')


@app.route('/user/<name>', methods = ['GET', 'POST'])
def user(name='Hernan'):
    age = 36
    my_list = [1, 2, 3, 4]

    comment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        print comment_form.username.data
        print comment_form.email.data
        print comment_form.comment.data

    return render_template('usuario.html', nombre=name, edad=age,
                           lista=my_list, form = comment_form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    formulario = forms.RegistrationForm(request.form)

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
    formulario = forms.LoginForm(request.form)

    if request.method == 'POST' and formulario.validate():
        usuario = User.query.filter_by(username=formulario.username.data,
                                       password=formulario.password.data).one()

        if usuario is not None:
            return render_template('usuario.html', user=usuario)
        else:
            return render_template('login.html', form=formulario)

    else:
        return render_template('login.html', form=formulario)

if __name__ == '__main__':
    app.run(debug=True)