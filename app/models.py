from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Enum

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Hero(db.Model, SerializerMixin):
    __tablename__= 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name= db.Column(db.String)

    heropowers = db.relationship('HerePower', back_populates='hero')

class Power(db.Model,SerializerMixin):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description= db.Column(db.String(20), nullable=False)

    heropowers = db.relationship('HerePower', back_populates='power')


class HeroPower(db.Model, SerializerMixin):
    __tablename__='heropowers'

    id= db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    strength = db.Column(Enum('Strong', 'Weak', 'Average', name='strength_enum'), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    hero = db.relationship('Hero', back_populates='heropowers')
    power = db.relationship('Power', back_populates='heropowers')