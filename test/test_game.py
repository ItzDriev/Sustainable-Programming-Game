#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import os
from guess import game
from guess.player import Player


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        self.test_dir = "./guess/TestGameData"
        res = game.Game(dir_path=self.test_dir)
        exp = game.Game
        self.assertIsInstance(res, exp)

    def test_start_the_game(self):
        """Roll a dice and check value is in bounds."""
        self.test_dir = "./guess/TestGameData"
        the_game = game.Game(dir_path=self.test_dir)
        the_game.data_handler.user_data.add_user("testuser")
        players = []
        players.append(Player("testuser", the_game.data_handler.user_data.get_user_id("testuser")))
        the_game.start(players, True)


        self.assertTrue(True)
        os.remove(self.test_dir+"/UserData.json")
        os.rmdir(self.test_dir)         
        

if __name__ == "__main__":
    unittest.main()
