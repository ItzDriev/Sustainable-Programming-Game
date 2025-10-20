#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module for ai rolling logic."""
from pig_game.game.computer_difficulties import ComputerDifficulties


class Computer:
    """Handles how the AI thinks."""

    difficulty = 0

    def __init__(self):
        """Declare variables."""
        self.difficulties = ComputerDifficulties(self)
        self.score: int = 0

    def should_roll(self, player_score):
        """Dice which difficulty function that should be played."""
        match Computer.difficulty:
            case 1:
                return self.difficulties.easy_mode(player_score, self.score)
            case 2:
                return self.difficulties.medium_mode(player_score, self.score)
            case 3:
                return self.difficulties.hard_mode(player_score, self.score)
            case 4:
                return self.difficulties.extreme_mode(player_score, self.score)
