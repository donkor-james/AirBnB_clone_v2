#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel
from models.review import Review
from models.review import Review
from sqlalchemy import Column, ForeignKey, String, Integer, Float
from sqlalchemy.orm import relationship
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

    if models.storage_t == "db":
        reviews = relationship("Review", backref="user",
                               cascade="all, delete-orphan")

    else:
        @property
        def reviews(self):
            "gettr for list of previews"
            review_list = []
            all_reviews = models.storage.all(Review)
            for review_inst in list(all_reviews.values()):
                if self.id == review_inst["place_id"]:
                    review_list.append(review_inst)
            return review_list

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
