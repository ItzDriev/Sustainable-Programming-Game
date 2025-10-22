#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import shutil
import unittest
from pig_game.game.game import Game
from pig_game.game.player import Player


class TestGameClass(unittest.TestCase):  # noqa : H601
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        self.test_dir = "./pig_game/TestGameData"
        res = Game(dir_path=self.test_dir)
        exp = Game
        self.assertIsInstance(res, exp)

    def test_start_the_game_case_1(self):
        """Test."""
        self.test_dir = "./pig_game/TestGameData"
        the_game = Game(dir_path=self.test_dir)
        the_game.turn_manager.data_handler.user_data.add_user("testuser")
        uid = the_game.turn_manager.data_handler.user_data.get_user_id("testuser")
        the_game.turn_manager.data_handler.leaderboard_data.add_new_player(uid)
        players = [Player("testuser", uid)]

        self.assertFalse(the_game.game_over)
        the_game.start(players, 0, True, 1, 1)
        self.assertTrue(the_game.game_over)
        self.assertTrue(the_game.game_over)
        the_game.start(players, 30, True, 1, 1)
        self.assertTrue(the_game.game_over)

        shutil.rmtree(self.test_dir)

    def test_start_the_game_case_2(self):
        """Test."""
        self.test_dir = "./pig_game/TestGameData"
        the_game = Game(dir_path=self.test_dir)
        the_game.turn_manager.data_handler.user_data.add_user("testuser")
        uid = the_game.turn_manager.data_handler.user_data.get_user_id("testuser")
        the_game.turn_manager.data_handler.leaderboard_data.add_new_player(uid)
        players = [Player("testuser", uid)]

        self.assertFalse(the_game.game_over)
        the_game.start(players, 0, True, 2, 2)
        self.assertTrue(the_game.game_over)
        the_game.game_over = False
        the_game.start(players, 13, True, 2, 2)
        self.assertTrue(the_game.game_over)

        shutil.rmtree(self.test_dir)

    def test_start_the_game_two_player(self):
        """Roll a dice and check value is in bounds."""
        self.test_dir = "./pig_game/TestGameData"
        the_game = Game(dir_path=self.test_dir)
        the_game.turn_manager.data_handler.user_data.add_user("testuser")
        uid = the_game.turn_manager.data_handler.user_data.get_user_id("testuser")
        the_game.turn_manager.data_handler.leaderboard_data.add_new_player(uid)
        the_game.turn_manager.data_handler.user_data.add_user("testuser2")
        uid2 = the_game.turn_manager.data_handler.user_data.get_user_id("testuser2")
        the_game.turn_manager.data_handler.leaderboard_data.add_new_player(uid2)
        players = []
        players.append(
            Player(
                "testuser",
                uid,
            )
        )
        players.append(
            Player(
                "testuser2",
                uid2,
            )
        )
        self.assertFalse(the_game.game_over)
        the_game.start(players, 15, True)

        self.assertTrue(the_game.game_over)
        shutil.rmtree(self.test_dir)

    def test_quit_game(self):
        """Test if the game quits properly."""
        self.test_dir = "./pig_game/TestGameData"
        test_game = Game(dir_path=self.test_dir)
        self.assertFalse(test_game.game_over)
        test_game.quit_game(Player("test_player", 1))
        self.assertTrue(test_game.game_over)
        shutil.rmtree(self.test_dir)

    def test_reset_game(self):
        """Tests if the game resets properly."""
        self.test_dir = "./pig_game/TestGameData"
        test_game = Game(dir_path=self.test_dir)
        test_game.turn_manager.data_handler.user_data.add_user("testuser")
        uid = test_game.turn_manager.data_handler.user_data.get_user_id("testuser")
        test_game.turn_manager.data_handler.leaderboard_data.add_new_player(uid)
        players = []
        players.append(
            Player(
                "testuser",
                uid,
            )
        )
        test_game.start(players, 0, True)
        test_game.computer.score = 10
        self.assertEqual(10, test_game.computer.score)
        self.assertIsNotNone(test_game.players)
        test_game.game_over = True
        test_game.reset_game()
        self.assertEqual(0, test_game.computer.score)
        self.assertFalse(test_game.game_over)
        self.assertIsNone(test_game.players)
        shutil.rmtree(self.test_dir)


if __name__ == "__main__":
    unittest.main()
