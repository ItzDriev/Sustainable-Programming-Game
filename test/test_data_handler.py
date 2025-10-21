#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""


import os
import shutil
import unittest
from pig_game.utils.data_handler import DataHandler


class TestDataHandlerClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        self.test_dir = "./pig_game/TestGameData"
        res = DataHandler(self.test_dir)
        exp = DataHandler
        self.assertIsInstance(res, exp)

        # Cleanup directory
        shutil.rmtree(self.test_dir)

    def test_leaderboard_empty_args(self):
        """Instantiate an object and check its properties."""
        self.test_dir = "./pig_game/TestGameData"
        data_handler = DataHandler(self.test_dir)

        for x in range(0, 11):
            data_handler.user_data.add_user(f"test_name{x}")
            userid = data_handler.user_data.get_user_id(f"test_name{x}")
            data_handler.leaderboard_data.add_new_player(userid)

        data_handler.print_leaderboard("", True)
        shutil.rmtree(self.test_dir)


if __name__ == "__main__":
    unittest.main()
