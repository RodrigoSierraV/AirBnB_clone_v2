#!/usr/bin/python3
"""This is the state class"""
from os import environ
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if 'HBNB_TYPE_STORAGE' in environ and environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship('City', backref="state")
    else:
        @property
        def cities(self):
            """ getter for cities """

            tmp_list = []
            for key, obj in models.storage.all().items():
                if "City" in key and obj.state_id == self.id:
                    tmp_list.append(obj)
            return tmp_list
