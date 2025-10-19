"""Test Module for Game UI."""

import unittest
from unittest.mock import patch
from pig_game.utils.game_ui import GameUI


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


if __name__ == "__main__":
    unittest.main()
