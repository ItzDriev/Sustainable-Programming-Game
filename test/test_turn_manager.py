#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import shutil
import unittest
from unittest.mock import patch
from pig_game.game.turn_manager import TurnManager
from pig_game.game.game import Game
from pig_game.game.player import Player
from test.test_computer import TestComputerClass


class TestTurnManagerClass(unittest.TestCase):

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        self.test_dir = "./pig_game/TestGameData"
        game = Game(dir_path=self.test_dir)
        res = TurnManager(dir_path=self.test_dir, dice_emoji=Game.dice_emoji, game=game)
        exp = TurnManager
        self.assertIsInstance(res, exp)
        shutil.rmtree(self.test_dir)

    @patch("builtins.print")
    def test_npc_turn(self, mock_print):
        """Tests if npc hand rolls correctly."""
        self.test_dir = "./pig_game/TestGameData"
        game = Game(dir_path=self.test_dir)
        turn_manager = TurnManager(
            dir_path=self.test_dir, dice_emoji=Game.dice_emoji, game=game
        )
        turn_manager.data_handler.user_data.add_user("test_name")
        userid = turn_manager.data_handler.user_data.get_user_id("test_name")
        turn_manager.data_handler.leaderboard_data.add_new_player(userid)
        game.players.append(Player("test_name", userid))
        game.players[0].score = 2

        shutil.rmtree(self.test_dir)
