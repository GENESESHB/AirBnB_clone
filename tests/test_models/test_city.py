#!/usr/bin/python3

import os
import unittest
from models.city import City
from datetime import datetime

class TestCity(unittest.TestCase):
    def test_attributes_exist(self):
        c = City()
        self.assertTrue(hasattr(c, 'id'))
        self.assertTrue(hasattr(c, 'created_at'))
        self.assertTrue(hasattr(c, 'updated_at'))
        self.assertTrue(hasattr(c, 'state_id'))
        self.assertTrue(hasattr(c, 'name'))

    def test_id_is_string(self):
        c = City()
        self.assertIsInstance(c.id, str)

    def test_state_id_is_empty_string(self):
        c = City()
        self.assertEqual(c.state_id, "")

    def test_name_is_empty_string(self):
        c = City()
        self.assertEqual(c.name, "")

    def test_str_representation(self):
        c = City()
        c.id = "123"
        c.state_id = "456"
        c.name = "Sample City"
        self.assertIn("[City] (123)", str(c))
        self.assertIn("'state_id': '456'", str(c))
        self.assertIn("'name': 'Sample City'", str(c))

    def test_to_dict(self):
        c = City()
        c.id = "123"
        c.state_id = "456"
        c.name = "Sample City"
        c_dict = c.to_dict()
        self.assertEqual(c_dict['id'], '123')
        self.assertEqual(c_dict['state_id'], '456')
        self.assertEqual(c_dict['name'], 'Sample City')
        self.assertIn('__class__', c_dict)
        self.assertIn('created_at', c_dict)
        self.assertIn('updated_at', c_dict)

    def test_to_dict_datetime_attributes(self):
        c = City()
        c_dict = c.to_dict()
        self.assertIsInstance(c_dict['created_at'], str)
        self.assertIsInstance(c_dict['updated_at'], str)

    def test_to_dict_with_arg(self):
        c = City()
        with self.assertRaises(TypeError):
            c.to_dict(None)

    def test_updated_at_after_save(self):
        c = City()
        initial_updated_at = c.updated_at
        c.save()
        self.assertNotEqual(initial_updated_at, c.updated_at)

    def test_updated_at_type_after_save(self):
        c = City()
        c.save()
        self.assertIsInstance(c.updated_at, datetime)

    def test_reload(self):
        c = City()
        c.save()

        new_storage = FileStorage()
        new_storage.reload()
        loaded_objects = new_storage.all()

        self.assertIn(c.id, loaded_objects)
        loaded_city = loaded_objects[c.id]
        self.assertEqual(loaded_city.id, c.id)
        self.assertEqual(loaded_city.state_id, c.state_id)
        self.assertEqual(loaded_city.name, c.name)

if __name__ == "__main__":
    unittest.main()
