#!/usr/bin/python3
"""creating the city class module"""

from models.base_model import BaseModel


class City(BaseModel):
    """the city objects module"""
    state_id = ""
    name = ""
