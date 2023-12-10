#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
import re
import json
from datetime import datetime
import time
from models.user import User
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    """
    testing cases for User class involved
    """

    def setUp(self):
        """
        test methods for the set-up case
        """
        pass

    def tearDown(self):
        """this test methods breaks down"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """this case resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """
        testing fo the instantiation of User class.
        """

        b = User()
        self.assertEqual(str(type(b)), "<class 'models.user.User'>")
        self.assertIsInstance(b, User)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_for_attributes(self):
        """
        testing for the attributes of User class
        """
        attributes = storage.attributes()["User"]
        o = User()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()
