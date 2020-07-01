#!/usr/bin/python3
"""create class Base"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """class Base"""

    def __init__(self, *args, **kwargs):
        """Initializates a new instance of Base
            Args:
                id
                datetime
                updated_at"""
        format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(self.created_at,
                                                    format)
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(self.updated_at,
                                                    format)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Return a string about a BaseModel instance """
        a, b, c = type(self).__name__, self.id, self.__dict__
        return ("[{}] ({}) {}".format(a, b, c))

    def save(self):
        """ Updates the instance attribute
            with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
            of __dict__ of the instance """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = str(type(self).__name__)
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return new_dict
