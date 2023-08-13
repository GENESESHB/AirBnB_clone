#!/usr/bin/python3
"""
    TestConsole module
"""
import unittest
import sys
from io import StringIO
import re
from unittest.mock import patch
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """the TestConsole class"""
    def test_the_prompt(self):
        """
            a method that tests the prompt and
            checks if is the expected one
        """
        expected = "(hbnb)"
        self.assertEqual(expected, HBNBCommand.prompt)

    def test_help__cmd(self):
        """Test <help> cmd"""
        expected = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

"""
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("help")
            self.assertEqual(expected, file.getvalue())

    def test_help_show(self):
        """a method that test <help show> cmd"""
        expected = "Usage: show <class_name> <id> or <class>.show(<id>)\n"
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("help show")
            self.assertEqual(expected, file.getvalue())


if __name__ == "__main__":
    unittest.main()
