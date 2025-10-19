"""GameUI module."""


class GameUI():  # noqa: H601
    """Handles ui interaction during a game."""

    def __init__(self, emojis):
        """Inititializes the GameUI object."""
        self.emojis = emojis

    def show_roll(self, player_name, dice_values):
        """Print the roll made to the terminal.

        :param player_name: Username of the player.
        :type player_name: :py:obj:`str`
        :param dice_values: List of dice values.
        :type dice_values: :py:obj:`list` [ :py:obj:`int` ]
        """
        print(f"{player_name} rolled {dice_values[0]} and {dice_values[1]} "
              f"{self.emojis[dice_values[0]-1]} {self.emojis[dice_values[1]-1]}")

    def prompt_next_action(self, username, score):
        """Promt player to choose next action.

        :param username: Username of the player.
        :type username: :py:obj:`str`
        :param score: Score of player.
        :type score: :py:obj:`int`
        """
        return input(f"{username}'s " +
                     f"Total score: {score}" +
                     "\n\nContinue? 'y'/'n' or 'quit' to quit\n")

    def clear_terminal(self):
        """Clear the terminal."""
        print("\n" * 40)
