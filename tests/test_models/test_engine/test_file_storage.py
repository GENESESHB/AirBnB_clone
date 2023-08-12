#!/usr/bin/python3

import unittest
import os
from models.base_model import BaseModel
from models.file_storage import FileStorage
from datetime import datetime

class TestFileStorage(unittest.TestCase):
    def test_attributes_exist(self):
        fs = FileStorage()
        self.assertTrue(hasattr(fs, '_FileStorage__file_path'))
        self.assertTrue(hasattr(fs, '_FileStorage__objects'))
        self.assertTrue(hasattr(fs, 'classes'))

    def test_all(self):
        fs = FileStorage()
        all_objects = fs.all()
        self.assertEqual(all_objects, fs._FileStorage__objects)

    def test_new(self):
        fs = FileStorage()
        obj = BaseModel()
        fs.new(obj)
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertTrue(obj_key in fs._FileStorage__objects)

    def test_save(self):
        fs = FileStorage()
        obj = BaseModel()
        fs.new(obj)
        fs.save()
        self.assertTrue(os.path.exists(fs._FileStorage__file_path))

    def test_reload(self):
        fs = FileStorage()
        obj = BaseModel()
        fs.new(obj)
        fs.save()
        fs.reload()
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertTrue(obj_key in fs._FileStorage__objects)

    def test_reload_empty_file(self):
        fs = FileStorage()
        fs.save()
        fs.reload()
        self.assertEqual(len(fs._FileStorage__objects), 0)

    def test_reload_nonexistent_file(self):
        fs = FileStorage()
        fs._FileStorage__file_path = "nonexistent.json"
        fs.reload()
        self.assertEqual(len(fs._FileStorage__objects), 0)

    def test_reload_with_data(self):
        fs = FileStorage()
        obj1 = BaseModel()
        obj2 = BaseModel()
        fs.new(obj1)
        fs.new(obj2)
        fs.save()

        new_fs = FileStorage()
        new_fs.reload()

        obj1_key = f"{obj1.__class__.__name__}.{obj1.id}"
        obj2_key = f"{obj2.__class__.__name__}.{obj2.id}"
        self.assertTrue(obj1_key in new_fs._FileStorage__objects)
        self.assertTrue(obj2_key in new_fs._FileStorage__objects)

    def test_reload_with_class_instance(self):
        fs = FileStorage()
        obj = BaseModel()
        fs.new(obj)
        fs.save()

        new_fs = FileStorage()
        new_fs.reload()

        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIsInstance(new_fs._FileStorage__objects[obj_key], BaseModel)

    def test_reload_with_datetime_attributes(self):
        fs = FileStorage()
        obj = BaseModel()
        fs.new(obj)
        fs.save()

        new_fs = FileStorage()
        new_fs.reload()

        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        reloaded_obj = new_fs._FileStorage__objects[obj_key]
        self.assertIsInstance(reloaded_obj.created_at, datetime)
        self.assertIsInstance(reloaded_obj.updated_at, datetime)

    def test_reload_with_custom_attributes(self):
        fs = FileStorage()
        obj = BaseModel()
        obj.custom_attr = "test"
        fs.new(obj)
        fs.save()

        new_fs = FileStorage()
        new_fs.reload()

        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        reloaded_obj = new_fs._FileStorage__objects[obj_key]
        self.assertEqual(reloaded_obj.custom_attr, "test")

if __name__ == "__main__":
    unittest.main()
