#!/usr/bin/python3
"""
Defines Amenity subclass.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class for representing amenities.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
