#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest

from guess import dice_hand

class TestDiceHandClass(unittest.TestCase):
    """Test class object for dice_hand class """

    def test_init_dice_hand(self):
        """Test object instantiation"""
        res = dice_hand.DiceHand()
        exp = dice_hand.DiceHand
        self.assertIsInstance(res,exp)

    def test_roll_dice(self):
        """Tests if the dice generates a integer between 1 and 6."""
        test_hand = dice_hand.DiceHand()

        value = test_hand.roll_dice()

        self.assertIsInstance(value, int)

        self.assertGreaterEqual(value, 1)
        self.assertLessEqual(value, 6)

    def test_get_last_value(self):
        """Tests if the get_last_value method return the expected value 
        from roll_dice method"""
        test_hand = dice_hand.DiceHand()

        test_hand.roll_dice()
        value = test_hand.dice.get_last_roll()

        self.assertIsInstance(value, int)

        self.assertGreaterEqual(value, 1)
        self.assertLessEqual(value, 6)

    def test_get_roll_history(self):
        """Test if the returned roll_history matches the actual dice roll ristory"""
        test_hand = dice_hand.DiceHand()
        exp = []
        res = test_hand.get_roll_history()
        for i in range(1, 11):
            exp.append(test_hand.roll_dice())
        self.assertEqual(exp, res)

if __name__ == "__main__":
    unittest.main()        