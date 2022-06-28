"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Personajes, Planets, Vehiculos, Favoritos
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Methods User:

@app.route('/user', methods=['GET'])
def handle_hello():
    users = User.query.all()
    userList = list(map(lambda obj : obj.serialize(),users))

    response_body = {
        "msg": userList
    }

    return jsonify(response_body), 200

@app.route('/user/<int:user_id>', methods=['GET'])
def show_users(user_id):
    userId = User.query.get(user_id)
    print(userId)
    return jsonify(userId.serialize()), 200

@app.route('/user', methods=['POST'])   
def create_new_user():
    body = json.loads(request.data)
    new_user = User(nombre=body["nombre"], email=body["email"],password=body["password"])
    db.session.add(new_user)
    db.session.commit()
    response_body={
        "msg": ("usuario creado", new_user)
    }
    return jsonify(response_body,200)


#Methods Personajes
@app.route('/Personajes', methods=['GET'])
def handle_Person():

    response_body = {
        "msg": "Hello, this is your GET /Personajes response "
    }

    return jsonify(response_body), 200

#Methods Planets

@app.route('/Planets', methods=['GET'])
def handle_Planets():

    response_body = {
        "msg": "Hello, this is your GET /Planets response "
    }

    return jsonify(response_body), 200


#Methods Vehiculos

@app.route('/Vehiculos', methods=['GET'])
def handle_Vehiculos():

    response_body = {
        "msg": "Hello, this is your GET /Vehiculos response "
    }

    return jsonify(response_body), 200


#Methods Favoritos

@app.route('/user/<int:user_id>/favoritos', methods=['GET'])
def handle_favorites(user_id):
    favoritos2 = Favoritos.query.filter_by(user_id = user_id)
    listaFavoritos = list(map(lambda obj : obj.serialize(),favoritos))
    response_body = {
        "msg": ("Esta es la lista de favoritos:", listaFavoritos)
    }
    return jsonify(response_body),200

@app.route('/user/<int:user_id>/favoritos/<int:favoritos_id>', methods=['DELETE'])
def delete_favorites(user_id,favoritos_id):
    favoritos3 = Favoritos.query.filter_by(id = favoritos_id).all()
    print(favoritos3)
    db.session.delete(favoritos3[0])
    db.session.commit()
    response_body = {
        "msg": "Tu favorito ha sido eliminado!"
    }
    return jsonify(response_body),200  

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
