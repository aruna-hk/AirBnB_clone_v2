#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from os import getenv

env = getenv("HBNB_TYPE_STORAGE")
if (env == "db"):
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
