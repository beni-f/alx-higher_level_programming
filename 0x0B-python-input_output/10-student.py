#!/usr/bin/python3

class Student:
    """
        A class students that defines a student by:
        Attributes:
            first_name (str): name of student.
            last_name (str): name of student.
            age (int): age of student.
        Methods:
            __init__ - initializes the Student instance.
            to_json - retrieves dictionary repr of Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialises Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        """
            Retrieves a dictionary representation of a Student instance
        """
        if attrs is not None:
            json_dict = {k : self.__dict__[k] for k in self.__dict__.keys() & attrs}
            return json_dict
        else:
            return self.__dict__
