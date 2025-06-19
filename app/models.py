from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Enum
from . import db


class Hero(db.Model, SerializerMixin):
    __tablename__= 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name= db.Column(db.String)

    heropowers = db.relationship('HeroPower', back_populates='hero')

    serialize_rules = ('-heropowers.hero',)

class Power(db.Model,SerializerMixin):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description= db.Column(db.String(20), nullable=False)

    heropowers = db.relationship('HeroPower', back_populates='power')

    serialize_rules = ('-heropowers.power',)


class HeroPower(db.Model, SerializerMixin):
    __tablename__='heropowers'

    id= db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    strength = db.Column(Enum('Strong', 'Weak', 'Average', name='strength_enum'), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    hero = db.relationship('Hero', back_populates='heropowers')
    power = db.relationship('Power', back_populates='heropowers')

    serialize_rules = ('-hero.heropowers', '-power.heropowers')