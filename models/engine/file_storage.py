#!/usr/bin/python3
"""A module for file storage to json"""
import json


class FileStorage:
    """A class defined for the serialization and
    deserialization of  json file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """A module that returns the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        a public instance method for  __objects
        with key in obj class
        """
        if obj:
            FileStorage.__objects[
                "{}.{}".format(obj.__class__.__name__, obj.id)
                ] = obj

    def save(self):
        """
        creating a public instance method that serializes the__objects
        to JSON file
        """
        thenew_dict = {}
        for k, value in FileStorage.__objects.items():
            thenew_dict[k] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as files:
            json.dump(thenew_dict, files)

    def reload(self):
        """
        deserializing the JSON
        file to __objects file
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        try:
            with open(FileStorage.__file_path, mode='r') as files:
                thenew_dict = json.load(files)

            for k, value in thenew_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[k] = obj

        except FileNotFoundError:
            pass
