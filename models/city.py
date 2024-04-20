#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.state import State
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"

    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", String(60), ForeignKey(""))
    places = relationship("place", backref="cities",
                          cascade="all, delete-orphan")

    name = ""
    state_id = ""
