#!/usr/bin/python3
""" create class """
import cmd
import models
import os.path
import shlex
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.city import City

class_name = {"BaseModel": BaseModel, "User": User,
              "Place": Place, "City": City,
              "Amenity": Amenity, "State": State,
              "Review": Review}
instance = None


class HBNBCommand(cmd.Cmd):
    """ class HBNBCommand """

    prompt = "(hbnb)"

    def do_EOF(self, line):
        """Exits the program using EOF"""
        return True

    def do_quit(self, line):
        """The command quit exits the program"""
        return True

    def emptyline(self):
        """ Do nothing when the user enter a empty line + newline"""
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel,\
 saves it (to the JSON file) and prints the id. """

        if not line:
            print("** class name missing **")

        elif line is not None and line in class_name:
            for k, v in class_name.items():

                if line == k:
                    instance = class_name[k]()
                    key = '{}.{}'.format(type(instance).__name__, instance.id)

            models.storage.save()
            print(instance.id)

        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ Prints the string representation of an instance\
 based on the class name and id """

        if not line:
            print("** class name missing **")

        else:
            args = line.split()
            if args[0] not in class_name:
                print("** class doesn't exist **")

            elif len(args) == 1:
                print("** instance id missing **")

            else:
                key = '{}.{}'.format(args[0], args[1])
                all_instances = models.storage.all()
                if key in all_instances:
                    print(all_instances[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """

        if not line:
            print("** class name missing **")

        else:
            args = line.split()

            if args[0] not in class_name:
                print("** class doesn't exist **")

            elif len(args) == 1:
                print("** instance id missing **")

            else:
                key = "{}.{}".format(args[0], args[1])
                all_instances = models.storage.all()

                if key in all_instances:
                    all_instances.pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """ Prints all string representation of all instances\
 based or not on the class name """

        args = line.split()
        all_list = []
        all_instances = models.storage.all()
        if not line:
            for k, v in all_instances.items():
                all_list.append(str(all_instances[k]))
            print(all_list)
        else:
            if args[0] in class_name:
                for k, v in all_instances.items():
                    search = k.split('.')
                    if search[0] == args[0]:
                        all_list.append(str(all_instances[k]))
                print(all_list)

            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """ Updates an instance based on the class name and id
 by adding or updating attribute. """

        args = shlex.split(line)
        all_instances = models.storage.all()

        if len(args) < 1:
            print("** class name missing **")

        elif len(args) < 2:
            print("** instance id missing **")

        elif len(args) < 3:
            print("** attribute name missing **")

        elif len(args) < 4:
            print("** value missing **")

        else:
            if args[0] in class_name:
                key = "{}.{}".format(args[0], args[1])

                if key in all_instances:
                    for k, v in all_instances.items():
                        if k == key:
                            setattr(v, args[2], args[3])
                            v.save()
                else:
                    print("** no instance found **")

            else:
                print("** class doesn't exist **")

    def default(self, line):
        """ default method in case of no valid arguments """

        args = line.split('.')
        if len(args) > 1 and args[0] in class_name:
            if args[1] == 'all()':
                self.do_all(args[0])

            if args[1] == 'count()':
                count = 0
                all_instances = models.storage.all()

                for k, v in all_instances.items():
                    search = k.split('.')

                    if search[0] == args[0]:
                        count += 1
                print("{}".format(count))

        else:
            cmd.Cmd.default(self, line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
