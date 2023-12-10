#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
import re
import json
from datetime import datetime
import time
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """
    testing modules for the Amenity class.
    """

    def setUp(self):
        """module for test set-up."""
        pass

    def tearDown(self):
        """test methods breaks off"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """the FileStorage data resets"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_for_instantiation(self):
        """testing the instantiation Amenity class."""

        b = Amenity()
        self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_for_attributes(self):
        """testing the attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]
        o = Amenity()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()

