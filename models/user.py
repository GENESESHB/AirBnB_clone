#!/usr/bin/python3

"""
the class for user
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    User class
    & inheritence BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

