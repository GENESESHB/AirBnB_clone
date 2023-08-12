#!/usr/bin/python3
"""
defines the unittest for city
"""
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
        cty = City()
        self.assertIsInstance(cty.id, str)

    def test_state_id_is_empty_string(self):
        cty = City()
        self.assertEqual(cty.state_id, "")

    def test_name_is_empty_string(self):
        c = City()
        self.assertEqual(c.name, "")

    def test_str_representation(self):
        b = City()
        b.id = "123"
        b.state_id = "456"
        b.name = "Sample City"
        self.assertIn("[City] (123)", str(b))
        self.assertIn("'state_id': '456'", str(b))
        self.assertIn("'name': 'Sample City'", str(b))

    def test_to_dict(self):
        k = City()
        k.id = "123"
        k.state_id = "456"
        k.name = "Sample City"
        k_dict = k.to_dict()
        self.assertEqual(c_dict['id'], '123')
        self.assertEqual(c_dict['state_id'], '456')
        self.assertEqual(c_dict['name'], 'Sample City')
        self.assertIn('__class__', k_dict)
        self.assertIn('created_at', k_dict)
        self.assertIn('updated_at', k_dict)

    def test_to_dict_datetime_attributes(self):
        m = City()
        m_dict = c.to_dict()
        self.assertIsInstance(m_dict['created_at'], str)
        self.assertIsInstance(m_dict['updated_at'], str)

    def test_to_dict_with_arg(self):
        nw = City()
        with self.assertRaises(TypeError):
            nw.to_dict(None)

    def test_updated_at_after_save(self):
        kl = City()
        initial_updated_at = kl.updated_at
        kl.save()
        self.assertNotEqual(initial_updated_at, kl.updated_at)

    def test_updated_at_type_after_save(self):
        bn = City()
        bn.save()
        self.assertIsInstance(bn.updated_at, datetime)

    def test_reload(self):
        l = City()
        l.save()

        new_storage = FileStorage()
        new_storage.reload()
        loaded_objects = new_storage.all()

        self.assertIn(l.id, loaded_objects)
        loaded_city = loaded_objects[l.id]
        self.assertEqual(loaded_city.id, l.id)
        self.assertEqual(loaded_city.state_id, l.state_id)
        self.assertEqual(loaded_city.name, l.name)

if __name__ == "__main__":
    unittest.main()
