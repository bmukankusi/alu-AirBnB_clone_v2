#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    """
    City class representing a city in the system.

    Attributes:
        __tablename__ (str): Represents the table name, 'cities'.
        name (str): Represents a column containing a string (128 characters).
                    It can't be null.
        state_id (str): Represents a column containing a string (60 characters).
                        It can't be null and is a foreign key to states.id.
    """

    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
