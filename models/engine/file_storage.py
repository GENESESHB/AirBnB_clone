#!/usr/bin/python3

'''define the FileStorage Class
'''

from models.base_model import BaseModel
import json
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "Place": Place,
        "State": State,
        "Review": Review,
        "Amenity": Amenity
        }

    '''
    Define all the dictionary objects
    '''
    def all(self):
        return FileStorage.__objects

    '''
    Define a new key
    '''
    def new(self, objc):
        ky = objc.__class__.__name__ + '.' + objc.id
        FileStorage.__objects[ky] = objc

    '''
    Define the abstracted save engine
    '''
    def save(self):
        my_dictio = {}
        for ky, objc in FileStorage.__objects.items():
            my_dictio[ky] = objc.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(my_dictio, file)

    '''method that deserializes the Json file and restores the objects.'''
    def reload(self):
        if not os.path.isfile(self.__file_path):
            return
        with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
            objc = json.loads(f.read())
            for ky, valu in objc.items():
                class_name, objc_id = ky.split('.')
                if class_name in self.classes:
                    cls_constructor = self.classes[class_name]
                    objc_instance = cls_constructor(**valu)
                    FileStorage.__objects[ky] = objc_instance
