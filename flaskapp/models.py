
# SQLAchemy was attempted before switching to DynamoDB. DynamoDB is simplier to use

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

db = SQLAlchemy()

class User(db.Model):
    
    __tablename__ = 'User'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable=True)
    email = db.Column(db.Column(db.String(100), unique=True))
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    pass
    