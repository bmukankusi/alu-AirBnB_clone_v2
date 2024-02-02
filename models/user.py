#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class User(BaseModel, Base):
    """
    User class representing a user in the system.

    Attributes:
        __tablename__ (str): Represents the table name, 'users'.
        email (str): Represents a column containing a string (128 characters).
                     It can't be null.
        password (str): Represents a column containing a string (128 characters).
                        It can't be null.
        first_name (str): Represents a column containing a string (128 characters).
                          It can be null.
        last_name (str): Represents a column containing a string (128 characters).
                         It can be null.
    """

    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
