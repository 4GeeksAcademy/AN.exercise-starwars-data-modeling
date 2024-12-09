import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Date,Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# Tabla usuarios
class Usuario(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    updata_at = Column(Date, nullable=False)
    create_at = Column(Date, nullable=False)
    active = Column(Boolean, nullable=False)

    # # Relacion con los elemos marcados como favoritos
    favorites = relationship("Favorites",backref="user")
    # # Relacion con personajes favoritos
    # Favorite_characters = relationship("Favorite_characters", backref="user")

    # # Relacion con planetas favoritos
    # Favorite_planets = relationship("Favorite_planets", backref="user")

# Tabla Planets
class Planets(Base):
    __tablename__= 'planets'

    id = Column(Integer,primary_key=True)
    name = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    terreain = Column(String(50), nullable=False)
    population = Column(String(50), nullable=False)

    # Relacion con la tabla characters
    Characters = relationship("characters",backref="planet")

    # # Relación con vehículos favoritos
    favorites = relationship("Favorites", backref="planet")

    #  # Relacion con los planetas marcados como favoritos
    # Favorite_planets = relationship("Favorite_planets", backref="planet")
# Tabla Characters
class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    species = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'))

    #   # Relación con vehículos favoritos
    favorites = relationship("Favorites", backref="character")

    # Relacion con los personaes marcados como favoritos
    # Favorite_characters = relationship("Favorite_characters", backref="character")

# Tabla Vehicles
class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    manufacturer = Column(String(50), nullable=False)

    # Relación con la tabla favorites
    favorites = relationship("Favorites", backref="vehicle")

# Tabla Favorites
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=True)
    favorite_type = Column(String(50), nullable=False)  # 'planet', 'character' o 'vehicles' 
    date_added = Column(Date, nullable=False)
# Tabla Favorite_characters
# class Favorite_characters(Base):
#     __tablename__ = 'favorite_characters'

#     user_id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
#     character_id = Column(Integer, ForeignKey('characters.id'), primary_key=True)
#     date_added = Column(Date, nullable=False)

# # Tabla Favorite_planets
# class Favorite_planets(Base):
#     __tablename__ = 'favorite_planets'

#     user_id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
#     planet_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)
#     date_added = Column(Date, nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
