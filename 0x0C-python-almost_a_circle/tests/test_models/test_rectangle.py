#!/usr/bin/python3
import json
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test for id attribute in rectangle class
    """

    def test_passing_two_arg(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertTrue(r.id is not None)

    def test_passing_three_arg(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)
        self.assertTrue(r.id is not None)

    def test_passing_four_arg(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertTrue(r.id is not None)

    def test_passing_five_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_passing_str_arg(self):
        with self.assertRaises(TypeError):
            Rectangle("1")
            Rectangle(1, "2")
            Rectangle(1, 2, "3")
            Rectangle(1, 2, 3, "4")

    def test_passing_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(2)

    def test_passing_negative_arg(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
            Rectangle(1, -2)
            Rectangle(1, 2, -3)
            Rectangle(1, 2, 3, -4)

    def test_passing_zero_arg(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
            Rectangle(1, 0)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_str_(self):
        r1 = Rectangle(4, 6, 2, 1, 12).__str__()
        self.assertEqual(r1, '[Rectangle] (12) 2/1 - 4/6')
        r2 = Rectangle(5, 5, 1).__str__()
        self.assertEqual(str(r2), '[Rectangle] (21) 1/0 - 5/5')

    def test_display(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()
            r1.display()
            r1 = Rectangle(5)
            r1.display()

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(type(r1_dictionary), dict)

        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r1_dictionary == r2, False)

    def test_update_one_integer_args(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(5)
            r1.update(10)

    def test_update_two_integers_args(self):
        r1 = Rectangle(5, 6)
        r1.update(1, 2)
        self.assertEqual(str(r1), '[Rectangle] (1) 0/0 - 2/6')

    def test_update_three_integers_args(self):
        r1 = Rectangle(5, 6)
        r1.update(1, 2, 3)
        self.assertEqual(str(r1), '[Rectangle] (1) 0/0 - 2/3')

    def test_update_four_integers_args(self):
        r1 = Rectangle(5, 6)
        r1.update(1, 2, 3, 4)
        self.assertEqual(str(r1), '[Rectangle] (1) 4/0 - 2/3')

    def test_update_kwargs_one(self):
        r1 = Rectangle(5, 6)
        r1.update(**{'id': 89})
        self.assertEqual(str(r1), '[Rectangle] (89) 0/0 - 5/6')

    def test_update_kwargs_two(self):
        r1 = Rectangle(5, 6)
        r1.update(**{'id': 89, 'size': 1})
        self.assertEqual(str(r1), '[Rectangle] (89) 0/0 - 5/6')

    def test_update_kwargs_three(self):
        r1 = Rectangle(5, 6)
        r1.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(str(r1), '[Rectangle] (89) 2/0 - 5/6')

    def test_update_kwargs_four(self):
        r1 = Rectangle(5, 6)
        r1.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(r1), '[Rectangle] (89) 2/3 - 5/6')

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1 is r2, False)
        self.assertEqual(r1 == r2, False)

    def test_create_kwargs_one(self):
        r1 = Rectangle(3, 5, 1)
        r1.create(**{'id': 89})
        self.assertEqual(str(r1), '[Rectangle] (10) 1/0 - 3/5')

    def test_create_kwargs_two(self):
        r2 = Rectangle(3, 5, 1)
        r2.create(**{'id': 89, 'size': 1})
        self.assertEqual(str(r2), '[Rectangle] (14) 1/0 - 3/5')

    def test_create_kwargs_three(self):
        r3 = Rectangle(3, 5, 1)
        r3.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(str(r3), '[Rectangle] (12) 1/0 - 3/5')

    def test_create_kwargs_four(self):
        r4 = Rectangle(3, 5, 1)
        r4.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(r4), '[Rectangle] (8) 1/0 - 3/5')

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual('[]', f.read())

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual('[]', f.read())

    def test_save_to_file(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)
            Rectangle.save_to_file([r1])
            with open("Rectangle.json", "r") as f:
                self.assertEqual(json.dumps([r1.to_dictionary()]), f.read())

    def test_save_to_file2(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.dumps(
                [r1.to_dictionary(), r2.to_dictionary()]), file.read())
