#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module for handling LeaderboardData.

Handles LeaderboardData.
"""

from PigGame.json_file_handler import JSONFileHandler
from PigGame.player import Player


class LeaderboardDataHandler(JSONFileHandler):  # noqa: H601
    """Handle writing leaderboard data to JSON file."""

    def __init__(self, file_path, dir_path):
        """Handle leaderboard data to JSON file."""
        super().__init__(file_path, dir_path)

    def get_highscore(self, user_id):
        """Return highscore of player based on user_id."""
        data = self.read()
        return data[str(user_id)]

    def update_ppt_and_turns(self, player: Player, value):
        """Update points per turn and total turns for players."""
        uid = str(player.get_user_id())

        data = self.read()
        data[uid]["total_turns"] += 1
        data[uid]["ppt"] = (data[uid]["ppt"]
                            * (data[uid]["total_turns"]-1)
                            + value)/data[uid]["total_turns"]
        self.write(data)

    def update_games_played(self, player_won, player: Player):
        """Update wins and games played for players."""
        data = self.read()
        if player_won:
            data[str(player.get_user_id())]["wins"] += 1
            data[str(player.get_user_id())]["games_played"] += 1
        else:
            data[str(player.get_user_id())]["games_played"] += 1
        self.write(data)

    def add_new_player(self, user_id):
        """Create leaderboard data for user."""
        data = dict(self.read())
        if any(keys == str(user_id) for keys in data.keys()):
            return
        data[str(user_id)] = {"wins": 0, "games_played": 0, "ppt": 0, "total_turns": 0}
        self.write(data)
