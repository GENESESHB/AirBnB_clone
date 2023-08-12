#!/usr/bin/python3
import unittest
from models.user import User
from datetime import datetime

class TestUser(unittest.TestCase):
    def test_attributes_exist(self):
        u = User()
        self.assertTrue(hasattr(u, 'id'))
        self.assertTrue(hasattr(u, 'created_at'))
        self.assertTrue(hasattr(u, 'updated_at'))
        self.assertTrue(hasattr(u, 'email'))
        self.assertTrue(hasattr(u, 'password'))
        self.assertTrue(hasattr(u, 'first_name'))
        self.assertTrue(hasattr(u, 'last_name'))

    def test_id_is_string(self):
        u = User()
        self.assertIsInstance(u.id, str)

    def test_email_is_empty_string(self):
        u = User()
        self.assertEqual(u.email, "")

    def test_password_is_empty_string(self):
        u = User()
        self.assertEqual(u.password, "")

    def test_first_name_is_empty_string(self):
        u = User()
        self.assertEqual(u.first_name, "")

    def test_last_name_is_empty_string(self):
        u = User()
        self.assertEqual(u.last_name, "")

    def test_str_representation(self):
        u = User()
        u.id = "123"
        u.email = "test@example.com"
        u.password = "password123"
        u.first_name = "John"
        u.last_name = "Doe"
        self.assertIn("[User] (123)", str(u))
        self.assertIn("'email': 'test@example.com'", str(u))
        self.assertIn("'password': 'password123'", str(u))
        self.assertIn("'first_name': 'John'", str(u))
        self.assertIn("'last_name': 'Doe'", str(u))

    def test_to_dict(self):
        u = User()
        u.id = "123"
        u.email = "test@example.com"
        u.password = "password123"
        u.first_name = "John"
        u.last_name = "Doe"
        u_dict = u.to_dict()
        self.assertEqual(u_dict['id'], '123')
        self.assertEqual(u_dict['email'], 'test@example.com')
        self.assertEqual(u_dict['password'], 'password123')
        self.assertEqual(u_dict['first_name'], 'John')
        self.assertEqual(u_dict['last_name'], 'Doe')
        self.assertIn('__class__', u_dict)
        self.assertIn('created_at', u_dict)
        self.assertIn('updated_at', u_dict)

    def test_to_dict_datetime_attributes(self):
        u = User()
        u_dict = u.to_dict()
        self.assertIsInstance(u_dict['created_at'], str)
        self.assertIsInstance(u_dict['updated_at'], str)

    def test_to_dict_with_arg(self):
        u = User()
        with self.assertRaises(TypeError):
            u.to_dict(None)

    def test_updated_at_after_save(self):
        u = User()
        initial_updated_at = u.updated_at
        u.save()
        self.assertNotEqual(initial_updated_at, u.updated_at)

    def test_updated_at_type_after_save(self):
        u = User()
        u.save()
        self.assertIsInstance(u.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
