#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from datetime import datetime
import re
import json
import time
from models.city import City
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    """the test Cases for the City class involved"""

    def setUp(self):
        """test methods set-up case"""
        pass

    def tearDown(self):
        """
        test methods for the break down case
        """
        self.resetStorage()
        pass

    def resetStorage(self):
        """FileStorage data reset"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_for_instantiation(self):
        """
        testing the instantiation of City class.
        """

        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_for_attributes(self):
        """
        testing for the attributes of City class.
        """
        attributes = storage.attributes()["City"]
        o = City()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()
