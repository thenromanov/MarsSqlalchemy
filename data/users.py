import datetime
import sqlalchemy
from sqlalchemy import orm
from .dbSession import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    hashedPassword = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modifiedDate = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.surname = kwargs.get('surname')
        self.name = kwargs.get('name')
        self.age = kwargs.get('age')
        self.position = kwargs.get('position')
        self.speciality = kwargs.get('speciality')
        self.address = kwargs.get('address')
        self.email = kwargs.get('email')
        self.hashedPassword = kwargs.get('hashedPassword')
        self.modifiedDate = kwargs.get('modifiedDate')
