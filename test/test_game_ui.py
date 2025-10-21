"""Test Module for Game UI."""

import unittest
from unittest.mock import patch
from pig_game.game.game_ui import GameUI


class TestGameUIClass(unittest.TestCase):  # noqa: H601
    """Game UI test class."""

    @patch("builtins.input", return_value="input")
    def test_prompt_next_action(self, mock_input):
        """Test."""
        game_ui = GameUI("")
        result = game_ui.prompt_next_action("User", 99)
        mock_input.assert_called_once_with(
            "User's Total score: 99\n\nContinue? 'y'/'n' or 'quit' to quit\n"
        )
        self.assertEqual(result, "input")

    @patch("builtins.print")
    def test_show_roll(self, mock_print):
        """Test."""
        game_ui = GameUI("\u2680\u2681\u2682\u2683\u2684\u2685")

        game_ui.show_roll("User", [1, 2])

        mock_print.assert_called_once_with("User rolled 1 and 2 \u2680 \u2681")

    @patch("builtins.print")
    def test_clear_terminal(self, mock_print):
        """Test."""
        game_ui = GameUI("\u2680\u2681\u2682\u2683\u2684\u2685")

        game_ui.clear_terminal()

        mock_print.assert_called_once_with("\n" * 40)


if __name__ == "__main__":
    unittest.main()
