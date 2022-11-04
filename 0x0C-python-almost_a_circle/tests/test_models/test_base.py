#!/usr/bin/python3
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ Test for instantiation of the base class
    """

    def test_id_auto(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_passing(self):
        b1 = Base(89)

        self.assertEqual(b1.id, 89)

    def test_to_json_string_none(self):
        dic = None
        string = Base.to_json_string(dic)
        self.assertEqual(type(string), str)
        self.assertEqual(string, '[]')

    def test_to_json_string_empty(self):
        dic = {}
        string = Base.to_json_string(dic)
        self.assertEqual(len(dic), 0)
        self.assertEqual(type(string), str)
        self.assertEqual(string, '{}')

    def test_to_json_string(self):
        dic = [{'id': 12, 'width': 10, 'height': 12, 'x': 4, 'y': 6}]
        string = Base.to_json_string(dic)
        self.assertEqual(type(string), str)
        self.assertEqual(
            string, '[{"x": 4, "y": 6, "height": 12, "id": 12, "width": 10}]')

    def test_from_json_string_none(self):
        list1 = None
        json_list1 = Base.from_json_string(list1)
        self.assertEqual(type(json_list1), list)
        self.assertEqual(json_list1, [])


    def test_from_json_string(self):
        list3 = '[{"id": 89, "width": 10, "height": 4, "x": 4, "y": 6}, \
            {"id": 7, "width": 1, "height": 7, "x": 6, "y": 8}]'
        json_list3 = Base.from_json_string(list3)
        self.assertEqual(type(json_list3), list)
        self.assertEqual(json_list3,
                         [{"id": 89, "width": 10, "height": 4, "x": 4, "y": 6},
                          {"id": 7, "width": 1, "height": 7, "x": 6, "y": 8}])
