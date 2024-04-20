#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.place import Place
from models.user import User
from sqlalchemy import String, ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Review(BaseModel):
    """ Review classto store review information """

    __tablename__ = "reviews"

    text = Column(String(1024), nullable=False)
    place_id = Column(String, ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

    text = ""
    place_id = ""
    user_id = ""
