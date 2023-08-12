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
        bs = BaseModel()
        self.assertIsInstance(bs, BaseModel)
        self.assertIsInstance(bs.id, str)
        self.assertIsInstance(bs.created_at, datetime)
        self.assertIsInstance(bs.updated_at, datetime)

    def test_str(self):
        bh = BaseModel()
        expected_str = f"[BaseModel] ({bh.id}) {bh.__dict__}"
        self.assertEqual(str(bh), expected_str)

    def test_save(self):
        bh = BaseModel()
        old_updated_at = bh.updated_at
        bh.save()
        self.assertNotEqual(old_updated_at, bh.updated_at)

    def test_to_dict(self):
        bj = BaseModel()
        bj_dict = bj.to_dict()
        self.assertIsInstance(bj_dict, dict)
        self.assertEqual(bj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(datetime.strptime(bj_dict['created_at'],
            "%Y-%m-%dT%H:%M:%S.%f"), datetime)
        self.assertIsInstance(datetime.strptime(bj_dict['updated_at'], 
            "%Y-%m-%dT%H:%M:%S.%f"), datetime)

    def test_init_with_args(self):
        args = {"id": "test_id", "created_at": "2023-08-12T12:34:56.789",
                "updated_at": "2023-08-12T12:34:56.789", "name": "John"}
        bp = BaseModel(**args)
        self.assertEqual(bp.id, "test_id")
        self.assertEqual(bp.created_at, datetime(
            2023, 8, 12, 12, 34, 56, 789000))
        self.assertEqual(bp.updated_at, datetime(
            2023, 8, 12, 12, 34, 56, 789000))
        self.assertEqual(bp.name, "John")

    def test_to_dict_with_new_attribute(self):
        bb = BaseModel()
        bb.name = "Alice"
        bb_dict = bb.to_dict()
        self.assertEqual(bb_dict['name'], "Alice")

    def test_to_dict_with_arg(self):
        bb = BaseModel()
        with self.assertRaises(TypeError):
            bb.to_dict(None)

    def test_created_at_is_before_updated_at(self):
        bb = BaseModel()
        self.assertLess(bb.created_at, bb.updated_at)

    def test_save_updates_updated_at(self):
        h = BaseModel()
        old_updated_at = h.updated_at
        h.save()
        self.assertGreater(h.updated_at, old_updated_at)

    def test_updated_at_is_different_after_time_passes(self):
        cv = BaseModel()
        old_updated_at = cv.updated_at
        # Sleep for a short time to simulate passage of time
        timedelta_seconds = 1
        sleep(timedelta_seconds)
        cv.save()
        self.assertGreater(cv.updated_at, old_updated_at)

    def test_to_dict_includes_all_attributes(self):
        args = {"id": "test_id", "created_at": "2023-08-12T12:34:56.789",
                "updated_at": "2023-08-12T12:34:56.789", "name": "John"}
        ok = BaseModel(**args)
        ok_dict = ok.to_dict()
        for key, value in args.items():
            self.assertIn(key, ok_dict)
            self.assertEqual(ok_dict[key], value)

if __name__ == "__main__":
    unittest.main()
