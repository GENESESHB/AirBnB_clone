#!/usr/bin/python3
"""The BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    '''initialize the BaseModel'''
    def __init__(self, *args, **kwargs):
        formt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, formt)
                if key != "__class__":
                    self.__dict__[key] = value
        else:
            models.storage.new(self)
        if not isinstance(self.created_at, datetime):
            self.created_at = datetime.strptime(self.creadted_at, formt)

    '''The str of the BaseModel'''
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    '''The update of the datetime'''
    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    '''Return the dictionary of the BaseModel'''
    def to_dict(self):
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = dic['created_at'].isoformat()
        dic['updated_at'] = dic['updated_at'].isoformat()
        return dic
