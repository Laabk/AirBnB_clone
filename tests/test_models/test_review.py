#!/usr/bin/python3
"""this a Unittest case module for the Review Class."""

import unittest
import re
import json
from datetime import datetime
import time
from models.review import Review
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    """
    a test Cases for the Review class.
    """

    def setUp(self):
        """a test methods for the set-up"""
        pass

    def tearDown(self):
        """
        this test methods for the break down cae
        """
        self.resetStorage()
        pass

    def resetStorage(self):
        """
        this methods resets FileStorage data
        """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_for_instantiation(self):
        """
        this for testing instantiation of Review class
        """

        b = Review()
        self.assertEqual(str(type(b)), "<class 'models.review.Review'>")
        self.assertIsInstance(b, Review)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_for_attributes(self):
        """
        testing all the attributes of Review class involved
        """
        attributes = storage.attributes()["Review"]
        o = Review()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()
