#!/usr/bin/python3
"""The base model for the script as a parent class"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """the parent class for all the other sub classes will use"""

    def __init__(self, *args, **kwargs):
        """Instantiation all the  instance attributes"""

        if kwargs is not None and kwargs != {}:
            for k in kwargs:
                if k == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = kwargs[k]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns string representation of the name and id"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """provides an updates to instance attribute"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """this calls and returns dictionary of all keys present in dict"""

        thenew_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        thenew_dict["created_at"] = thenew_dict["created_at"].isoformat()
        thenew_dict["updated_at"] = thenew_dict["updated_at"].isoformat()
        return thenew_dict
