import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    suscription_date = Column(String(250))
    user_name = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), nullable=False)

class Login(Base):
    __tablename__ = 'login'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    password = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(String(250))
    terrain = Column(String(250))
  
class PlanetasFav(Base):
    __tablename__ = 'planetas favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    PlanetasFav = relationship(Planetas)

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    eye_color = Column(String(250))

class PersonajesFav(Base):
    __tablename__ = 'personajes favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    personaje_id = Column(Integer, ForeignKey('personaje.id'))
    PersonajesFav = relationship(Personajes)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
