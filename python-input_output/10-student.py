#!/usr/bin/python3
"""Module that defines a Student class with filtered JSON serialization."""


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

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve.
                If None or not a list, all attributes are returned.

        Returns:
            dict: Dictionary of selected attributes.
        """
        if isinstance(attrs, list) and all(type(attr) == str for attr in attrs):
            filtered_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return filtered_dict
        else:
            return self.__dict__.copy()
