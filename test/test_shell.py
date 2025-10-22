"""Unit tests for the Shell class in the Pig Game CLI."""

import unittest
from unittest.mock import patch, MagicMock
from pig_game.game.shell import Shell
from pig_game.game.game import Game


class TestShell(unittest.TestCase):
    """Unit tests for the Shell class command methods."""

    def setUp(self):
        """Create a Shell instance and replace its game object with a dummy."""
        self.shell = Shell()
        self.shell.game = MagicMock()

    # Patch replaces the input with a mock and side_effect are used as the paramters
    @patch("builtins.input", side_effect=["1", "50", "player1", "1"])
    def test_do_start_single_player(self, dummy_input):
        """Simulate a single-player game start with dummy inputs."""
        self.shell.game.turn_manager.data_handler.user_data = MagicMock()
        self.shell.game.turn_manager.data_handler.user_data.get_user_id.return_value = (
            123
        )
        self.shell.game.turn_manager.data_handler.leaderboard_data = MagicMock()
        self.shell.game.start = MagicMock()

        self.shell.do_start(None)

        self.shell.game.turn_manager.data_handler.user_data.add_user.assert_called_with(
            "player1"
        )
        self.shell.game.start.assert_called_once()

    @patch("builtins.input", side_effect=["1", "50", "player1", "1"])
    def test_do_start_userid_not_found(self, _dummy_input):
        """Test that LookupError is raised if get_user_id returns None."""
        # Setup user_data mock to return None for get_user_id
        self.shell.game.turn_manager.data_handler.user_data = MagicMock()
        self.shell.game.turn_manager.data_handler.user_data.get_user_id.return_value = (
            None
        )
        self.shell.game.turn_manager.data_handler.leaderboard_data = MagicMock()

        # Test if the LookupError is raised
        with self.assertRaises(LookupError) as context:
            self.shell.do_start(None)

        self.assertEqual(str(context.exception), "UserID Not Found!")

    @patch("builtins.print")
    def test_do_cheat(self, dummy_print):
        """Test that do_cheat activates cheat mode."""
        self.shell.do_cheat(None)
        self.assertTrue(Game.cheat_mode)
        dummy_print.assert_called_once()

    @patch("builtins.print")
    def test_do_namechange_valid(self, dummy_print):
        """Test that do_namechange calls the update method with args."""
        self.shell.game.turn_manager.data_handler.user_data.update_username = (
            MagicMock()
        )

        self.shell.do_namechange("old new")
        user_data = self.shell.game.turn_manager.data_handler.user_data
        user_data.update_username.assert_called_with("old", "new")

        dummy_print.assert_called()

    @patch("builtins.print")
    def test_do_namechange_invalid(self, dummy_print):
        """Test that do_namechange ignores invalid argument counts."""
        self.shell.game.turn_manager.data_handler.user_data.update_username = (
            MagicMock()
        )

        self.shell.do_namechange("onlyone")
        user_data = self.shell.game.turn_manager.data_handler.user_data
        user_data.update_username.assert_not_called()

    def test_exit_aliases(self):
        """Test that all exit commands return True."""
        for cmd in [
            self.shell.do_exit,
            self.shell.do_quit,
            self.shell.do_q,
            self.shell.do_EOF,
        ]:
            with self.subTest(cmd=cmd):
                with patch("builtins.print"):
                    self.assertTrue(cmd(None))
