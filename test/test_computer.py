# test/test_computer_should_roll.py
"""Module for difficulty testing."""


import shutil
import unittest
from pig_game.game.computer import Computer


class TestComputerClass(unittest.TestCase):
    """Tests for player choice of difficulty."""

    def test_match_dispatch(self):
        """Check if all cases works."""
        c = Computer()
        c.score = 10
        original = Computer.difficulty
        try:
            cases = {
                1: ("easy_mode", "easy"),
                2: ("medium_mode", "medium"),
                3: ("hard_mode", "hard"),
                4: ("extreme_mode", "extreme"),
            }
            for diff, (method, label) in cases.items():
                Computer.difficulty = diff
                called = {}
                setattr(
                    c.difficulties,
                    method,
                    lambda ps, cs, lab=label, called=called: called.update(
                        args=(ps, cs)
                    )
                    or lab,
                )
                res = c.should_roll(player_score=7)
                self.assertEqual(res, label)
                self.assertEqual(called["args"], (7, 10))

            Computer.difficulty = 0
            self.assertIsNone(c.should_roll(player_score=7))
        finally:
            Computer.difficulty = original

    def test_computer_should_roll(self, player_score=2):
        """Tests if npc turn declines and score remain unchanged."""
        self.test_dir = "./pig_game/TestGameData"
        computer = Computer()
        computer.score = 1
        Computer.difficulty = 1

        computer.should_roll(player_score)


if __name__ == "__main__":
    unittest.main()
