from flask import Blueprint, request, jsonify
from marvel_inventory.helpers import token_required
from marvel_inventory.models import User, Character, character_schema, characters_schema, db

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return { 'some': 'value'}


# CREATE CHARACTER ENDPOINT
@api.route('/characters', methods = ['POST'])
@token_required
def create_character(current_user_token):
    name = request.json['name']
    description = request.json['description']
    comics_appeared_in = request.json['comics_appeared_in']
    super_power = request.json['super_power']
    user_token = current_user_token.token

    character = Character(name,description,comics_appeared_in,super_power,user_token = user_token)

    db.session.add(character)
    db.session.commit()


    response = character_schema.dump(character)
    return jsonify(response) 


# RETRIEVE ALL CHARACTERS ENDPOINT
@api.route('/characters', methods = ['GET'])
@token_required
def get_characters(current_user_token):
    # set owner equal to 
    owner = current_user_token.token
    # .all to get everthing
    characters = Character.query.filter_by(user_token = owner).all()
    response = characters_schema.dump(characters)
    return jsonify(response)


@api.route('/characters/<id>', methods = ['GET'])
@token_required
def get_character(current_user_token, id):
    character = Character.query.get(id)
    response = character_schema.dump(character)
    return jsonify(response)


# UPDATE CHARACTER ENDPOINT
@api.route('/characters/<id>', methods = ['POST', 'PUT'])
@token_required
def update_character(current_user_token, id):
    # Grabbing the character from the table - instance is denoted by the id
    character = Character.query.get(id)  #Getting a character instance

    # Then grab each individual attribute and update zero or more of the following values
    character.name = request.json['name']
    character.description = request.json['description']
    character.comics_appeared_in = request.json['comics_appeared_in']
    character.super_power = request.json['super_power']
    character.user_token = current_user_token.token

    # Then commit it to the database
    db.session.commit()
    response = character_schema.dump(character)
    return jsonify(response)


# DELETE CHARACTER ENDPOINT
@api.route('/characters/<id>', methods = ['DELETE'])
@token_required
def delete_character(current_user_token, id):
    character = Character.query.get(id)
    db.session.delete(character)
    db.session.commit()
    response = character_schema.dump(character)
    return jsonify(response)


