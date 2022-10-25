#!/usr/bin/python3
"""Define a Student class"""


class Student:
    """Represent a student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization a new student

        Args:
            first _name: first name of the student
            last_name: last name of the student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """a dictionary representation of of the student"""
        return self.__dict__
