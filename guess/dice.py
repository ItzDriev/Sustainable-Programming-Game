#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module defines a Dice class to simulate rolling dice."""

import random

class Dice:
    """Represents a dice object that can be rolled."""

    def __init__(self, sides=6):
        """Initialize the dice object."""
        self.__sides = sides
        self.__last_roll = None

    def roll_dice(self):
        """Roll the dice and generate a random integer
        between 1 and the number of sides."""
        self.__last_roll = random.randint(1, self.__sides)
        return self.__last_roll #Testing purpose

    def get_last_roll(self):
        """Return the value of the last roll."""
        return self.__last_roll
