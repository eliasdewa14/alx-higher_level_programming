#!/usr/bin/python3
import unittest
import json
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test for instantiation of the square class
    """

    def test_passing_one_arg(self):
        sqr = Square(1)
        self.assertEqual(sqr.width, 1)
        self.assertEqual(sqr.height, 1)
        self.assertEqual(sqr.x, 0)
        self.assertEqual(sqr.y, 0)
        self.assertTrue(sqr.id is not None)

    def test_passing_two_arg(self):
        sqr = Square(1, 2)
        self.assertEqual(sqr.width, 1)
        self.assertEqual(sqr.height, 1)
        self.assertEqual(sqr.x, 2)
        self.assertEqual(sqr.y, 0)
        self.assertTrue(sqr.id is not None)

    def test_passing_three_arg(self):
        sqr = Square(1, 2, 3)
        self.assertEqual(sqr.width, 1)
        self.assertEqual(sqr.height, 1)
        self.assertEqual(sqr.x, 2)
        self.assertEqual(sqr.y, 3)
        self.assertTrue(sqr.id is not None)

    def test_passing_four_arg(self):
        sqr = Square(1, 2, 3, 4)
        self.assertEqual(sqr.width, 1)
        self.assertEqual(sqr.height, 1)
        self.assertEqual(sqr.x, 2)
        self.assertEqual(sqr.y, 3)
        self.assertEqual(sqr.id, 4)

    def test_passing_str_arg(self):
        with self.assertRaises(TypeError):
            Square("1")
            Square(1, "2")
            Square(1, 2, "3")

    def test_passing_negative_arg(self):
        with self.assertRaises(ValueError):
            Square(-1)
            Square(1, -2)
            Square(1, 2, -3)

    def test_passing_zero_arg(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_str_(self):
        s1 = Square(1, 2, 3, 4)
        s1.size = 5
        self.assertEqual(str(s1), '[Square] (4) 2/3 - 5')

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1, 9)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(type(s1_dictionary), dict)

        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s1_dictionary == s2, False)

    def test_update_no_args(self):
        s = Square(5)
        s.update()
        self.assertEqual(str(s), '[Square] (52) 0/0 - 5')

    def test_update_one_integer_args(self):
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(str(s1), '[Square] (10) 0/0 - 5')

    def test_update_two_integers_args(self):
        s1 = Square(5)
        s1.update(1, 2)
        self.assertEqual(str(s1), '[Square] (1) 0/0 - 2')

    def test_update_three_integers_args(self):
        s1 = Square(5)
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), '[Square] (1) 3/0 - 2')

    def test_update_four_integers_args(self):
        s1 = Square(5)
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), '[Square] (1) 3/4 - 2')

    def test_update_kwargs_one(self):
        s1 = Square(5)
        s1.update(**{'id': 89})
        self.assertEqual(str(s1), '[Square] (89) 0/0 - 5')

    def test_update_kwargs_two(self):
        s1 = Square(5)
        s1.update(**{'id': 89, 'size': 1})
        self.assertEqual(str(s1), '[Square] (89) 0/0 - 1')

    def test_update_kwargs_three(self):
        s1 = Square(5)
        s1.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(str(s1), '[Square] (89) 2/0 - 1')

    def test_update_kwargs_four(self):
        s1 = Square(5)
        s1.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s1), '[Square] (89) 2/3 - 1')

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual('[]', f.read())
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual('[]', f.read())

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual('[]', f.read())
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual('[]', f.read())

    def test_save_to_file(self):
        s1 = Square(1)
        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            self.assertEqual(json.dumps([s1.to_dictionary()]), f.read())

    def test_save_to_file2(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as file:
            self.assertEqual(json.dumps(
                [s1.to_dictionary(), s2.to_dictionary()]), file.read())

    def test_create(self):
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(s1 is s2, False)
        self.assertEqual(s1 == s2, False)

    def test_create_kwargs_one(self):
        s1 = Square(3, 5, 1)
        s1.create(**{'id': 89})
        self.assertEqual(str(s1), '[Square] (35) 5/1 - 3')

    def test_create_kwargs_two(self):
        s2 = Square(3, 5, 1)
        s2.create(**{'id': 89, 'size': 1})
        self.assertEqual(str(s2), '[Square] (39) 5/1 - 3')

    def test_create_kwargs_three(self):
        s3 = Square(3, 5, 1)
        s3.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(str(s3), '[Square] (37) 5/1 - 3')

    def test_create_kwargs_four(self):
        s4 = Square(3, 5, 1)
        s4.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s4), '[Square] (33) 5/1 - 3')
