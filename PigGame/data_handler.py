#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DataHandler module.

Provides the DataHandler class to manage reading, writing,
and updating user and leaderboard data in JSON format.
"""

from pathlib import Path
from PigGame.user_data_handler import UserDataHandler
from PigGame.leaderboard_data_handler import LeaderboardDataHandler

# pylint: disable=too-few-public-methods,line-too-long
# flake8: noqa


class DataHandler:
    """Handles game's data."""

    def __init__(self, dir_path="./PigGame/GameData"):
        """Initialize the object.

        :param dir_path: Directory path, eg. './PigGame/GameData'.
        :type dir_path: :py:obj:`str`
        """
        self.__dir_path = Path(dir_path)
        self.user_data = UserDataHandler(
            self.__dir_path / "UserData.json", self.__dir_path
        )
        self.leaderboard_data = LeaderboardDataHandler(
            self.__dir_path / "LeaderboardData.json", self.__dir_path
        )

    def print_leaderboard(self):
        """Print leaderboard."""
        print(f"{'Name':<15}{'Wins':<15}{'PPT':<15}")
        leaderboard = self.leaderboard_data.read()
        for user_id, score in leaderboard.items():
            print(f"{self.user_data.get_username(int(user_id)):<15}")
            print(f"{self.user_data.get_username(int(user_id))}: {score}")
