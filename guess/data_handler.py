#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DataHandler module.

Provides the DataHandler class to manage reading, writing,
and updating user and leaderboard data in JSON format.
"""

from pathlib import Path
from guess.user_data_handler import UserDataHandler
from guess.leaderboard_data_handler import LeaderboardDataHandler

# pylint: disable=too-few-public-methods,line-too-long
# flake8: noqa

class DataHandler:
    """Handles game's data."""

    def __init__(self, dir_path="./guess/GameData"):
        """Initialize the object."""
        self.__dir_path = Path(dir_path)
        self.user_data = UserDataHandler(self.__dir_path/"UserData.json", self.__dir_path)
        self.leaderboard_data = LeaderboardDataHandler(self.__dir_path/"LeaderboardData.json", self.__dir_path)
