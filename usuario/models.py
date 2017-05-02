from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from database import metadata, db_session

class User2(object):
    query = db_session.query_property()

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(30), unique=True),
              Column('email', String(20), unique=True),
              Column('password', String(20), unique=True)
              )

mapper(User2, users)