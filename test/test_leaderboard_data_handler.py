#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing for LeaderboardDataHandler."""

import unittest
from unittest.mock import MagicMock, patch
from copy import deepcopy

from PigGame.leaderboard_data_handler import LeaderboardDataHandler
from PigGame.json_file_handler import JSONFileHandler


class DummyPlayer:
    """Mimic as a player for the tests."""

    def __init__(self, user_id):
        """Mimic the init to simmulate a player."""
        self._id = user_id

    def get_user_id(self):
        """Mimic get_user to help tests."""
        return self._id


class TestLeaderBoardDataHandler(unittest.TestCase):
    """Holds all tests for leaderboardDataHandler."""

    def setUp(self):
        """Set up everything I need for the Unit-tests."""
        with patch.object(JSONFileHandler, "__init__", return_value=None):
            self.h = LeaderboardDataHandler(file_path="dummy.json", dir_path="/tmp")

        self.h.write = MagicMock()

        self.base = {
            '0': {'wins': 1, 'games_played': 1, 'ppt': 13.5, 'total_turns': 4},
            '2': {'wins': 3, 'games_played': 5, 'ppt': 8.2,  'total_turns': 19},
            '3': {'wins': 0, 'games_played': 2, 'ppt': 4.0,  'total_turns': 7},
        }

    # 22–23 get_highscore
    def test_get_highscore_returns_user_2(self):
        """Test for get_highscore."""
        self.h.read = MagicMock(return_value=deepcopy(self.base))
        result = self.h.get_highscore(2)
        self.assertEqual(result, self.base['2'])

    # 27–30 update_player_ppt_and_total_turns_total
    def test_update_player_ppt_and_total_turns_total_updates_average_and_turns(self):
        """Test for update player ppt and total turns."""
        data = deepcopy(self.base)
        self.h.read = MagicMock(return_value=data)

        player = DummyPlayer(user_id=2)
        value = 10.0

        prev_turns = data['2']['total_turns']
        prev_ppt = data['2']['ppt']
        expected_turns = prev_turns + 1
        expected_ppt = (prev_ppt * prev_turns + value) / expected_turns

        self.h.update_player_ppt_and_total_turns_total(player, value)

        self.h.write.assert_called_once()
        written = self.h.write.call_args.args[0]
        self.assertEqual(written['2']['total_turns'], expected_turns)
        self.assertAlmostEqual(written['2']['ppt'], expected_ppt, places=7)

    # 34–40 update_player_games_played
    def test_update_player_games_played_when_won_increments_wins_and_games(self):
        """Test for update player games played."""
        data = deepcopy(self.base)
        self.h.read = MagicMock(return_value=data)

        player = DummyPlayer(user_id=0)
        prev_wins = data['0']['wins']
        prev_games = data['0']['games_played']

        self.h.update_player_games_played(player_won=True, player=player)

        self.h.write.assert_called_once()
        written = self.h.write.call_args.args[0]
        self.assertEqual(written['0']['wins'], prev_wins + 1)
        self.assertEqual(written['0']['games_played'], prev_games + 1)

    # 34–40 update_player_games_played
    def test_update_player_games_played_when_lost_increments_games_only(self):
        """Test for player when lost."""
        data = deepcopy(self.base)
        self.h.read = MagicMock(return_value=data)

        player = DummyPlayer(user_id=3)
        prev_wins = data['3']['wins']
        prev_games = data['3']['games_played']

        self.h.update_player_games_played(player_won=False, player=player)

        self.h.write.assert_called_once()
        written = self.h.write.call_args.args[0]
        self.assertEqual(written['3']['wins'], prev_wins)
        self.assertEqual(written['3']['games_played'], prev_games + 1)

        # 44–48 create_leaderboard_information_for_new_players
    def test_create_leaderboard_information_for_new_players__exists(self):
        """create_leaderboard_information_for_new_players."""
        self.h.read = MagicMock(return_value=deepcopy(self.base))
        self.h.create_leaderboard_information_for_new_players(user_id=2)
        self.h.write.assert_not_called()

    def test_create_leaderboard_information_for_new_players__missing(self):
        """create_leaderboard_information_for_new_players."""
        data = deepcopy(self.base)
        self.h.read = MagicMock(return_value=data)

        new_id = 9
        self.h.create_leaderboard_information_for_new_players(user_id=new_id)

        self.h.write.assert_called_once()
        written = self.h.write.call_args.args[0]
        self.assertIn(str(new_id), written)
        self.assertEqual(
            written[str(new_id)],
            {"wins": 0, "games_played": 0, "ppt": 0, "total_turns": 0}
        )


if __name__ == "__main__":
    unittest.main()