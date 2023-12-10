#!/usr/bin/python3
"""This moduledefines a review class for the place"""

from models.base_model import BaseModel


class Review(BaseModel):
    """reviews made on the place class"""

    place_id = ""
    text = ""
    user_id = ""
