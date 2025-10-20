#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module for the Player object representing a player in the game."""


class Player:  # noqa : H601
    """Represent a player in the game."""

    def __init__(self, username, user_id):
        """Initialize the player object.

        :param username: Name of the player.
        :type username: :py:obj:`str`
        :param user_id: Id of player.
        :type user_id: :py:obj:`int`
        """
        self.score = 0
        self.__user_id = user_id
        self.__username = username

    def set_username(self, new_username):
        """Set the player's username.

        :param new_username: New username.
        :type new_username: :py:obj:`str`
        """
        self.__username = new_username

    def get_username(self):
        """Return the player's username.

        :return: The username of the player.
        :rtype: :py:obj:`str`
        """
        return self.__username

    def get_user_id(self):
        """Return the player's user ID.

        :return: The id of the player.
        :rtype: :py:obj:`int`
        """
        return self.__user_id
