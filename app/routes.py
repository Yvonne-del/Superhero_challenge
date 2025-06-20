from flask import Blueprint, jsonify, request
from app.models import db, Hero, Power, HeroPower

main = Blueprint('main', __name__)

# GET /heroes
@main.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict(only=('id', 'name', 'super_name')) for hero in heroes]), 200

# GET /heroes/:id
@main.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(hero.to_dict()), 200

# GET /powers
@main.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200

# GET /powers/:id
@main.route('/powers/<int:id>', methods=['GET'])
def get_power_by_id(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict()), 200

# PATCH /powers/:id
@main.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    description = data.get("description")

    if not description or len(description.strip()) == 0:
        return jsonify({"errors": ["validation errors"]}), 400

    power.description = description
    db.session.commit()
    return jsonify(power.to_dict()), 200

# POST /hero_powers
@main.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    strength = data.get("strength")
    power_id = data.get("power_id")
    hero_id = data.get("hero_id")

    if not strength or not power_id or not hero_id:
        return jsonify({"errors": ["validation errors"]}), 400

    new_hero_power = HeroPower(strength=strength, power_id=power_id, hero_id=hero_id)
    try:
        db.session.add(new_hero_power)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"errors": ["validation errors"]}), 400

    return jsonify(new_hero_power.to_dict()), 201
