#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""


import unittest
import os
from pig_game.utils.user_data_handler import UserDataHandler


class TestUserDataHandlerClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        self.test_dir = "./pig_game/TestGameData"
        res = UserDataHandler(self.test_dir + "/UserData.json", dir_path=self.test_dir)
        exp = UserDataHandler
        self.assertIsInstance(res, exp)

        # Cleanup directory
        os.rmdir(self.test_dir)

    def test_get_user_id(self):
        """Test auto creation of data file."""
        self.test_dir = "./pig_game/TestGameData"
        user_data = UserDataHandler(
            self.test_dir + "/UserData.json", dir_path=self.test_dir
        )

        user_data.write({"55": {"user_id": 55, "username": "Test"}})

        res = user_data.get_user_id("Test")
        exp = 55
        self.assertEqual(res, exp)

        res_not_existing = user_data.get_user_id("Test1")
        exp1 = None
        self.assertEqual(res_not_existing, exp1)

        # Cleanup directory
        os.remove(self.test_dir + "/UserData.json")
        os.rmdir(self.test_dir)

    def test_add_user(self):
        """Test auto creation of data file."""
        self.test_dir = "./pig_game/TestGameData"
        user_data = UserDataHandler(
            self.test_dir + "/UserData.json", dir_path=self.test_dir
        )

        user_data.add_user("Test0")

        res = user_data.read()
        exp = {"0": {"user_id": 0, "username": "Test0"}}
        self.assertDictEqual(res, exp)

        # Cleanup directory
        os.remove(self.test_dir + "/UserData.json")
        os.rmdir(self.test_dir)

    def test_update_username(self):
        """Test auto creation of data file."""
        self.test_dir = "./pig_game/TestGameData"
        user_data = UserDataHandler(
            self.test_dir + "/UserData.json", dir_path=self.test_dir
        )

        user_data.add_user("Test0")
        user_data.update_username("Test0", "Test0NewUsername")

        res = user_data.read()
        exp = {"0": {"user_id": 0, "username": "Test0NewUsername"}}
        self.assertDictEqual(res, exp)
        self.assertFalse(user_data.add_user("Test0NewUsername"))

        # Cleanup directory
        os.remove(self.test_dir + "/UserData.json")
        os.rmdir(self.test_dir)

    def test_update_username_taken(self):
        """Test auto creation of data file."""
        self.test_dir = "./pig_game/TestGameData"
        user_data = UserDataHandler(
            self.test_dir + "/UserData.json", dir_path=self.test_dir
        )

        user_data.add_user("Test0")
        user_data.add_user("Test1")
        user_data.update_username(0, "Test1")

        res = user_data.read()
        exp = {
            "0": {"user_id": 0, "username": "Test0"},
            "1": {"user_id": 1, "username": "Test1"},
        }
        self.assertDictEqual(res, exp)
        self.assertFalse(user_data.update_username(99, "UserDontExist"))

        # Cleanup directory
        os.remove(self.test_dir + "/UserData.json")
        os.rmdir(self.test_dir)

    def test_get_username(self):
        """Test auto creation of data file."""
        self.test_dir = "./pig_game/TestGameData"
        user_data = UserDataHandler(
            self.test_dir + "/UserData.json", dir_path=self.test_dir
        )
        self.assertIsNone(user_data.get_username(99999999))

        # Cleanup directory
        os.remove(self.test_dir + "/UserData.json")
        os.rmdir(self.test_dir)


if __name__ == "__main__":
    unittest.main()
