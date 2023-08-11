#!/usr/bin/python3

"""
defines a class Review
and his attributes
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    defines all attributes and inheritance from
    parent class BaseModel
    """
    place_id = ""
    text = ""
    user_id = ""

