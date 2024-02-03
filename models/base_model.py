#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy import Column, String, DateTime, MetaData, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import models

Base = declarative_base()

class BaseModel:
    """
    BaseModel class representing the base model for other classes.

    Attributes:
        id (str): Represents a unique string column (60 characters) and primary key.
        created_at (datetime): Represents a datetime column with a default value of the current datetime.
        updated_at (datetime): Represents a datetime column with a default value of the current datetime.
    """

    id = Column(String(60), unique=True, primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            **kwargs: Dictionary of key-value pairs to set as instance attributes.
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        """
        Saves the current instance to the storage (models.storage) and updates the updated_at attribute.
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: Dictionary representation of the BaseModel instance.
        """
        dictionary = dict(self.__dict__)
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    def delete(self):
        """
        Deletes the current instance from the storage (models.storage).
        """
        models.storage.delete(self)
