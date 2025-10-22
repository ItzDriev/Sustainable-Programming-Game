#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module defines a hand in order to engage with a dice."""

from pig_game.game.dice import Dice


class DiceHand:
    """Represents a dice hand."""

    def __init__(self):
        """Initialize the dice hand object."""
        self.dice = Dice()  # Purpose of this line, pyreverse connection to class.
        self.dice = [Dice(), Dice()]
        self.roll_history = []
        self.last_roll = []

    def roll_dice(self):
        """Roll the dice in hand.

        :return: The value of the dice roll.
        :rtype: :py:obj:`int`
        """
        self.last_roll.clear()

        for die in self.dice:
            die.roll_dice()
            self.last_roll.append(die.get_last_roll())

        self.roll_history.append(self.last_roll)
        return self.last_roll  # Testing purpose

    def get_last_roll(self):
        """Return the value of the last die throw.

        :return: The value of the last dice roll.
        :rtype: :py:obj:`int`
        """
        return self.last_roll

    def get_roll_history(self):
        """Return all rolls from current session.

        :return: All previous rolls from the dice.
        :rtype: :py:obj:`list` [:py:obj:`int`]
        """
        return self.roll_history
