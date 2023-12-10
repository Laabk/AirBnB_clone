#!/usr/bin/python3
"""this a Unittest case module for the Place Class."""

import unittest
import re
import jso
from datetime import datetime
import time
from models.place import Place
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    """
    testing cases for the Place class
    """

    def setUp(self):
        """
        a test methods for the set-up case
        """
        pass

    def tearDown(self):
        """a test methods for the break apart case"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """this resets fileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_for_instantiation(self):
        """
        testing for the instantiation of Place class
        """

        b = Place()
        self.assertEqual(str(type(b)), "<class 'models.place.Place'>")
        self.assertIsInstance(b, Place)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_for_attributes(self):
        """
        testing for the attributes of Place class involved
        """
        attributes = storage.attributes()["Place"]
        o = Place()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()
