#!/usr/bin/python3
"""a unittest case module for the State Class."""

import unittest
import re
import json
from datetime import datetime
import time
from models.state import State
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    """
    test Cases for State class involved
    """

    def setUp(self):
        """
        this test methods for the set-up
        """
        pass

    def tearDown(self):
        """
        this test methods for breakes down
        """
        self.resetStorage()
        pass

    def resetStorage(self):
        """this a case for FileStorage data reset"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_for_instantiation(self):
        """
        a testing for the instantiation of State class
        """

        b = State()
        self.assertEqual(str(type(b)), "<class 'models.state.State'>")
        self.assertIsInstance(b, State)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_for_attributes(self):
        """
        testing for the attributes of State class
        """
        attributes = storage.attributes()["State"]
        o = State()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()
