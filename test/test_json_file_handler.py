#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""


import unittest
import os
from pig_game.json_file_handler import JSONFileHandler


class TestJSONFileHandlerClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        self.test_dir = "./pig_game/TestGameData"
        res = JSONFileHandler("", dir_path=self.test_dir)
        exp = JSONFileHandler
        self.assertIsInstance(res, exp)

        # Cleanup directory
        os.rmdir(self.test_dir)

    def test_file_is_missing(self):
        """Test auto creation of data file."""
        self.test_dir = "./pig_game/TestGameData"
        json_file_handler = JSONFileHandler(self.test_dir+"/DoesntExist.json",
                                            dir_path=self.test_dir)
        res = json_file_handler.is_missing_or_empty()
        exp = True
        self.assertEqual(res, exp)

        # Cleanup directory
        os.remove(self.test_dir+"/DoesntExist.json")
        os.rmdir(self.test_dir)

    def test_file_is_empty(self):
        """Test correcting content of empty file."""
        self.test_dir = "./pig_game/TestGameData"
        json_file_handler = JSONFileHandler(self.test_dir+"/DoesntExist.json",
                                            dir_path=self.test_dir)
        json_file_handler.write({})
        res = json_file_handler.is_missing_or_empty()
        exp = False
        self.assertEqual(res, exp)

        # Cleanup directory
        os.remove(self.test_dir+"/DoesntExist.json")
        os.rmdir(self.test_dir)

    def test_read(self):
        """Test correcting content of empty file."""
        self.test_dir = "./pig_game/TestGameData"
        json_file_handler = JSONFileHandler(self.test_dir+"/DoesntExist.json",
                                            dir_path=self.test_dir)
        json_file_handler.write({
            "1": {
                "user_id": 1,
                "username": "TesUser1"
            }
        })
        res = json_file_handler.read()
        exp = {
            "1": {
                "user_id": 1,
                "username": "TesUser1"
            }
        }
        self.assertDictEqual(res, exp)

        # Cleanup directory
        os.remove(self.test_dir+"/DoesntExist.json")
        os.rmdir(self.test_dir)


if __name__ == "__main__":
    unittest.main()
