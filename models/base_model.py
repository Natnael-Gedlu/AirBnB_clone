#!/usr/bin/python3
"""
Defines BaseModel class.
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Base class for all models.
    Attributes:
        id (str): Unique identifier.
        created_at (datetime): Creation timestamp.
        updated_at (datetime): Last update timestamp.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        Args:
            *args: Non-keyword arguments (unused).
            **kwargs: Keyword arguments to initialize the instance.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """
        Updates the updated_at timestamp and saves the instance
        to the storage system.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance to a dictionary representation.
        Returns:
            dict: A dictionary containing the instance attributes.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name()
        return rdict

    def __str__(self):
        """
        Generates a string representation of the instance.
        Returns:
            str: A string representation of the instance.
        """
        clname = self.__class__.__name
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
