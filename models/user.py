#!/usr/bin/python3
"""
Defines User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class for representing users.

    Attributes:
        email (str): The email address of the user.
        password (str): The password associated with the user.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
