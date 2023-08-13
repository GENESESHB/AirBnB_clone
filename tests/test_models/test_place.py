#!/usr/bin/python3

"""
defines all unittest for the file
"""
import os 
from datetime import datetime
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):

    def setUp(self):
        """
        Create a Place instance for testing
        """
        self.place = Place()

    def test_attributes_initialization(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_attribute_types(self):
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_update_attributes(self):
        self.place.city_id = "test_city_id"
        self.place.user_id = "test_user_id"
        self.place.name = "Test Place"
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.price_by_night = 150
        self.place.max_guest = 6
        self.place.longitude = -122.0840
        self.place.latitude = 37.4219
        self.place.amenity_ids = ["wifi", "pool"]

        self.assertEqual(self.place.city_id, "test_city_id")
        self.assertEqual(self.place.user_id, "test_user_id")
        self.assertEqual(self.place.name, "Test Place")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.price_by_night, 150)
        self.assertEqual(self.place.max_guest, 6)
        self.assertEqual(self.place.longitude, -122.0840)
        self.assertEqual(self.place.latitude, 37.4219)
        self.assertListEqual(self.place.amenity_ids, ["wifi", "pool"])

    def test_str_representation(self):
        self.place.name = "Test Place"
        self.assertEqual(str(self.place), "<Place> Test Place")

    def test_eq_comparison(self):
        blassa1 = Place()
        blassa1.id = "123"
        blassa2 = Place()
        blassa2.id = "123"
        self.assertEqual(blassa1, blassa2)

    def test_to_dict_method(self):
        self.place.name = "Test Place"
        self.place.price_by_night = 100
        place_dict = self.place.to_dict()

        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['name'], "Test Place")
        self.assertEqual(place_dict['price_by_night'], 100)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)

    def test_default_attributes(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_non_empty_amenity_ids(self):
        self.place.amenity_ids = ["wifi", "pool", "gym"]
        self.assertListEqual(self.place.amenity_ids, ["wifi", "pool", "gym"])

    def test_equality_with_different_instance(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1, pl2)

    def test_attribute_bounds(self):
        self.place.number_rooms = -1
        self.assertEqual(self.place.number_rooms, 0)

    def test_attribute_constraints(self):
        self.place.name = "A" * 500
        self.assertEqual(len(self.place.name), 255)

if __name__ == '__main__':
    unittest.main()
