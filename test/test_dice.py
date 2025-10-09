#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest

from guess import dice

class TestDiceClass(unittest.TestCase):
    """A test class to test the dice class"""

    def test_init_dice(self):
        """Tests the instatiation of the dice class"""
        test_dice = dice.Dice()
        exp = dice.Dice
        self.assertIsInstance(test_dice,exp)

    def test_roll_dice(self):
        """Tests the roll dice method and if it generates an integer between 1-6"""
        test_dice = dice.Dice()
        value = test_dice.roll_dice()
        self.assertIsInstance(value,int)
        self.assertGreaterEqual(value, 1)
        self.assertLessEqual(value,6)

    def test_get_last_roll(self):
        """Test if the get method get_last_roll returns the actual roll value"""
        test_dice = dice.Dice()
        exp = test_dice.roll_dice()
        res = test_dice.get_last_roll()
        self.assertEqual(exp, res)

if __name__ == "__main__":
    unittest.main()  