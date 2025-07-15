#!/usr/bin/python3
"""Module that defines a Student class with JSON serialization capability."""


class Student:
    """
    Represents a student with first name, last name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        """
        Return a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary with all serializable attributes.
        """
        return self.__dict__
