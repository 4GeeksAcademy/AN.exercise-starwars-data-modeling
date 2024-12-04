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

# Tabla Planets
class Planets(Base):
    __tablename__= 'planets'

    id = Column(Integer,primary_key=True)
    name = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    terreain = Column(String(50), nullable=False)
    population = Column(String(50), nullable=False)

    #relacion con la tabla characters
    Characters = relationship("characters",backref="planet")

# Tabla Characters
class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    species = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'))

# Tabla Favorite_characters
class Favorite_characters(Base):
    __tablename__ = 'favorite_characters'

    user_id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'), primary_key=True)
    date_added = Column(Date, nullable=False)

# Tabla Favorite_planets
class Favorite_planets(Base):
    __tablename__ = 'favorite_planets'

    user_id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)
    date_added = Column(Date, nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
