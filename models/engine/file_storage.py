#!/usr/bin/python3
'''The FileStorage Class'''
from models.base_model import BaseModel
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    classes = {"BaseModel": BaseModel}

    '''Define all the dictionary objects'''
    def all(self):
        return FileStorage.__objects

    '''Define a new key'''
    def new(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    '''Define the abstracted save engine'''
    def save(self):
        my_dict = {}
        for key, obj in FileStorage.__objects.items():
            my_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(my_dict, file)

    '''method that deserializes the Json file and restores the objects.'''
    def reload(self):
        if not os.path.isfile(self.__file_path):
            return
        with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
            obj = json.loads(f.read())
            for key, value in obj.items():
                class_name, obj_id = key.split('.')
                if class_name in self.classes:
                    cls_constructor = self.classes[class_name]
                    obj_instance = cls_constructor(**value)
                    FileStorage.__objects[key] = obj_instance
