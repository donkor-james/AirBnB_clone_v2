#!/usr/bin/python3
""" holds class State """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

STORAGE_TYPE = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ Representation of state """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    if STORAGE_TYPE != 'db':
        name = ""
        city_list = []

        @property
        def cities(self):
            """ getter for list of city instances related to the state """
            city_list = []
            for city in models.storage.all(City):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
