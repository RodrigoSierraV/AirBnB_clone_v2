#!/usr/bin/python3
"""This is the db storage class for AirBnB"""
import json
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ doc """

    __engine = None
    __session = None
    __classes_av = [User, State, City, Amenity, Place, Review]

    def __init__(self):
        """ doc """
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.\
                                      format(environ['HBNB_MYSQL_USER'],\
                                             environ['HBNB_MYSQL_PWD'],\
                                             environ['HBNB_MYSQL_HOST'],\
                                             environ['HBNB_MYSQL_DB']), pool_pre_ping=True)
        if environ['HBNB_ENV'] == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ doc """

        ret_dic = {}
        if cls is not None:
            response = self.__session.query(eval(cls))
            for obj in response:
                key = ".".join([cls, obj.id])
                ret_dic.update({key: obj})
        else:
            for class_ in self.__classes_av:
                response = self.__session.query(class_)
                for obj in response:
                    key = ".".join([cls, obj.id])
                    ret_dic.update({key: obj})
        return ret_dic


    def new(self, obj):
        """ doc """
        
        self.__session.add(obj)
    
    def save(self):
        """ doc """

        self.__session.commit()

    def delete(self, obj=None):
        """ doc """

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ doc """

        Base.metadata.create_all(self.__engine)
        tmpSession = sessionmaker(bind=engine, expire_on_commit=False)
        self.__session = scoped_session(tmpSession)()
