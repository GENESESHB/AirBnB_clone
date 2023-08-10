#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        win you tape (quit) it s down => exit
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        & print a new line empty after you tape (quit)
        """
        print()
        return True

    def do_create(self, arg):
        """
        Create a new instance of BaseModel
        """
        if not arg:
            """
            if the class nameis not define
            """
            print("** class name missing **")
            return

        class_name = arg

        if class_name not in models.storage.classes:
            """
            if class name not here
            """
            print("** class doesn't exist **")
            return

        new_instance = models.storage.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in models.storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        instances = models.storage.all()

        if key not in instances:
            print("** no instance found **")
            return

        print(instances[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and id
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in models.storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        instances = models.storage.all()

        if key not in instances:
            print("** no instance found **")
            return

        del instances[key]
        models.storage.save()

    def do_all(self, arg):
        """
        Prints string representations of all instances
        """
        args = arg.split()
        instances = models.storage.all()

        if len(args) < 1:
            print([str(inst) for inst in instances.values()])
            return

        class_name = args[0]

        if class_name not in models.storage.classes:
            print("** class doesn't exist **")
            return

        filtered_instances = [str(inst) for key, inst in instances.items() if key.startswith(class_name + ".")]
        print(filtered_instances)

    def do_update(self, arg):
        """
        Updates an instance based on class name, id, attribute, and value
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in models.storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        instances = models.storage.all()

        if key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        instance = instances[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

