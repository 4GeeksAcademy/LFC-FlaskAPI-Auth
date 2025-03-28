from flask_sqlalchemy import SQLAlchemy
from enum import Enum
from sqlalchemy import ForeignKey
from dataclasses import dataclass
db = SQLAlchemy()

class FavouritesType(str, Enum):
    SPECIES = "SPECIES"
    FILMS = "FILMS"
    PLANETS = "PLANETS"
    PEOPLE = "PEOPLE"
    SPACESHIPS = "SPACESHIPS"
    VEHICLES = "VEHICLES"

@dataclass
class User(db.Model):
    __tablename__="user"
    id:int = db.Column(db.Integer, primary_key=True, nullable=False)
    username:str = db.Column(db.String(50), nullable=False)
    password:str = db.Column(db.VARCHAR(100), nullable=False)
    email:str = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username
        
@dataclass
class Favourites(db.Model):
    __tablename__= "Favourites"
    id:int = db.Column(db.Integer, primary_key=True, unique=True)
    user_id:int = db.Column(db.Integer, ForeignKey('user.id'), index=True, nullable=False)
    name:str = db.Column(db.String(250), nullable=False, unique=True)
    external_id:int = db.Column(db.Integer, nullable=False)
    type:FavouritesType = db.Column(db.Enum(FavouritesType), nullable=False)

@dataclass
class Films(db.Model):
    __tablename__= "Films"
    id:int = db.Column(db.Integer, primary_key=True, unique=True)
    title:str = db.Column(db.String(250), nullable=False, unique=True)
    director:str = db.Column(db.String(250), nullable=False)
    producer:str = db.Column(db.String(250), nullable=False)
    people:str = db.Column(db.String(250), nullable=False)
    planets:str = db.Column(db.String(250), nullable=False)
    species:str = db.Column(db.String(250),  nullable=False)

@dataclass
class Planets(db.Model):
    __tablename__= "Planets"
    id:int = db.Column(db.Integer, primary_key=True, unique=True)
    climate:str = db.Column(db.String(250), nullable=False, unique=True)
    diameter:int = db.Column(db.Integer, nullable=False)
    name:str = db.Column(db.String(250), nullable=False)
    population:int = db.Column(db.Integer, nullable=False)
    residents:str = db.Column(db.String(250), nullable=False)
    terrain:str = db.Column (db.String(250), nullable=False)


@dataclass
class People(db.Model):
    __tablename__= "People"
    id:int = db.Column(db.Integer, primary_key=True, unique=True)
    name:str = db.Column(db.String(250), nullable=False, unique=True)
    species:str = db.Column(db.String(250), nullable=False)
    skin_color:str = db.Column(db.String(250), nullable=False)
    hair_color:str = db.Column(db.String(250), nullable=False)
    height:str = db.Column(db.String(250), nullable=False)
    
@dataclass
class Spaceships(db.Model):
    __tablename__= "Spaceships"
    id:int = db.Column(db.Integer, primary_key=True, unique=True)
    crew:int = db.Column(db.Integer, nullable=False)
    edited:str = db.Column(db.String(250), nullable=False)
    length:int = db.Column(db.Integer, nullable=False)
    manufacturer:str = db.Column(db.String(500), nullable=False)
    model:str = db.Column(db.String(250), nullable=False)
    name:str = db.Column(db.String(250), nullable=False)
    passengers:int = db.Column(db.Integer, nullable=False)
    starship_class:str = db.Column(db.String(250), nullable=False)

@dataclass
class Vehicles(db.Model):
    __tablename__= "Vehicles"
    id:int = db.Column(db.Integer, primary_key=True, unique=True)
    length:int = db.Column(db.Integer, nullable=False)
    manufacturer:str = db.Column(db.String(500), nullable=False)
    model:str = db.Column(db.String(250), nullable=False)
    name:str = db.Column(db.String(250), nullable=False)
    passengers:int = db.Column(db.Integer, nullable=False)
    pilots = db.Column(db.String(250), nullable=True)
    vehicle_class:str = db.Column(db.String(250), nullable=False)

@dataclass
class Species(db.Model):
    __tablename__= "Species"
    id:int = db.Column(db.Integer, primary_key=True, unique=True)
    average_heigth:str = db.Column(db.String(250), nullable=False)
    designation:str = db.Column(db.String(250), nullable=False)
    eye_colors:str = db.Column(db.String(250), nullable=False)
    hair_colors:str = db.Column(db.String(500), nullable=False)
    homeworld:str = db.Column(db.String(250), nullable=False)
    name:str = db.Column(db.String(250), nullable=False)
    skin_color:str = db.Column(db.String(250), nullable=False)
