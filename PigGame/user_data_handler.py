#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module for handling UserData.

Handles user data.
"""

from PigGame.json_file_handler import JSONFileHandler


class UserDataHandler(JSONFileHandler):
    """Handles writing user data to JSON file."""

    def __init__(self, file_path, dir_path):
        """Initialize the object.

        :param file_path: File name, eg. '/file.json'.
        :type file_path: :py:obj:`str`
        :param dir_path: Directory path, eg. './PigGame/GameData'.
        :type dir_path: :py:obj:`str`
        """
        super().__init__(file_path, dir_path)

    def get_user_id(self, username):
        """Return user id based on username.

        :param username: Username of a user/player.
        :type username: :py:obj:`str`
        :return: The id of a user based on username.
        :rtype: :py:obj:`int` | :py:obj:`None`
        """
        data = self.read()

        for user_id, user_info in data.items():
            if user_info.get("username") == username:
                return int(user_id)
        return None

    def add_user(self, username):
        """Add a new user if username is unique.

        :param username: Username of a user/player.
        :type username: :py:obj:`str`
        :return: If the user was added succesfully.
        :rtype: :py:obj:`bool`
        """
        data = self.read()

        if any(info.get("username") == username for info in data.values()):
            return False
        user_id = len(data)

        data[str(user_id)] = {"user_id": int(user_id), "username": username}

        self.write(data)
        return True

    def update_username(self, current_username, new_username):
        """Update the username for an existing user.

        :param current_username: The username of the user/player.
        :type current_username: :py:obj:`str`
        :param new_username: New username.
        :type new_username: :py:obj:`str`
        :return: If the username was updated or not.
        :rtype: :py:obj:`bool`
        """
        data = self.read()
        if any(info.get("username") == new_username for info in data.values()):
            return False
        if str(self.get_user_id(current_username)) not in data:
            return False
        data[str(self.get_user_id(current_username))]["username"] = new_username
        self.write(data)
        return True

    def get_username(self, user_id):
        """Return username based on user_id.

        :param user_id: Id of player.
        :type user_id: :py:obj:`int`
        :return: The username of a user/player.
        :rtype: :py:obj:`str` | :py:obj:`None`
        """
        data = self.read()
        for info in data.values():
            if info.get("user_id") == user_id:
                return info.get("username")
        return None
