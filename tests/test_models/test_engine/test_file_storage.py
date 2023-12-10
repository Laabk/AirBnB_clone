#!/usr/bin/python3
"""Unittest module for the FileStorage class."""

import unittest
import re
import json
import os
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    the test Cases for the FileStorage class
    """

    def setUp(self):
        """this Sets up test methods class"""
        pass

    def resetStorage(self):
        """
        fileStorage data reset case test
        """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """the Tears/breakes down test methods case"""
        self.resetStorage()
        pass

    def test_for_instantiation(self):
        """
        instantiation case test for the storage class
        """
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_for_init_no_args(self):
        ""
        "esting the init case with no arguments
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(e.exception), msg)

    def test_for_init_many_args(self):
        """
        testing the init case with many arguments
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            b = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        msg = "object() takes no parameters"
        self.assertEqual(str(e.exception), msg)

    def test_for_attributes(self):
        """teesting the class attributes."""
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def help_test_all(self, classname):
        """
        tests helper for all option for classname case
        """
        self.resetStorage()
        self.assertEqual(storage.all(), {})

        o = storage.classes()[classname]()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], o)

    def test_for_all_base_model(self):
        """testing the  all opt for BaseModel."""
        self.help_test_all("BaseModel")

    def test_for_all_user(self):
        """testing for all() the opt for User."""
        self.help_test_all("User")

    def test_for_all_state(self):
        """testing for the all opt for State."""
        self.help_test_all("State")

    def test_for_all_city(self):
        """testing for the all() method for City."""
        self.help_test_all("City")

    def test_for_all_amenity(self):
        """testing for the all opt for Amenity."""
        self.help_test_all("Amenity")

    def test_for_all_place(self):
        """testing for all opt for Place."""
        self.help_test_all("Place")

    def test_for_all_review(self):
        """testing all opt for Review."""
        self.help_test_all("Review")

    def help_test_all_multiple(self, classname):
        """
        test helps for all opt with many objects for classname
        """
        self.resetStorage()
        self.assertEqual(storage.all(), {})

        cls = storage.classes()[classname]
        objs = [cls() for i in range(1000)]
        [storage.new(o) for o in objs]
        self.assertEqual(len(objs), len(storage.all()))
        for o in objs:
            key = "{}.{}".format(type(o).__name__, o.id)
            self.assertTrue(key in storage.all())
            self.assertEqual(storage.all()[key], o)

    def test_for_all_multiple_base_model(self):
        """
        testing the all opt with many objects
        """
        self.help_test_all_multiple("BaseModel")

    def test_for_all_multiple_user(self):
        """
        testing for all_multiple() method for User
        """
        self.help_test_all_multiple("User")

    def test_for_all_multiple_state(self):
        """
        testing the all_multiple for for State
        """
        self.help_test_all_multiple("State")

    def test_for_all_multiple_city(self):
        """testing for all_multiple opt for City."""
        self.help_test_all_multiple("City")

    def test_for_all_multiple_amenity(self):
        """testing for all_multiple for Amenity."""
        self.help_test_all_multiple("Amenity")

    def test_for_all_multiple_place(self):
        """testing the all_multiple opt for Place."""
        self.help_test_all_multiple("Place")

    def test_for_all_multiple_review(self):
        """testing for all_multiple for Review."""
        self.help_test_all_multiple("Review")

    def test_for_all_no_args(self):
        """testing the all opt with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.all()
        msg = "all() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_for_all_excess_args(self):
        """
        teestings the all option with too many arguments
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.all(self, 98)
        msg = "all() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def help_test_new(self, classname):
        """Helps tests new() method for classname."""
        self.resetStorage()
        cls = storage.classes()[classname]
        o = cls()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertTrue(key in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], o)

    def test_for_new_base_model(self):
        """testing the new option for BaseModel."""
        self.help_test_new("BaseModel")

    def test_for_new_user(self):
        """testings the new option for User."""
        self.help_test_new("User")

    def test_for_new_state(self):
        """teesting the new option for State."""
        self.help_test_new("State")

    def test_for_new_city(self):
        """testing the new option for City."""
        self.help_test_new("City")

    def test_for_new_amenity(self):
        """testing the new opt for Amenity."""
        self.help_test_new("Amenity")

    def test_for_new_place(self):
        """testing the new opt for Place."""
        self.help_test_new("Place")

    def test_for_new_review(self):
        """testing the new opt for Review."""
        self.help_test_new("Review")

    def test_for_new_no_args(self):
        """Testing the new opt with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            storage.new()
        msg = "new() missing 1 required positional argument: 'obj'"
        self.assertEqual(str(e.exception), msg)

    def test_for_new_excess_args(self):
        """Tests new() with too many arguments."""
        self.resetStorage()
        b = BaseModel()
        with self.assertRaises(TypeError) as e:
            storage.new(b, 98)
        msg = "new() takes 2 positional arguments but 3 were given"
        self.assertEqual(str(e.exception), msg)

    def help_test_save(self, classname):
        """the helps tests save opt for classname."""
        self.resetStorage()
        cls = storage.classes()[classname]
        o = cls()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        d = {key: o.to_dict()}
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_for_save_base_model(self):
        """testing the save option for BaseModel."""
        self.help_test_save("BaseModel")

    def test_for_save_user(self):
        """testimg save opt for User."""
        self.help_test_save("User")

    def test_for_save_state(self):
        """testing the save opt for State."""
        self.help_test_save("State")

    def test_for_save_city(self):
        """testing the save opt for City."""
        self.help_test_save("City")

    def test_for_save_amenity(self):
        """testing the save opt for Amenity."""
        self.help_test_save("Amenity")

    def test_for_save_place(self):
        """testing save opt for Place."""
        self.help_test_save("Place")

    def test_for_save_review(self):
        """testing the save opt for Review."""
        self.help_test_save("Review")

    def test_for_save_no_args(self):
        """testing the save opt with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_for_save_excess_args(self):
        """testing the save with too many arguments"""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def help_test_reload(self, classname):
        """
        the test-helps for the reload opt for classname
        """
        self.resetStorage()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        cls = storage.classes()[classname]
        o = cls()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        storage.save()
        storage.reload()
        self.assertEqual(o.to_dict(), storage.all()[key].to_dict())

    def test_for_reload_base_model(self):
        """Testing the reload opt for BaseModel."""
        self.help_test_reload("BaseModel")

    def test_for_reload_user(self):
        """Testing reload opt for User."""
        self.help_test_reload("User")

    def testfor5_reload_state(self):
        """testing the reload opt for State."""
        self.help_test_reload("State")

    def test_for_reload_city(self):
        """Testing reload opot for City."""
        self.help_test_reload("City")

    def test_for_reload_amenity(self):
        """testing the reload opt for Amenity."""
        self.help_test_reload("Amenity")

    def test_for_reload_place(self):
        """
        testing the reload opt for Place
        """
        self.help_test_reload("Place")

    def test_for_reload_review(self):
        """
        testingg the reload opt for the Review
        """
        self.help_test_reload("Review")

    def help_test_reload_mismatch(self, classname):
        """
        the helpers test reload() method for classname.
        """
        self.resetStorage()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})

        cls = storage.classes()[classname]
        o = cls()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        storage.save()
        o.name = "Laura"
        storage.reload()
        self.assertNotEqual(o.to_dict(), storage.all()[key].to_dict())

    def test_for_reload_mismatch_base_model(self):
        """
        tests the reload opt for the mismatch for BaseModel
        """
        self.help_test_reload_mismatch("BaseModel")

    def test_5_reload_mismatch_user(self):
        """
        tests ther reload_mismatch opt for the for User
        """
        self.help_test_reload_mismatch("User")

    def test_for_reload_mismatch_state(self):
        """
        tests the reload_mismatch opt for State
        """
        self.help_test_reload_mismatch("State")

    def test_5_reload_mismatch_city(self):
        """
        testsing the reload_mismatch optfor the City involved
        """
        self.help_test_reload_mismatch("City")

    def test_for_reload_mismatch_amenity(self):
        """
        testing the reload_mismatch method for Amenity involved
        """
        self.help_test_reload_mismatch("Amenity")

    def test_for_reload_mismatch_place(self):
        """
        testing the reload_mismatch opt for the Place
        """
        self.help_test_reload_mismatch("Place")

    def test_for_reload_mismatch_review(self):
        """
        testing the reload_mismatch opt for any review
        """
        self.help_test_reload_mismatch("Review")

    def test_for_reload_no_args(self):
        """
        testing the reload opt with no arguments involved
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.reload()
        msg = "reload() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_for_reload_excess_args(self):
        """
        tests the reload opt with too many arguments
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.reload(self, 98)
        msg = "reload() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
    unittest.main()
