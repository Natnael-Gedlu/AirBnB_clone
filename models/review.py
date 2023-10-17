#!/usr/bin/python3
"""
Defines Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class for representing user reviews of places.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
