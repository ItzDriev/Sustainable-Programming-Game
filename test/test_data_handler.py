#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""


import unittest
import os
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
        os.rmdir(self.test_dir)
        # Cleanup file
        # os.remove(self.test_dir/"LeaderboardData.json")
        # os.rmdir(self.test_dir)


if __name__ == "__main__":
    unittest.main()
