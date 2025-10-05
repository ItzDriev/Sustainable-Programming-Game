#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""


from pathlib import Path
import unittest
import os
from guess import data_handler


class TestDataHandlerClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        self.test_dir = "./guess/TestGameData"
        res = data_handler.DataHandler(self.test_dir)
        exp = data_handler.DataHandler
        self.assertIsInstance(res, exp)

        # Cleanup directory
        os.rmdir(self.test_dir)

    def test_dir_creation(self):
        """Test directionry creation"""
        self.test_dir = "./guess/TestGameData"
        self.data_handler = data_handler.DataHandler(self.test_dir)
        self.test_dir = Path(self.test_dir)

        self.assertTrue(self.test_dir.exists())

        # Cleanup directory
        os.rmdir(self.test_dir)

    def test_file_creation(self):
        """Test data file creation"""
        self.test_dir = "./guess/TestGameData"
        self.data_handler = data_handler.DataHandler(self.test_dir)
        self.test_dir = Path(self.test_dir)

        data = {
        0: {
            "user_id": 0,
            "username": "TestUsername"
            }
        }

        self.data_handler.write_user_data_json(data)

        self.assertTrue((self.test_dir/"UserData.json").exists())

        # Cleanup file
        os.remove(self.test_dir/"UserData.json")
        os.rmdir(self.test_dir)

    def test_read_user_data(self):
        """Test user data file reading"""
        self.test_dir = "./guess/TestGameData"
        self.data_handler = data_handler.DataHandler(self.test_dir)
        self.test_dir = Path(self.test_dir)

        data = {
        "1": {
            "user_id": 0,
            "username": "TestUsername"
            }
        }

        self.data_handler.write_user_data_json(data)

        read_data = self.data_handler.read_user_data_json()

        self.assertTrue((self.test_dir/"UserData.json").exists())
        self.assertDictEqual(data, read_data)

        # Cleanup file
        os.remove(self.test_dir/"UserData.json")
        os.rmdir(self.test_dir)

    def test_read_leaderboard_data(self):
        """Test user data file reading"""
        self.test_dir = "./guess/TestGameData"
        self.data_handler = data_handler.DataHandler(self.test_dir)
        self.test_dir = Path(self.test_dir)

        read_data = self.data_handler.read_leaderboard_data_json()

        self.assertTrue((self.test_dir/"LeaderboardData.json").exists())
        self.assertDictEqual({}, read_data)

        # Cleanup file
        os.remove(self.test_dir/"LeaderboardData.json")
        os.rmdir(self.test_dir)

    def test_get_user_id(self):
        """Test get user id"""
        self.test_dir = "./guess/TestGameData"
        self.data_handler = data_handler.DataHandler(self.test_dir)
        self.test_dir = Path(self.test_dir)

        data = {
        "5": {
            "user_id": 5,
            "username": "TestUsername"
            }
        }

        self.data_handler.write_user_data_json(data)
        self.assertEqual(self.data_handler.get_user_id("TestUsername"), 5)
        self.assertFalse(self.data_handler.get_user_id("UsernameNotExisting"))

        # Cleanup file
        os.remove(self.test_dir/"UserData.json")
        os.rmdir(self.test_dir)

    def test_add_or_update_user(self):
        """Test get user id"""
        self.test_dir = "./guess/TestGameData"
        self.data_handler = data_handler.DataHandler(self.test_dir)
        self.test_dir = Path(self.test_dir)

        test_data = {
        "0": {
            "user_id": 0,
            "username": "TestUsername0"
            },
        "1": {
            "user_id": 1,
            "username": "TestUsername1"
            },
        "2": {
            "user_id": 2,
            "username": "TestUsername2"
            }
        }

        exp = {
        "0": {
            "user_id": 0,
            "username": "TestUsername0"
            },
        "1": {
            "user_id": 1,
            "username": "ChangedName"
            },
        "2": {
            "user_id": 2,
            "username": "TestUsername2"
            }
        }

        exp1 = {
        "0": {
            "user_id": 0,
            "username": "TestUsername0"
            },
        "1": {
            "user_id": 1,
            "username": "TestUsername1"
            },
        "2": {
            "user_id": 2,
            "username": "TestUsername2"
            },
        "3": {
            "user_id": 3,
            "username": "TestUsername3"
            }
        }
        
        #Assert unable to take another user's username
        self.data_handler.write_user_data_json(test_data)
        self.assertFalse(self.data_handler.add_or_update_user("TestUsername1", 0))

        #Assert update username
        self.data_handler.write_user_data_json(test_data)
        self.data_handler.add_or_update_user("ChangedName", 1)
        self.assertDictEqual(self.data_handler.read_user_data_json(), exp)

        #Assert proper adding of new user
        self.data_handler.write_user_data_json(test_data)
        self.data_handler.add_or_update_user("TestUsername3")

        new_data = self.data_handler.read_user_data_json()
        self.assertDictEqual(new_data, exp1)

        # Cleanup file
        os.remove(self.test_dir/"UserData.json")
        os.rmdir(self.test_dir)

    def test_user_data_file_missing_or_empty(self):
        """Test get user id"""
        self.test_dir = "./guess/TestGameData"
        self.data_handler = data_handler.DataHandler(self.test_dir)
        self.test_dir = Path(self.test_dir)

        self.assertEqual(not(self.test_dir/"UserData.json").exists(), self.data_handler.is_user_data_file_missing_or_empty())

        # Cleanup file
        os.remove(self.test_dir/"UserData.json")
        os.rmdir(self.test_dir)
    def test_write_leaderboard_data(self):
        """Test get user id"""
        self.test_dir = "./guess/TestGameData"
        self.data_handler = data_handler.DataHandler(self.test_dir)
        self.test_dir = Path(self.test_dir)

        data_to_write = {
            "1":{
                "user_id" : 1,
                "username": "TestName"
            }
        }

        self.data_handler.write_leaderboard_data_json(data_to_write)

        self.assertDictEqual(self.data_handler.read_leaderboard_data_json(), data_to_write)

        # Cleanup file
        os.remove(self.test_dir/"LeaderboardData.json")
        os.rmdir(self.test_dir)


if __name__ == "__main__":
    unittest.main()
