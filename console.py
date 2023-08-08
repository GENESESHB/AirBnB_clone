#!/usr/bin/python3
"""Console for the HBNB project."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the console using Ctrl-D (EOF)."""
        print("")  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing on empty line + ENTER."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

