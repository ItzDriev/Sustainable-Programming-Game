#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""


from pathlib import Path
import unittest
import os
from guess.data_handler import DataHandler


class TestDataHandlerClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        self.test_dir = "./guess/TestGameData"
        res = DataHandler(self.test_dir)
        exp = DataHandler
        self.assertIsInstance(res, exp)

        # Cleanup directory
        os.rmdir(self.test_dir)
        # Cleanup file
        #os.remove(self.test_dir/"LeaderboardData.json")
        #os.rmdir(self.test_dir)



if __name__ == "__main__":
    unittest.main()
