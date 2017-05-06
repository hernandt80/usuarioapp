from flask_sqlalchemy import SQLAlchemy

#Configuracion base de datos
db = SQLAlchemy()

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