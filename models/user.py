#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.place import Place
from sqlalchemy import String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user",
                          cascade="all, delete-orphan")

    email = ""
    password = ""
    first_name = ""
    last_name = ""
