#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest

from guess import dice_hand

class TestDiceHandClass(unittest.TestCase):
    """Test class object for dice_hand class."""

    def test_init_dice_hand(self):
        """Test object instantiation."""
        res = dice_hand.DiceHand()
        exp = dice_hand.DiceHand
        self.assertIsInstance(res, exp)

    def test_roll_dice(self):
        """Tests if the dice generates a integer between 1 and 6."""
        test_hand = dice_hand.DiceHand()

        value = test_hand.roll_dice()

        self.assertIsInstance(value[0], int)
        self.assertIsInstance(value[1], int)

        self.assertGreaterEqual(value[0], 1)
        self.assertLessEqual(value[0], 6)
        self.assertGreaterEqual(value[1], 1)
        self.assertLessEqual(value[1], 6)

    def test_get_last_value(self):
        """
        Tests if the get_last_value method return the expected value.
        from roll_dice method.
        """

        test_hand = dice_hand.DiceHand()

        test_hand.roll_dice()
        value1 = test_hand.dice[0].get_last_roll()
        value2 = test_hand.dice[1].get_last_roll()

        self.assertIsInstance(value1, int)
        self.assertIsInstance(value2, int)

        self.assertGreaterEqual(value1, 1)
        self.assertLessEqual(value1, 6)
        self.assertGreaterEqual(value2, 1)
        self.assertLessEqual(value2, 6)

    def test_get_roll_history(self):
        """Test if the returned roll_history matches the actual dice roll ristory."""
        test_hand = dice_hand.DiceHand()
        exp = []
        res = test_hand.get_roll_history()
        for i in range(1, 11):
            exp.append(test_hand.roll_dice())
        self.assertEqual(exp, res)


if __name__ == "__main__":
    unittest.main()