#!/usr/bin/python3
"""Console for the HBNB project."""
import cmd
import shlex
import models
from models.base_model import BaseModel

list_class={"BaseModel"}

def split_input(txt):
    """split the txt into a list of arg"""
    if txt:
        return txt.split()
    else:
        return None

def check_input(arg):
    """ Parse the argument, and then checks if the class name is valid"""
    larg=split_input(arg)
    if larg == None:
        print("** class name missing **")
        "return False"
    elif larg[0] not in list_class:
        print("** class doesn't exist **")
        "return False"
    else:
        return larg
        

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
    
    def do_create(self, arg):
        """create a new instance of the specified class."""
        larg = check_input(arg)
        if larg:
            new_instance = globals()[larg[0]]()
            print(new_instance.id)
    
    def do_show(self, arg):
        """Show details of an instance of the specified class"""
        larg = check_input(arg)
        if larg:
            print(larg[0])
    
    def do_destroy(self, arg):
        """Delete an instance of the specified class"""
        larg = check_input(arg)
        if larg:
            print(larg[0])

    def do_update(self, arg):
        """Supdate attributes of a specific instance based"""
        larg = check_input(arg)
        if larg:
            print(larg[0])
    
    def do_all(self, arg):
        """Show details of all instances of the specified class"""
        larg = check_input(arg)
        if larg:
            print(larg[0])

        
if __name__ == '__main__':
    HBNBCommand().cmdloop()

