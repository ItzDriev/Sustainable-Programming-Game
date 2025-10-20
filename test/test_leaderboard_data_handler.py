#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing for LeaderboardDataHandler."""

import unittest
import tempfile
from pathlib import Path
from io import StringIO
import contextlib
from copy import deepcopy

from PigGame.leaderboard_data_handler import LeaderboardDataHandler
from PigGame.data_handler import DataHandler


class DummyPlayer:
    """Player with only get_user_id()."""

    def __init__(self, user_id: int):
        """Store the provided user id."""
        self._id = user_id

    def get_user_id(self) -> int:
        """Return the stored user id."""
        return self._id


class TestLeaderBoardDataHandlerClass(unittest.TestCase):
    """Unit tests targeting LeaderboardDataHandler methods."""

    def setUp(self):
        """Create an isolated temp directory and seed LeaderboardData.json."""
        self.tmp = tempfile.TemporaryDirectory()
        self.dir_path = Path(self.tmp.name)
        self.lb_file = self.dir_path / "LeaderboardData.json"
        self.user_file = self.dir_path / "UserData.json"
        self.lb = LeaderboardDataHandler(self.lb_file, self.dir_path)
        self.base = {
            '0': {'wins': 1, 'games_played': 1, 'ppt': 13.5, 'total_turns': 4},
            '1': {'wins': 0, 'games_played': 1, 'ppt': 9.75, 'total_turns': 4},
            '3': {'wins': 1, 'games_played': 1, 'ppt': 1.0, 'total_turns': 1},
        }
        self.lb.write(deepcopy(self.base))

    def tearDown(self):
        """Clean up the temporary directory."""
        self.tmp.cleanup()

    def test_get_highscore(self):
        """Get_highscore returns dict for a given user_id."""
        self.assertEqual(self.lb.get_highscore(0), self.base['0'])
        self.assertEqual(self.lb.get_highscore('3')['ppt'], 1.0)

    def test_update_ppt_and_turns(self):
        """Update_ppt_and_turns increments turns and updates running average ppt."""
        player = DummyPlayer(user_id=1)
        data_before = self.lb.read()
        old_turns = data_before['1']['total_turns']
        old_ppt = data_before['1']['ppt']
        value = 11.0
        expected_turns = old_turns + 1
        expected_ppt = (old_ppt * old_turns + value) / expected_turns
        self.lb.update_ppt_and_turns(player, value)
        data_after = self.lb.read()
        self.assertEqual(data_after['1']['total_turns'], expected_turns)
        self.assertAlmostEqual(data_after['1']['ppt'], expected_ppt, places=7)

    def test_update_games_played_won(self):
        """Test for win path in update_games_played."""
        player = DummyPlayer(user_id=0)
        data_before = self.lb.read()
        wins_before = data_before['0']['wins']
        games_before = data_before['0']['games_played']
        self.lb.update_games_played(True, player)
        data_after = self.lb.read()
        self.assertEqual(data_after['0']['wins'], wins_before + 1)
        self.assertEqual(data_after['0']['games_played'], games_before + 1)

    def test_update_games_played_lost(self):
        """Test for loss path in update_games_played."""
        player = DummyPlayer(user_id=1)
        data_before = self.lb.read()
        wins_before = data_before['1']['wins']
        games_before = data_before['1']['games_played']
        self.lb.update_games_played(False, player)
        data_after = self.lb.read()
        self.assertEqual(data_after['1']['wins'], wins_before)
        self.assertEqual(data_after['1']['games_played'], games_before + 1)

    def test_add_new_player_exists(self):
        """Check if player already have stats."""
        self.lb.add_new_player(0)
        data = self.lb.read()
        self.assertEqual(data['0'], self.base['0'])

    def test_add_new_player_missing(self):
        """Check if player have no stats."""
        new_id = 9
        self.lb.add_new_player(new_id)
        data = self.lb.read()
        self.assertIn(str(new_id), data)
        self.assertEqual(
            data[str(new_id)],
            {"wins": 0, "games_played": 0, "ppt": 0, "total_turns": 0}
        )


class TestDataHandlerPrintLeaderboard(unittest.TestCase):
    """Unit tests for DataHandler.print_leaderboard output ordering and limits."""

    def setUp(self):
        """Create temp data files and seed leaderboard."""
        self.tmp = tempfile.TemporaryDirectory()
        self.dir_path = Path(self.tmp.name)
        self.lb_file = self.dir_path / "LeaderboardData.json"
        self.user_file = self.dir_path / "UserData.json"
        self.base = {
            '0': {'wins': 1, 'games_played': 1, 'ppt': 13.5, 'total_turns': 4},
            '1': {'wins': 0, 'games_played': 1, 'ppt': 9.75, 'total_turns': 4},
            '3': {'wins': 1, 'games_played': 1, 'ppt': 1.0, 'total_turns': 1},
        }
        self.lb = LeaderboardDataHandler(self.lb_file, self.dir_path)
        self.lb.write(deepcopy(self.base))
        self.dh = DataHandler(dir_path=self.dir_path)
        self.dh.user_data.get_username = (
            lambda uid: {0: "Alice", 1: "Bob", 3: "Carol"}[uid]
        )

    def tearDown(self):
        """Remove temporary test artifacts."""
        self.tmp.cleanup()

    def test_print_leaderboard_order_and_default_limit(self):
        """Sorts by ppt descending and respects default top 10 limit."""
        buf = StringIO()
        with contextlib.redirect_stdout(buf):
            self.dh.print_leaderboard(arg="")
        out = buf.getvalue().splitlines()
        rows = [line for line in out if line.startswith("|") and "Top" not in line]
        self.assertIn("Alice", rows[0])
        self.assertIn("Bob", rows[1])
        self.assertIn("Carol", rows[2])
        self.assertIn("13.50", rows[0])
        self.assertIn("9.75", rows[1])
        self.assertIn("1.00", rows[2])

    def test_print_leaderboard_with_limit(self):
        """Applies provided numeric limit to number of printed rows."""
        buf = StringIO()
        with contextlib.redirect_stdout(buf):
            self.dh.print_leaderboard(arg="2")
        out = buf.getvalue().splitlines()
        rows = [line for line in out if line.startswith("|") and "Top" not in line]
        data_rows = [r for r in rows if "Name:" not in r]
        self.assertEqual(len(data_rows), 2)
        self.assertIn("Alice", data_rows[0])


if __name__ == "__main__":
    """Run the unittest module."""
    unittest.main()
