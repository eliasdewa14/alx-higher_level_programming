#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

    def test_id(self):
        """ Test for instantiation of the base class
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)


class TestBase_to_json_string(unittest.TestCase):
    def test_to_json_string(self):

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(
            dictionary, {'x': 2, 'y': 8, 'id': 1,   'height': 7, 'width': 10})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(json_dictionary, str([
            {'x': 2, 'y': 8, 'id': 1, 'width': 10, 'height': 7}]))
        self.assertEqual(type(json_dictionary), str)


class TestBase_save_to_file(unittest.TestCase):
    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), [{"y": 8, "x": 2, "id": 1,
                                            "width": 10, "height": 7},
                                           {"y": 0, "x": 0, "id": 2,
                                            "width": 2, "height": 4}])


class TestBase_from_json_string(unittest.TestCase):
    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual("[{}] {}".format(type(list_input), list_input),
                         [list][{'height': 4, 'width': 10, 'id': 89},
                                {'height': 7, 'width': 1, 'id': 7}])
        self.assertEqual("[{}] {}".format(type(json_list_input),
                                          json_list_input),
                         [str][{"height": 4, "width": 10, "id": 89},
                               {"height": 7, "width": 1, "id": 7}])
        self.assertEqual("[{}] {}".format(type(list_output), list_output),
                         [list][{'height': 4, 'width': 10, 'id': 89},
                                {'height': 7, 'width': 1, 'id': 7}])


class TestBase_create(unittest.TestCase):
    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1, "[Rectangle](1) 1/0 - 3/5")
        self.assertEqual(r2, "[Rectangle](1) 1/0 - 3/5")
        self.assertEqual(r1 is r2, False)
        self.assertEqual(r1 == r2, False)


if __name__ == "__main__":
    unittest.main()
