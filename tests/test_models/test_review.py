#!/usr/bin/python3

import unittest
from models.review import Review
from datetime import datetime

class TestReview(unittest.TestCase):
    def test_attributes_exist(self):
        r = Review()
        self.assertTrue(hasattr(r, 'id'))
        self.assertTrue(hasattr(r, 'created_at'))
        self.assertTrue(hasattr(r, 'updated_at'))
        self.assertTrue(hasattr(r, 'place_id'))
        self.assertTrue(hasattr(r, 'text'))
        self.assertTrue(hasattr(r, 'user_id'))

    def test_id_is_string(self):
        r = Review()
        self.assertIsInstance(r.id, str)

    def test_created_at_is_datetime(self):
        r = Review()
        self.assertIsInstance(r.created_at, datetime)

    def test_updated_at_is_datetime(self):
        r = Review()
        self.assertIsInstance(r.updated_at, datetime)

    def test_place_id_is_empty_string(self):
        r = Review()
        self.assertEqual(r.place_id, "")

    def test_text_is_empty_string(self):
        r = Review()
        self.assertEqual(r.text, "")

    def test_user_id_is_empty_string(self):
        r = Review()
        self.assertEqual(r.user_id, "")

    def test_str_representation(self):
        r = Review()
        r.id = "123"
        r.place_id = "456"
        r.text = "Sample text"
        r.user_id = "789"
        self.assertIn("[Review] (123)", str(r))
        self.assertIn("'place_id': '456'", str(r))
        self.assertIn("'text': 'Sample text'", str(r))
        self.assertIn("'user_id': '789'", str(r))

    def test_to_dict(self):
        r = Review()
        r.id = "123"
        r.place_id = "456"
        r.text = "Sample text"
        r.user_id = "789"
        r_dict = r.to_dict()
        self.assertEqual(r_dict['id'], '123')
        self.assertEqual(r_dict['place_id'], '456')
        self.assertEqual(r_dict['text'], 'Sample text')
        self.assertEqual(r_dict['user_id'], '789')
        self.assertIn('__class__', r_dict)
        self.assertIn('created_at', r_dict)
        self.assertIn('updated_at', r_dict)

    def test_to_dict_datetime_attributes(self):
        r = Review()
        r_dict = r.to_dict()
        self.assertIsInstance(r_dict['created_at'], str)
        self.assertIsInstance(r_dict['updated_at'], str)

    def test_to_dict_with_arg(self):
        r = Review()
        with self.assertRaises(TypeError):
            r.to_dict(None)

if __name__ == "__main__":
    unittest.main()
