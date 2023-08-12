#!/usr/bin/python3
"""
defines unittest for models.base_model
"""

import os
from time import sleep
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertIsInstance(b.id, str)
        self.assertIsInstance(b.created_at, datetime)
        self.assertIsInstance(b.updated_at, datetime)

    def test_str(self):
        b = BaseModel()
        expected_str = f"[BaseModel] ({b.id}) {b.__dict__}"
        self.assertEqual(str(b), expected_str)

    def test_save(self):
        b = BaseModel()
        old_updated_at = b.updated_at
        b.save()
        self.assertNotEqual(old_updated_at, b.updated_at)

    def test_to_dict(self):
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertIsInstance(b_dict, dict)
        self.assertEqual(b_dict['__class__'], 'BaseModel')
        self.assertIsInstance(datetime.strptime(b_dict['created_at'],
            "%Y-%m-%dT%H:%M:%S.%f"), datetime)
        self.assertIsInstance(datetime.strptime(b_dict['updated_at'], 
            "%Y-%m-%dT%H:%M:%S.%f"), datetime)

    def test_init_with_args(self):
        args = {"id": "test_id", "created_at": "2023-08-12T12:34:56.789",
                "updated_at": "2023-08-12T12:34:56.789", "name": "John"}
        b = BaseModel(**args)
        self.assertEqual(b.id, "test_id")
        self.assertEqual(b.created_at, datetime(
            2023, 8, 12, 12, 34, 56, 789000))
        self.assertEqual(b.updated_at, datetime(
            2023, 8, 12, 12, 34, 56, 789000))
        self.assertEqual(b.name, "John")

    def test_to_dict_with_new_attribute(self):
        b = BaseModel()
        b.name = "Alice"
        b_dict = b.to_dict()
        self.assertEqual(b_dict['name'], "Alice")

    def test_to_dict_with_arg(self):
        b = BaseModel()
        with self.assertRaises(TypeError):
            b.to_dict(None)

    def test_created_at_is_before_updated_at(self):
        b = BaseModel()
        self.assertLess(b.created_at, b.updated_at)

    def test_save_updates_updated_at(self):
        b = BaseModel()
        old_updated_at = b.updated_at
        b.save()
        self.assertGreater(b.updated_at, old_updated_at)

    def test_updated_at_is_different_after_time_passes(self):
        b = BaseModel()
        old_updated_at = b.updated_at
        # Sleep for a short time to simulate passage of time
        timedelta_seconds = 1
        sleep(timedelta_seconds)
        b.save()
        self.assertGreater(b.updated_at, old_updated_at)

    def test_to_dict_includes_all_attributes(self):
        args = {"id": "test_id", "created_at": "2023-08-12T12:34:56.789",
                "updated_at": "2023-08-12T12:34:56.789", "name": "John"}
        b = BaseModel(**args)
        b_dict = b.to_dict()
        for key, value in args.items():
            self.assertIn(key, b_dict)
            self.assertEqual(b_dict[key], value)

if __name__ == "__main__":
    unittest.main()
