#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module for the Player object representing a player in the game."""


class Player:
    """Represent a player in the game."""

    def __init__(self, username, user_id):
        """Initialize the player object."""
        self.score = 0
        self.__user_id = user_id
        self.__username = username

    def set_username(self, new_username):
        """Set the player's username."""
        self.__username = new_username

    def get_username(self):
        """Return the player's username."""
        return self.__username

    def get_user_id(self):
        """Return the player's user ID."""
        return self.__user_id
