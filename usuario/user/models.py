from usuario.base import models

database = models.db

class User(models.Base):
    __tablename__ = 'USER'
    username = database.Column(database.String(30), unique=True)
    email = database.Column(database.String(60), unique=True)
    password = database.Column(database.String(15), unique=False)

    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.username)