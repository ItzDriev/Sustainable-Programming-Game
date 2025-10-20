#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module for handling LeaderboardData.

Handles LeaderboardData.
"""

from pig_game.utils.json_file_handler import JSONFileHandler
from pig_game.game.player import Player


class LeaderboardDataHandler(JSONFileHandler):
    """Handle reading/writing leaderboard data to a JSON file."""

    def __init__(self, file_path, dir_path):
        """Initialize the handler.

        :param file_path: Filename of the leaderboard JSON.
        :type file_path: str
        :param dir_path: Directory containing the JSON file.
        :type dir_path: str
        """
        super().__init__(file_path, dir_path)

    def get_highscore(self, user_id):
        """Return the highscore for a user.

        :param user_id: ID of the user.
        :type user_id: int | str
        :return: The user's highscore.
        :rtype: int
        """
        data = self.read()
        return data[str(user_id)]

    def update_ppt_and_turns(self, player: Player, value):
        """Update points-per-turn (ppt) and total turns for a player.

        :param player: Player whose stats to update.
        :type player: Player
        :param value: Points gained this turn.
        :type value: int | float
        """
        uid = str(player.get_user_id())

        data = self.read()
        data[uid]["total_turns"] += 1
        data[uid]["ppt"] = (
            data[uid]["ppt"] * (data[uid]["total_turns"] - 1) + value
        ) / data[uid]["total_turns"]
        self.write(data)

    def update_games_played(self, player_won, player: Player):
        """Update wins and games played.

        :param player_won: Whether the player won the game.
        :type player_won: bool
        :param player: Player whose record to update.
        :type player: Player
        """
        data = self.read()
        if player_won:
            data[str(player.get_user_id())]["wins"] += 1
            data[str(player.get_user_id())]["games_played"] += 1
        else:
            data[str(player.get_user_id())]["games_played"] += 1
        self.write(data)

    def add_new_player(self, user_id):
        """Add a new user to the leaderboard if missing.

        :param user_id: ID of the user to add.
        :type user_id: int | str
        """
        data = dict(self.read())
        if any(keys == str(user_id) for keys in data.keys()):
            return
        data[str(user_id)] = {"wins": 0, "games_played": 0, "ppt": 0, "total_turns": 0}
        self.write(data)
