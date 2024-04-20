#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from models.user import User
from sqlalchemy import Column, ForeignKey, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
