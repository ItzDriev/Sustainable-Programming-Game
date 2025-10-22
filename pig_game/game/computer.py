#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module for ai rolling logic."""
from pig_game.game.computer_difficulties import ComputerDifficulties


class Computer:  # pylint: disable=too-few-public-methods
    """Handles how the AI thinks."""

    difficulty = 0

    def __init__(self):
        """Declare variables."""
        self.difficulties = ComputerDifficulties(self)
        self.score: int = 0

    def should_roll(self, player_score):
        """Choose difficulty strategy and decide whether to roll.

        :param player_score: The human player's total score.
        :type player_score: :py:obj:`int`
        :return: True if should roll, False if should not continue.
        :rtype: :py:obj:`bool` | :py:obj:`None`
        :raises ValueError: If the difficulty variable is out of range or
                            incorrect data type.
        """
        match Computer.difficulty:
            case 1:
                return self.difficulties.easy_mode(player_score, self.score)
            case 2:
                return self.difficulties.medium_mode(player_score, self.score)
            case 3:
                return self.difficulties.hard_mode(player_score, self.score)
            case 4:
                return self.difficulties.extreme_mode(player_score, self.score)
            case _:
                raise ValueError("Difficulty is out of range!")
