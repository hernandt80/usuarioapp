from flask_sqlalchemy import SQLAlchemy

#Configuracion base de datos
db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, default=db.func.now(), onupdate=db.func.now())
