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

    def print_leaderboard(self, arg):
        """Print leaderboard."""
        leaderboard = self.leaderboard_data.read()
        sorted_data = dict(sorted(leaderboard.items(), key=lambda item: item[1]["ppt"], reverse=True))

        top_leader = 0
        print("----------------------------------------------------------------------------------------")
        print(f"|{'Top ' + str(arg if arg != "" else 10) + ':':<15}{'Name:':<15}{'Games played:':<20}{'Winrate:':<15}{'Avr score per turn:':<21}|")
        print("----------------------------------------------------------------------------------------")

        for user_id, stats in sorted_data.items():
            if stats['wins'] != 0:
                winrate = int(((stats['wins'])/(stats['games_played']))*100)
            else:
                winrate = 0
            top_leader+=1

            print(f"|{top_leader:<15}{str(self.user_data.get_username(int(user_id))):<15}{stats['games_played']:<20}{f'{winrate}%':<15}{stats['ppt']:<21.2f}|")
            print("----------------------------------------------------------------------------------------")
            if arg == "":
                if top_leader == 10:
                    break
            elif top_leader >= int(arg):
                break
