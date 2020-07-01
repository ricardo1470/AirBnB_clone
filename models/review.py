#!/usr/bin/python3
""" create class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ init class Review """
    place_id = ""
    useer_id = ""
    text = ""
