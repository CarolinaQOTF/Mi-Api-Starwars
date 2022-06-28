from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Personajes(db.Model):
    __tablename__ = 'Personajes'
    id = db.Column(db.Integer, primary_key=True)
    nombre_personaje = db.Column(db.String(100), unique=True, nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    color_ojos =  db.Column(db.String(50), nullable=False)
    color_cabello = db.Column(db.String(50), nullable=False)
    altura = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Personajes %r>' % self.nombre_personaje

    def serialize(self):
        return {
            "id": self.id,
            "nombre_personaje": self.nombre_personaje,
            "edad": self.edad,
            "genero": self.Genero,
            "color_ojos": self.color_ojos,
            "color_cabello": self.color_cabello,
            "altura": self.altura

        }

    
class Planets (db.Model):
    __tablename__ = 'Planets'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100),nullable=False)
    clima = db.Column(db.String(50),nullable=False)
    terreno= db.Column(db.String(250),nullable=False)
    rotación= db.Column(db.String(250),nullable=False)
    población= db.Column(db.String(250),nullable=False)
    periodo_orbital= db.Column(db.String(250),nullable=False)
    diametro= db.Column(db.String(250),nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "clima": self.climate,
            "terreno": self.terrain,
            "rotación": self.rotation,
            "población": self.population,
            "periodo_orbital": self.orbital_Period,
            "diametro": self.diameter
            # do not serialize the password, its a security breach
        }

class Vehiculos (db.Model):
    __tablename__ = 'Vehiculos'
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    name_Vehicles = db.Column(db.String(50),nullable=False)
    model = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return '<Vehiculos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name_Vehicles": self.name_Vehicles,
            "model": self.model
            # do not serialize the password, its a security breach
        }
class Favoritos (db.Model):
    __tablename__ = 'Favoritos'
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.String(250))
    items = db.Column(db.Integer)

    def __repr__(self):
        return '<Favoritos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "items": self.items
            # do not serialize the password, its a security breach
        }