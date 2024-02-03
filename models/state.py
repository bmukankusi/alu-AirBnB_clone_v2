#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """
    State class representing a state in the system.

    Attributes:
        __tablename__ (str): Represents the table name, 'states'.
        name (str): Represents a column containing a string (128 characters).
                    It can't be null.
        cities (relationship): Represents a relationship with the City class.
                               Linked City objects must be automatically deleted for DBStorage.
    """

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """
        Returns a dictionary representation of the State instance.
        Removes the key '_sa_instance_state' if it exists.

        Returns:
            dict: Dictionary representation of the State instance.
        """
        state_dict = super().to_dict()
        state_dict.pop('_sa_instance_state', None)
        return state_dict

    def delete(self):
        """
        Deletes the current instance from the storage (models.storage).
        Calls the method delete.
        """
        models.storage.delete(self)

