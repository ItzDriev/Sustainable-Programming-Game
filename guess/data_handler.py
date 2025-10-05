#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DataHandler module.

Provides the DataHandler class to manage reading, writing,
and updating user and leaderboard data in JSON format.
"""

import json
from pathlib import Path


class DataHandler:
    """Handles writing data to JSON file."""

    def __init__(self, dir_path="./guess/GameData"):
        """Initialize the data writer."""
        self.__dir_path = Path(dir_path)
        self.__dir_path.mkdir(parents=True, exist_ok=True)

        self.__user_data_path = self.__dir_path/"UserData.json"
        self.__leadboard_data_path = self.__dir_path/"LeaderboardData.json"

    def is_user_data_file_missing_or_empty(self):
        """Check for missing file or invalid content."""
        missing_file = not self.__user_data_path.exists()
        if not missing_file:
            empty_file = self.__user_data_path.stat().st_size == 0
        else:
            empty_file = True
        if missing_file or empty_file:
            self.write_user_data_json({})
            return True
        return False

    def write_user_data_json(self, data):
        """Write user data to file."""
        with open(self.__user_data_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def read_user_data_json(self):
        """Read user data file and returns."""
        self.is_user_data_file_missing_or_empty()
        with open(self.__user_data_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_user_id(self, username):
        """Return user id based on username."""
        data = self.read_user_data_json()

        for user_id, user_info in data.items():
            if user_info.get("username") == username:
                return int(user_id)
        return False

    def add_or_update_user(self, username, user_id=None):
        """Add a new user or updates their name."""
        data = self.read_user_data_json()

        user_id = len(data) if user_id is None else user_id

        # Ensure unique username
        for _, user_info in data.items():
            if user_info.get("username") == username:
                return False

        data[str(user_id)] = {
            "user_id": int(user_id),
            "username": username
        }

        self.write_user_data_json(data)
        return True

    def is_leaderboard_data_file_missing_or_empty(self):
        """Check for missing file or invalid content."""
        missing_file = not self.__leadboard_data_path.exists()
        if not missing_file:
            empty_file = self.__leadboard_data_path.stat().st_size == 0
        else:
            empty_file = True
        if missing_file or empty_file:
            self.write_leaderboard_data_json({})
            return True
        return False

    def write_leaderboard_data_json(self, data):
        """Write leadboard data to file."""
        with open(self.__leadboard_data_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def read_leaderboard_data_json(self):
        """Read leaderboard data from file."""
        self.is_leaderboard_data_file_missing_or_empty()
        with open(self.__leadboard_data_path, "r", encoding="utf-8") as f:
            return json.load(f)
