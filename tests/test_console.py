#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
import your_module_name

class TestHBNBCommand(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    def assert_stdout(self, expected_output, func, *args):
        with patch("sys.stdout", new_callable=StringIO)
        as mock_stdout:
            func(*args)
            self.assertEqual(mock_stdout.getvalue(),
                     expected_output)

    def test_quit_command(self):
        with patch("builtins.input", return_value="quit"):
            with self.assertRaises(SystemExit):
                your_module_name.HBNBCommand().cmdloop()

    def test_show_command(self):
        with patch("builtins.input",
                side_effect=["show BaseModel 123", "quit"]):
            self.assert_stdout("** class doesn't exist **\n",
                    your_module_name.HBNBCommand().cmdloop)

    def test_create_command(self):
        with patch("builtins.input",
                 side_effect=["create BaseModel", "quit"]):
            self.assert_stdout("** class doesn't exist **\n",
                     your_module_name.HBNBCommand().cmdloop)

    def test_destroy_command(self):
        with patch("builtins.input",
                side_effect=["destroy BaseModel 123", "quit"]):
            self.assert_stdout("** class doesn't exist **\n",
                    your_module_name.HBNBCommand().cmdloop)

    def test_all_command(self):
        with patch("builtins.input", side_effect=["all BaseModel", "quit"]):
            self.assert_stdout("[]\n", your_module_name.HBNBCommand().cmdloop)

    def test_all_with_objects(self):
        with patch("builtins.input",
                side_effect=["create BaseModel", "create User", "all BaseModel", "quit"]):
            self.assert_stdout("[]\n[", your_module_name.HBNBCommand().cmdloop)

    def test_update_command(self):
        with patch("builtins.input",
                side_effect=["update BaseModel 123 name John", "quit"]):
            self.assert_stdout("** class doesn't exist **\n",
                    your_module_name.HBNBCommand().cmdloop)

    def test_default_command(self):
        with patch("builtins.input",
                side_effect=["InvalidCommand", "quit"]):
            self.assert_stdout("** class doesn't exist **\n",
                    your_module_name.HBNBCommand().cmdloop)


if __name__ == '__main__':
    unittest.main()
