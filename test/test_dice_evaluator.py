#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
from PigGame.utils.dice_evaluator import DiceEvaluator


class TestDiceEvaluatorClass(unittest.TestCase):
    """Test the class."""

    def test_rolled_one(self):
        """Tests if the method evaluates 1's correct in all cases."""
        self.assertTrue(DiceEvaluator.rolled_one(1, 1))
        self.assertTrue(DiceEvaluator.rolled_one(2, 1))
        self.assertTrue(DiceEvaluator.rolled_one(1, 2))
        self.assertFalse(DiceEvaluator.rolled_one(2, 2))

    def test_rolled_two_ones(self):
        """Tests if the method evaluates 1's correct in all cases."""
        self.assertTrue(DiceEvaluator.rolled_two_ones(1, 1))
        self.assertFalse(DiceEvaluator.rolled_two_ones(2, 1))
        self.assertFalse(DiceEvaluator.rolled_two_ones(1, 2))
        self.assertFalse(DiceEvaluator.rolled_two_ones(2, 2))


if __name__ == "__main__":
    unittest.main()
