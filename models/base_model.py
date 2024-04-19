#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from models import storage

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            id = Column("id", String(60), primary_key=True, nullable=False)
            created_at = Column("created_at", DateTime,
                                nullable=False, default=datetime.utcnow())
            updated_at = Column("updated_at", DateTime,
                                nullable=False, default=datetime.utcnow())
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()

        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if dictionary["_sa_instance_state"]:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """deletes the current instance"""
        storage.delete(self)
