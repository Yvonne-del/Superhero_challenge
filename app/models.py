from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Hero(db.Model):
    __tablename__= 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name= db.Column(db.String)

    heropowers = db.relationship('HerePower', back_populates='hero')

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description= db.Column(db.String)

    heropowers = db.relationship('HerePower', back_populates='power')


class HeroPower(db.Model):
    __tablename__='heropowers'

    id= db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    hero = db.relationship('Hero', back_populates='heropowers')
    power = db.relationship('Power', back_populates='heropowers')