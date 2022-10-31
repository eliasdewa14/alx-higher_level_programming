#!/usr/bin/python3
""" Define a Base class
"""


import json


class Base:
    """A base class representation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the rectangle class

        Args:
            id (int): id value as argument. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ A static method representation

        Args:
            list_dictionaries (list): a list of dictionaries

        Returns:
            the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ A class method representation

        Args:
            list_objs (list): a list of inherited instances
        """
        file_name = cls.__name__ + ".json"
        list_of_dic = []
        if list_objs is not None:
            for item in list_objs:
                dic = json.loads(cls.to_json_string(item.to_dictionary()))
                list_of_dic.append(dic)
        with open(file_name, 'w') as f:
            json.dump(list_of_dic, f)

    @staticmethod
    def from_json_string(json_string):
        """ A static method representation

        Args:
            json_string (str): a string representing a list of dictionaries

        Returns:
            If json_string is None or empty, return an empty list
            Otherwise, return the list represented by json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ A class method representation

        Args:
            **dictionary (dict): key/value pairs of attribute
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new
