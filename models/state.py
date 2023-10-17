#!/usr/bin/python3
"""
Defines State class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class for representing states or regions.

    Attributes:
        name (str): The name of the state or region.
    """
    name = ""
