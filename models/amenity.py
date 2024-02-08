#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
from models import storage_t
from sqlalchemy import Column, String, Integer


class Amenity(BaseModel, Base):
    """
    doc
    """
    if models.storage_t == 'db':
        __tablename__ =- 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

        def __init__(self, *args, **kwargs):
            """initializes Amenity"""
            super().__init__(*args, **kwargs)
