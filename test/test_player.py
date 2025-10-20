#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
from pig_game.game.player import Player


class TestPlayerClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = Player("Test", 4)
        exp = Player
        self.assertIsInstance(res, exp)

    def test_set_username(self):
        """Update username and check."""
        the_player = Player("Test", 0)
        new_username = "NewUsername"
        the_player.set_username(new_username)

        res = the_player.get_username()
        exp = res == new_username
        self.assertTrue(exp)

    def test_get_username(self):
        """Test get username."""
        the_player = Player("Test", 0)

        res = the_player.get_username()
        exp = res == "Test"
        self.assertTrue(exp)

    def test_get_user_id(self):
        """Create player and check user_id."""
        the_player = Player("Test", 55)

        res = the_player.get_user_id()
        exp = res == 55
        self.assertTrue(exp)


if __name__ == "__main__":
    unittest.main()
