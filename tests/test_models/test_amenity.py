#!/usr/bin/python3
"""
defines the unittest for amenity
"""
import unittest
from models.amenity import Amenity
from datetime import datetime
from models.engine.file_storage import FileStorage
import os

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.amenity = Amenity()
        self.amenity.name = "Swimming Pool"

    def tearDown(self):
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_create_amenity(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertEqual(self.amenity.name, "Swimming Pool")

    def test_amenity_id(self):
        self.assertIsInstance(self.amenity.id, str)

    def test_amenity_created_at(self):
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_amenity_updated_at(self):
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_amenity_to_dict(self):
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], 'Swimming Pool')

    def test_save_and_reload(self):
        self.storage.new(self.amenity)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        loaded_objects = new_storage.all()
        self.assertIn(self.amenity.id, loaded_objects)
        loaded_amenity = loaded_objects[self.amenity.id]
        self.assertEqual(loaded_amenity.id, self.amenity.id)
        self.assertEqual(loaded_amenity.name, self.amenity.name)

    def test_updated_at_after_save(self):
        am = Amenity()
        initial_updated_at = am.updated_at
        am.save()
        self.assertNotEqual(initial_updated_at, am.updated_at)

    def test_updated_at_type_after_save(self):
        j = Amenity()
        j.save()
        self.assertIsInstance(a.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
