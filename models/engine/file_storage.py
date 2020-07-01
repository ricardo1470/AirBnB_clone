#!/usr/bin/python3
""" create File_storage class """


import json
from os import path
import models


class FileStorage:
    """ init File_Storage class """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ public instance method that returns the dictionary __objects """

        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """

        key = '{}.{}'.format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        new_dict = {}
        for k, v in self.__objects.items():
            new_dict[k] = v.to_dict()

        dumps = json.dumps(new_dict)
        with open(self.__file_path, 'w') as f:
            f.write(dumps)

    def reload(self):
        """ deserializes the JSON file to __objects """

        if path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as f:
                    self.__objects = json.load(f)
                    for k, v in self.__objects.items():
                        className = v['__class__']
                        className = models.all_classes[className]
                        self.__objects[k] = className(**v)

            except Exception:
                pass
