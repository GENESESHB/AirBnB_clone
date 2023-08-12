#!/usr/bin/python3

"""defines the BaseModel class -parent-classe-"""

import uuid
from datetime import datetime
import models


class BaseModel:
    '''initialization of  the BaseModel -parent-class-'''
    def __init__(self, *args, **kwargs):
        frmdat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, frmdat)
                if key != "__class__":
                    self.__dict__[key] = value
        else:
            models.storage.new(self)
        if not isinstance(self.created_at, datetime):
            self.created_at = datetime.strptime(self.creadted_at, frmdat)

    '''return The string of the BaseModel'''
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    '''save the date of update of the datetime'''
    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    '''
    Return the dictionary of the BaseModel
    send the information copy to json
    '''
    def to_dict(self):
        r_dic = self.__dict__.copy()
        r_dic['__class__'] = self.__class__.__name__
        r_dic['created_at'] = r_dic['created_at'].isoformat()
        r_dic['updated_at'] = r_dic['updated_at'].isoformat()
        return r_dic
