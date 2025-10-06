#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module for handling LeaderboardData.

Handles LeaderboardData.
"""

from guess.json_file_handler import JSONFileHandler


class LeaderboardDataHandler(JSONFileHandler):
    """Handle writing leaderboard data to JSON file."""

    def __init__(self, file_path, dir_path):
        """Handle leaderboard data to JSON file."""
        super().__init__(file_path, dir_path)
