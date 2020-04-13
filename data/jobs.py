import datetime
import sqlalchemy
from sqlalchemy import orm
from .dbSession import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    teamLeader = sqlalchemy.Column(sqlalchemy.Integer,  sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    workSize = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    startDate = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    endDate = sqlalchemy.Column(sqlalchemy.DateTime, default=None)
    isFinished = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.teamLeader = kwargs.get('teamLeader')
        self.job = kwargs.get('job')
        self.workSize = kwargs.get('workSize')
        self.collaborators = kwargs.get('collaborators')
        self.startDate = kwargs.get('startDate')
        self.endDate = kwargs.get('endDate')
        self.isFinished = kwargs.get('isFinished')
