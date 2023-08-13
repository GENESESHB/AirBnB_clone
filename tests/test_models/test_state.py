#!/usr/bin/python3

"""
defines unittest for state
"""
import os
from datetime import datetime
import unittest
from models.state import State  # Import the State class you defined

class TestState(unittest.TestCase):

    def setUp(self):
        """
        Create a State instance for testing
        """
        self.state = State()

    def test_attributes_initialization(self):
        self.assertEqual(self.state.name, "")

    def test_attribute_types(self):
        self.assertIsInstance(self.state.name, str)

    def test_update_attributes(self):
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

    def test_str_representation(self):
        self.state.name = "California"
        self.assertEqual(str(self.state), "[State] (None) {'name': 'California'}")

    def test_to_dict_method(self):
        self.state.name = "New York"
        state_dict = self.state.to_dict()

        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['name'], "New York")
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)

    def test_default_attributes(self):
        self.assertEqual(self.state.name, "")

    def test_non_empty_name(self):
        self.state.name = "Texas"
        self.assertEqual(self.state.name, "Texas")

    def test_attribute_bounds(self):
        self.state.name = "A" * 256  # Assuming a max length of 255 characters
        self.assertEqual(len(self.state.name), 255)

    def test_equality_with_different_instance(self):
        st1 = State()
        st1.id = "123"
        st2 = State()
        st2.id = "123"
        self.assertEqual(st1, st2)

    def test_equality_with_different_name(self):
        sta1 = State()
        sta1.name = "California"
        sta2 = State()
        sta2.name = "California"
        self.assertEqual(sta1, sta2)

    def test_inequality_with_different_instance(self):
        stae1 = State()
        stae2 = State()
        self.assertNotEqual(stae1, stae2)

    def test_str_output(self):
        self.state.name = "Florida"
        self.assertEqual(str(self.state), "[State] (None) {'name': 'Florida'}")

    def test_to_dict_values(self):
        self.state.name = "Georgia"
        state_dict = self.state.to_dict()

        self.assertEqual(state_dict['name'], "Georgia")
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)

if __name__ == '__main__':
    unittest.main()
