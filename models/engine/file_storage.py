#!/usr/bin/python3
"""
Defines FileStorage class.
"""

from models.base_model import BaseModel
import json
from models.place import Place
from models.review import Review
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State


class FileStorage:
    """
    A class for serializing and deserializing JSON objects.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary that stores all objects by ID.
        class_dict (dict): A dictionary mapping class names to classes.
    """

    __file_path = 'airborne.json'
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel, "Amenity": Amenity,
        "City": City, "Review": Review, "User": User,
        "Place": Place, "State": State
    }

    def all(self):
        """
        Returns the dictionary of all objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds an object to the dictionary of objects.

        Args:
            obj: The object to add to the dictionary.
        """
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Serializes the objects and saves them to the JSON file.
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the objects from the JSON file and populates the dictionary.
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
