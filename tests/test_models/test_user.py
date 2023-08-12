#!/usr/bin/python3
"""
defines unittest for user
"""
import unittest
from models.user import User
from datetime import datetime
import os

class TestUser(unittest.TestCase):
    def test_attributes_exist(self):
        us = User()
        self.assertTrue(hasattr(us, 'id'))
        self.assertTrue(hasattr(us, 'created_at'))
        self.assertTrue(hasattr(us, 'updated_at'))
        self.assertTrue(hasattr(us, 'email'))
        self.assertTrue(hasattr(us, 'password'))
        self.assertTrue(hasattr(us, 'first_name'))
        self.assertTrue(hasattr(us, 'last_name'))

    def test_id_is_string(self):
        me = User()
        self.assertIsInstance(me.id, str)

    def test_email_is_empty_string(self):
        y = User()
        self.assertEqual(y.email, "")

    def test_password_is_empty_string(self):
        she = User()
        self.assertEqual(she.password, "")

    def test_first_name_is_empty_string(self):
        he = User()
        self.assertEqual(he.first_name, "")

    def test_last_name_is_empty_string(self):
        we = User()
        self.assertEqual(we.last_name, "")

    def test_str_representation(self):
        mame = User()
        mame.id = "123"
        mame.email = "test@example.com"
        mame.password = "password123"
        mame.first_name = "John"
        mame.last_name = "Doe"
        self.assertIn("[User] (123)", str(mame))
        self.assertIn("'email': 'test@example.com'", str(mame))
        self.assertIn("'password': 'password123'", str(mame))
        self.assertIn("'first_name': 'John'", str(mame))
        self.assertIn("'last_name': 'Doe'", str(mame))

    def test_to_dict(self):
        uy = User()
        uy.id = "123"
        uy.email = "test@example.com"
        uy.password = "password123"
        uy.first_name = "John"
        uy.last_name = "Doe"
        uy_dict = uy.to_dict()
        self.assertEqual(uy_dict['id'], '123')
        self.assertEqual(uy_dict['email'], 'test@example.com')
        self.assertEqual(uy_dict['password'], 'password123')
        self.assertEqual(uy_dict['first_name'], 'John')
        self.assertEqual(uy_dict['last_name'], 'Doe')
        self.assertIn('__class__', uy_dict)
        self.assertIn('created_at', uy_dict)
        self.assertIn('updated_at', uy_dict)

    def test_to_dict_datetime_attributes(self):
        lv = User()
        lv_dict = lv.to_dict()
        self.assertIsInstance(lv_dict['created_at'], str)
        self.assertIsInstance(lv_dict['updated_at'], str)

    def test_to_dict_with_arg(self):
        lv = User()
        with self.assertRaises(TypeError):
            lv.to_dict(None)

    def test_updated_at_after_save(self):
        ki = User()
        initial_updated_at = ki.updated_at
        ki.save()
        self.assertNotEqual(initial_updated_at, ki.updated_at)

    def test_updated_at_type_after_save(self):
        al = User()
        al.save()
        self.assertIsInstance(al.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
