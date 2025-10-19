#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DataHandler module.

Provides the DataHandler class to manage reading, writing,
and updating user and leaderboard data in JSON format.
"""

from pathlib import Path
from pig_game.utils.user_data_handler import UserDataHandler
from pig_game.utils.leaderboard_data_handler import LeaderboardDataHandler


class DataHandler:  # pylint: disable=too-few-public-methods
    """Handles game's data."""

    def __init__(self, dir_path="./pig_game/GameData"):
        """Initialize the object.

        :param dir_path: Directory path, eg. './pig_game/GameData'.
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
        leaderboard = dict(self.leaderboard_data.read())
        sorted_data = dict(
            sorted(leaderboard.items(), key=lambda item: item[1]["ppt"], reverse=True)
        )

        top_leader = 0
        print("-" * 88)
        print(
            f"|{'Top ' + str(arg if arg != "" else 10) + ':':<15}{'Name:':<15}{'Games played:':<20}{'Winrate:':<15}{'Avr score per turn:':<21}|"
        )  # noqa : H601  # pylint: disable=line-too-long
        print("-" * 88)

        for user_id, stats in sorted_data.items():
            if stats["wins"] != 0:
                winrate = int(((stats["wins"]) / (stats["games_played"])) * 100)
            else:
                winrate = 0
            top_leader += 1

            print(
                f"|{top_leader:<15}{str(self.user_data.get_username(int(user_id))):<15}{stats['games_played']:<20}{f'{winrate}%':<15}{stats['ppt']:<21.2f}|"
            )  # noqa : H601  # pylint: disable=line-too-long
            print("-" * 88)
            if arg == "":
                if top_leader == 10:
                    break
            elif top_leader >= int(arg):
                break
