#!/usr/bin/python3
"""
A modukle for creating the User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """attributes involved in the user class"""
    email = ""
    first_name = ""
    password = ""
    last_name = ""
