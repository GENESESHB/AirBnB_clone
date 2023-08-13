#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import re
from shlex import split
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review


def tokenize_input(arg):
    """handle different cases involving curly braces {}
    and square brackets []"""
    indx_curly_brace = arg.find('{')
    curly_braces = arg.find('[')
    if indx_curly_brace != -1:
        result = [i.strip(",") for i in arg[:indx_curly_brace].split()]
        result.append(arg[indx_curly_brace:])
    elif curly_braces != -1:
        result = [i.strip(",") for i in arg[:curly_braces].split()]
        result.append(arg[curly_braces:])
    else:
        result = [i.strip(",") for i in arg.split()]
    return result


class_home = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
    "State": State
}


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

    def emptyline(self):
        """
        no inythings for empty line
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel

        ARGS:
            arg (str): the name of the class to create an instance of.
        Returns:
            None
        """
        if not arg:
            """
            if the class name is not define
            """
            print("** class name missing **")
            return

        class_name = arg

        if class_name not in models.storage.classes:
            """
            if class_name not here
            not fond in the models.storage.classes
            """
            print("** class doesn't exist **")
            return

        new_instance = models.storage.classes[class_name]()
        """
        creat a new_instance in the dictionary structurals
        models.storage.classes
        """
        new_instance.save()
        """
        save the new_instance
        """
        print(new_instance.id)
        """
        in this line print the id for new_instance
        """

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        all things of instance like what we define in structurals
        dectionary
        """
        args = arg.split()
        """
        we divise the arg & we take the numbers of words we have
        """
        if len(args) < 1:
            """
            if numbers of words we have < 1 then we missing somthings
            """
            print("** class name missing **")
            return

        class_name = args[0]
        """
        store the first element of list ARGS
        stock hem in class_name
        """

        if class_name not in models.storage.classes:
            '''
            if the class_name not in structurals dictioanary
            '''
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            '''
            just two elements after split()
            '''
            print("** instance id missing **")
            return

        objc_id = args[1]
        '''
        the variables number two store in objc_id
        '''
        ky = "{}.{}".format(class_name, objc_id)
        '''
        key define the classe_name & objc_id
        '''
        instances = models.storage.all()
        '''
        call the instance and store hem in variables instance
        '''

        if ky not in instances:
            print("** no instance found **")
            return

        print(instances[ky])

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and id
        """
        args = arg.split()
        if len(args) < 1:
            """
            if we have one word after split()
            """
            print("** class name missing **")
            return

        class_name = args[0]
        """
        store the arguments one in variables class_name
        """
        if class_name not in models.storage.classes:
            """
            check if the class_name not in structurals
            dictionary models.storage.classes
            """
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            """
            if we have two words after split()
            """
            print("** instance id missing **")
            return

        objc_id = args[1]
        """
        assingne the second element from args to variables
        objc_id
        """
        ky = "{}.{}".format(class_name, objc_id)
        """
        combinine the class_name & objc_id
        """
        instances = models.storage.all()
        """
        retrieves all instance using models.storage.all()
        """

        if ky not in instances:
            print("** no instance found **")
            return

        del instances[ky]
        """
        del = delete the instance associed with ky
        """
        models.storage.save()
        """
        save the update for deletation
        """

    def do_all(self, arg):
        """
        Prints string representations of all instances
        it take one optional argument arg
        """
        args = arg.split()
        """
        split the args
        and give heme to args
        """
        instances = models.storage.all()
        """
        we retrieve all instance and we store hem in the variable
        instance
        """

        if len(args) < 1:
            """
            after split we have one word
            """
            print([str(inst) for inst in instances.values()])
            """
            converting the instance to a string
            """
            return

        class_name = args[0]

        if class_name not in models.storage.classes:
            print("** class doesn't exist **")
            return

        f_ins = [str(inst) for ky, inst in instances.items()
                 if ky.startswith(class_name + ".")]
        print(f_ins)

    def do_update(self, arg):
        """
        Updates an instance based on class name, id, attribute, and value
        """
        args = tokenize_input(arg)
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

        objc_id = args[1]
        ky = "{}.{}".format(class_name, objc_id)
        instances = models.storage.all()

        if ky not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return
        if len(args) == 4:

            attribute_name = args[2]
            attribute_value = args[3]
            instance = instances[ky]
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        else:
            if type(eval(args[2])) == dict:
                instance = instances[ky]
                for key, value in eval(args[2]).items():
                    setattr(instance, key, value)
                instance.save()

    def default(self, arg):
        cnt = 0
        args = arg.split('.')
        all_objects = models.storage.all()
        if args[0] in models.storage.classes and args[1] == "all()":
            for ky in all_objects:
                class_name, objc = ky.split('.')
                if class_name == args[0]:
                    print(all_objects[ky])
        if args[0] in models.storage.classes and args[1] == "count()":
            for ky in all_objects:
                class_name, objc = ky.split('.')
                if class_name == args[0]:
                    cnt += 1
            print(cnt)
            return

        cmnd_dict = {
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            # Add more commands here...
        }

        args = arg.split('.')
        if len(args) != 2:
            print("Invalid command format")
            return

        class_name, cmnd_with_args = args
        cmnd_parts = cmnd_with_args.split("(")
        command = cmnd_parts[0]
        argu = cmnd_parts[1].rstrip(")")

        if class_name in models.storage.classes and command in cmnd_dict:
            comnd_function = cmnd_dict[command]
            comnd_function(f"{class_name} {argu}")
        else:
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
