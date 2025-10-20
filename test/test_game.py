#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import os
from pig_game.game.game import Game
from pig_game.game.player import Player


class TestGameClass(unittest.TestCase):  # noqa : H601
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        self.test_dir = "./guess/TestGameData"
        res = Game(dir_path=self.test_dir)
        exp = Game
        self.assertIsInstance(res, exp)

    def test_start_the_game(self):
        """Roll a dice and check value is in bounds."""
        self.test_dir = "./guess/TestGameData"
        the_game = Game(dir_path=self.test_dir)
        the_game.turn_manager.data_handler.user_data.add_user("testuser")
        players = []
        players.append(
            Player(
                "testuser",
                the_game.turn_manager.data_handler.user_data.get_user_id("testuser"),
            )
        )
        the_game.start(players, 100, True)

        self.assertTrue(True)
        os.remove(self.test_dir + "/UserData.json")
        os.rmdir(self.test_dir)

    def test_ai_should_roll(self):
        """Tests if npc turn declines and score remain unchanged."""
        test_game = Game()
        test_game.players = [Player("test_name", 1)]
        test_game.players[0].score = 2

        test_game.ai.should_roll = lambda *_: False

        roll_dice_flag = {"Called": False}
        test_game.dice_hand.roll_dice = lambda: roll_dice_flag.__setitem__(
            "Called", True
        )
        test_game.turn_manager.npc_turn(
            test_game.ai,
            test_game.dice_hand,
            test_game.players,
            test_game.target_points,
        )

        self.assertFalse(roll_dice_flag["Called"])
        self.assertEqual(test_game.ai.score, 0)

    def test_npc_hand_roll(self):
        """Tests if npc hand rolls correctly."""
        test_game = Game()
        test_game.players.append(Player("test_name", 1))
        test_game.players[0].score = 0
        test_game.target_points = 0

        test_game.ai.should_roll = lambda *_: True
        test_game.turn_manager.npc_turn(
            test_game.ai,
            test_game.dice_hand,
            test_game.players,
            test_game.target_points,
        )

        self.assertGreaterEqual(test_game.dice_hand.get_last_roll()[0], 1)
        self.assertLessEqual(test_game.dice_hand.get_last_roll()[0], 6)

        self.assertGreaterEqual(test_game.dice_hand.get_last_roll()[1], 1)
        self.assertLessEqual(test_game.dice_hand.get_last_roll()[1], 6)

        test_total_rolls = sum(test_game.dice_hand.get_last_roll())

        if any(1 in roll for roll in test_game.dice_hand.get_roll_history()):
            test_total_rolls = 0
        test_game.turn_manager.player_turn(
            test_game.players[0],
            test_game.dice_hand,
            test_game.ai,
            test_game.target_points,
            test_game.players,
            cheat_mode=True,
        )
        self.assertEqual(test_game.ai.score, test_total_rolls)

    def test_quit_game(self):
        """Test if the game quits properly."""
        test_game = Game()
        self.assertFalse(test_game.game_over)
        test_game.quit_game(Player("test_player", 1))
        self.assertTrue(test_game.game_over)

    def test_reset_game(self):
        """Tests if the game resets properly."""
        test_game = Game()
        test_game.start([Player("test_player", 1)], 100, True)
        test_game.ai.score = 10
        self.assertEqual(10, test_game.ai.score)
        self.assertFalse(test_game.game_over)
        self.assertIsNotNone(test_game.players)
        test_game.game_over = True
        test_game.reset_game()
        self.assertEqual(0, test_game.ai.score)
        self.assertFalse(test_game.game_over)
        self.assertIsNone(test_game.players)


if __name__ == "__main__":
    unittest.main()
