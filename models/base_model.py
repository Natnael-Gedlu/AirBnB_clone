#!/usr/bin/python3
"""
Defines BaseModel class.
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
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
        date = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        date)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        date)
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Generates a string representation of the instance.
        Returns:
            str: A string representation of the instance.
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the updated_at timestamp and saves the instance
        to the storage system.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dictionary of BaseModel with string formats of times
        """
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic

    def __repr__(self):
        """
        returns string repr
        """
        return (self.__str__())
