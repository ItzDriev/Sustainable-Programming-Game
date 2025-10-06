#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module for handling UserData.

Handles user data.
"""

from guess.json_file_handler import JSONFileHandler


class UserDataHandler(JSONFileHandler):
    """Handles writing user data to JSON file."""

    def __init__(self, file_path, dir_path):
        """Initialize the object."""
        super().__init__(file_path, dir_path)

    def get_user_id(self, username):
        """Return user id based on username."""
        data = self.read()

        for user_id, user_info in data.items():
            if user_info.get("username") == username:
                return int(user_id)
        return False

    def add_user(self, username):
        """Add a new user if username is unique."""
        data = self.read()

        if any(info.get("username") == username for info in data.values()):
            return False
        user_id = len(data)

        data[str(user_id)] = {
            "user_id": int(user_id),
            "username": username
        }

        self.write(data)
        return True

    def update_username(self, user_id, new_username):
        """Update the username for an existing user."""
        data = self.read()
        if str(user_id) not in data:
            return False
        data[str(user_id)]["username"] = new_username
        self.write(data)
        return True
