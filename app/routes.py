# app/routes.py
from flask import Blueprint, jsonify
from .models import Hero

main = Blueprint('main', __name__)

@main.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    result = [hero.to_dict(only=('id', 'name', 'super_name')) for hero in heroes]
    return jsonify(result), 200
