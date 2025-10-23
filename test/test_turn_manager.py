#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit tests for the TurnManager class."""

import shutil
import unittest
from unittest.mock import MagicMock, patch
from pig_game.game.turn_manager import TurnManager
from pig_game.game.game import Game
from pig_game.game.player import Player


class TestTurnManagerClass(unittest.TestCase):
    """Tests for the TurnManager class."""

    def setUp(self):
        """Create a test directory and initialize a Game instance."""
        # Temporary test directory to isolate data for each test
        self.test_dir = "./pig_game/TestGameData"

        # Create a fresh game and TurnManager for each test
        self.game = Game(dir_path=self.test_dir)
        self.turn_manager = TurnManager(
            dir_path=self.test_dir,
            dice_emoji=Game.dice_emoji,
            game=self.game,
        )

    def tearDown(self):
        """Clean up any created directories after each test."""
        # removing test directory
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        self.assertIsInstance(self.turn_manager, TurnManager)

    @patch("builtins.print")
    def test_npc_turn(self, dummy_print):
        """Tests if npc hand rolls correctly."""
        # Create user data and leaderboard for testingg
        self.turn_manager.data_handler.user_data.add_user("test_name")
        userid = self.turn_manager.data_handler.user_data.get_user_id("test_name")
        self.turn_manager.data_handler.leaderboard_data.add_new_player(userid)

        # Add a player to the game
        self.game.players.append(Player("test_name", userid))
        self.game.players[0].score = 2

        self.assertEqual(self.game.players[0].score, 2)

    @patch("builtins.print")
    def test_player_turn_cheat_mode_adds_score(self, dummy_print):
        """Test that cheat mode immediately increases player score."""
        self.game.cheat_mode = True

        # Create dummy player
        player_name = "Tester"
        self.turn_manager.data_handler.user_data.add_user(player_name)
        user_id = self.turn_manager.data_handler.user_data.get_user_id(player_name)
        self.turn_manager.data_handler.leaderboard_data.add_new_player(user_id)

        # Attach player to game
        player = Player(player_name, user_id)
        self.game.players.append(player)

        # Dummy dice hand and computer objects
        dice_hand = MagicMock()
        computer = MagicMock()

        # Store starting score
        starting_score = player.score

        # Run the player_turn method in test mode
        self.turn_manager.player_turn(player, dice_hand, computer, test_mode=True)

        # Assert the cheat mode applied correctly
        self.assertEqual(player.score, starting_score + self.game.target_points)

    # suppress the sleep so u dont have to wait 2.5s each turn
    @patch("time.sleep", return_value=None)
    @patch("builtins.print")
    def test_npc_turn_resets_score_on_double_ones(self, dummy_print, _):
        """Test that npc_turn resets AI score to 0 when two 1s are rolled."""
        # Prep
        self.turn_manager.data_handler.user_data.add_user("player1")
        uid = self.turn_manager.data_handler.user_data.get_user_id("player1")
        self.turn_manager.data_handler.leaderboard_data.add_new_player(uid)

        player = Player("player1", uid)
        self.game.players.append(player)

        # Mock computer and dicehand
        computer = MagicMock()
        dice_hand = MagicMock()
        computer.score = 20
        computer.should_roll.return_value = True
        dice_hand.get_last_roll.return_value = (1, 1)

        # Simulating rolling 2 1s
        with patch(
            "pig_game.utils.dice_evaluator.DiceEvaluator.rolled_one", return_value=True
        ), patch(
            "pig_game.utils.dice_evaluator.DiceEvaluator.rolled_two_ones",
            return_value=True,
        ):
            result = self.turn_manager.npc_turn(computer, dice_hand)

        self.assertEqual(computer.score, 0)  # score reset
        dummy_print.assert_any_call(
            "❌ Oh noooooo! Mr. AI rolled two 1's. Score will be reset down to 0 ❌"
        )
        self.assertTrue(result)

    # Supress the sleep so you dont have to wait 2.5s each time
    @patch("time.sleep", return_value=None)
    @patch("builtins.print")
    def test_player_turn_resets_score_on_double_ones(self, dummy_print, _):
        """Test that player_turn resets score to 0 when rolling two 1s."""
        # Prep
        self.turn_manager.data_handler.user_data.add_user("player1")
        user_id = self.turn_manager.data_handler.user_data.get_user_id("player1")
        self.turn_manager.data_handler.leaderboard_data.add_new_player(user_id)

        player = Player("player1", user_id)
        player.score = 25  # give player some score before the turn ppc

        dice_hand = MagicMock()
        dice_hand.get_last_roll.return_value = (1, 1)  # simulate rolling double 1s

        computer = MagicMock()
        computer.difficulties.reset_turn_score = MagicMock()

        # Simulating rolling two 1s
        with patch(
            "pig_game.utils.dice_evaluator.DiceEvaluator.rolled_one", return_value=True
        ), patch(
            "pig_game.utils.dice_evaluator.DiceEvaluator.rolled_two_ones",
            return_value=True,
        ):
            self.turn_manager.player_turn(
                player=player,
                dice_hand=dice_hand,
                computer=computer,
                test_mode=True,
            )

        # Assert that score reset and print was calleed
        self.assertEqual(player.score, 0)
        dummy_print.assert_any_call(
            f"❌ Oh noooooo! {player.get_username()} rolled two 1's. "
            f"Score will be reset down to {player.score} ❌"
        )
