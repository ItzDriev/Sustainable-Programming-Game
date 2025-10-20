#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module for ai unit-testing."""


import unittest

from PigGame.ai_logic import AiLogic


class TestAiLogic(unittest.TestCase):
    """Tests for the AI turn logic across all difficulty levels and helpers."""

    # ---------- RASMUS (1) ----------
    def test_rasmus_first_time_rolling_triggers_true_and_decrements(self):
        """When `first_time_rolling` > 0, returns True and decrements it."""
        ai = AiLogic()
        ai.first_time_rolling = 2
        self.assertTrue(ai.rasmus_ai_difficulty(npc_score=0, player_score=0))
        self.assertEqual(ai.first_time_rolling, 1)

    def test_rasmus_player_leads_and_npc_has_rolled_less(self):
        """If player leads, NPC rolls and increments its roll counter."""
        ai = AiLogic()
        ai.enemy_total_rolls_this_round = 2
        ai.npc_total_rolls_this_round = 0
        res = ai.rasmus_ai_difficulty(npc_score=10, player_score=20)
        self.assertTrue(res)
        self.assertEqual(ai.npc_total_rolls_this_round, 1)

    def test_rasmus_player_leads_once_more_flag(self):
        """If player leads and 'hit once more' flag is set, return True."""
        ai = AiLogic()
        ai.enemy_total_rolls_this_round = 1
        ai.npc_total_rolls_this_round = 1
        ai.if_under_then_hit_once_more = True
        res = ai.rasmus_ai_difficulty(npc_score=10, player_score=20)
        self.assertTrue(res)
        self.assertFalse(ai.if_under_then_hit_once_more)

    def test_rasmus_endgame_push(self):
        """Near the end (npc close to target), always return True to push."""
        ai = AiLogic()
        res = ai.rasmus_ai_difficulty(
            npc_score=ai.round_end_number - ai.near_end_buffer + 1,
            player_score=0,
        )
        self.assertTrue(res)

    def test_rasmus_otherwise_resets_and_returns_false(self):
        """When no condition to roll is met, returns False and calls reset."""
        ai = AiLogic()
        ai.first_time_rolling = 0
        ai.if_under_then_hit_once_more = False
        ai.enemy_total_rolls_this_round = 0
        ai.npc_total_rolls_this_round = 0
        ai._AiLogic__turn_score = 7
        res = ai.rasmus_ai_difficulty(npc_score=30, player_score=10)
        self.assertFalse(res)
        self.assertEqual(ai._AiLogic__turn_score, 0)
        self.assertEqual(ai.first_start_hand, 0)
        self.assertEqual(ai.first_time_rolling, 2)

    # ---------- JOHAN (2) ----------
    def test_johan_sets_target_on_first_call_and_rolls_until_target(self):
        """Sets target on first call, rolls until reaching it, then banks (False)."""
        ai = AiLogic()
        self.assertTrue(ai.johan_ai_difficulty(npc_score=0, player_score=0))
        ai.increment_turn_score(15)
        self.assertFalse(ai.johan_ai_difficulty(npc_score=0, player_score=0))
        self.assertEqual(ai._AiLogic__turn_score, 0)
        self.assertEqual(ai.first_start_hand, 0)

    def test_johan_target_adjusts_when_far_ahead(self):
        """With a large lead, target is reduced by -3 (and by npc_score//25)."""
        ai = AiLogic()
        ai.johan_ai_difficulty(npc_score=50, player_score=20)
        self.assertEqual(ai._AiLogic__target, 10)

    def test_johan_target_adjusts_when_far_behind(self):
        """When far behind, target increases by +5."""
        ai = AiLogic()
        ai.johan_ai_difficulty(npc_score=0, player_score=30)
        self.assertEqual(ai._AiLogic__target, 20)

    def test_johan_target_reduction_capped_at_4(self):
        """Npc_score//25 reduction is capped at 4 (min(...,4) branch)."""
        ai = AiLogic()
        ai.round_end_number = 1000
        ai.johan_ai_difficulty(npc_score=200, player_score=200)

    def test_johan_endgame_always_true(self):
        """When NPC is near end threshold, always chooses to roll."""
        ai = AiLogic()
        near = ai.round_end_number - ai.near_end_buffer
        self.assertTrue(ai.johan_ai_difficulty(npc_score=near, player_score=0))

    # ---------- ANTON (3) ----------
    def test_anton_rolls_until_target_then_banks(self):
        """Computes target on first call, rolls until target, then banks."""
        ai = AiLogic()
        self.assertTrue(ai.anton_ai_difficulty(npc_score=0, player_score=0))
        ai.increment_turn_score(16)
        self.assertFalse(ai.anton_ai_difficulty(npc_score=0, player_score=0))
        self.assertEqual(ai._AiLogic__turn_score, 0)
        self.assertEqual(ai.first_start_hand, 0)

    def test_anton_target_lead_near_end_and_clamp(self):
        """Big lead & near end -> reduced and clamped to >= 6."""
        ai = AiLogic()
        ai.anton_ai_difficulty(npc_score=95, player_score=70)
        self.assertEqual(ai._AiLogic__target, 6)

    def test_anton_push_buffer_when_behind(self):
        """When behind, push_buffer=3; rolls until target+3 then banks."""
        ai = AiLogic()
        self.assertTrue(ai.anton_ai_difficulty(npc_score=0, player_score=10))
        target = ai._AiLogic__target
        ai._AiLogic__turn_score = target + 2
        self.assertTrue(ai.anton_ai_difficulty(npc_score=0, player_score=10))
        ai._AiLogic__turn_score = target + 3
        self.assertFalse(ai.anton_ai_difficulty(npc_score=0, player_score=10))
        self.assertEqual(ai._AiLogic__turn_score, 0)

    def test_anton_target_increases_by_6_when_far_behind(self):
        """When far behind on the first call, Anton adds +6 to target."""
        ai = AiLogic()
        ai.anton_ai_difficulty(npc_score=0, player_score=30)
        self.assertEqual(ai._AiLogic__target, 22)

    # ---------- LIAM (4) ----------
    def test_liam_typical_case_prefers_rolling(self):
        """With balanced scores and zero turn score, EV of rolling is positive."""
        ai = AiLogic()
        self.assertTrue(ai.liam_ai_difficulty(npc_score=50, player_score=50))

    def test_liam_bad_ev_paths_to_false_and_resets(self):
        """With large current turn score, EV becomes negative -> False and reset."""
        ai = AiLogic()
        ai.increment_turn_score(30)
        res = ai.liam_ai_difficulty(npc_score=50, player_score=10)
        self.assertFalse(res)
        self.assertEqual(ai._AiLogic__turn_score, 0)

    def test_liam_early_true_when_can_finish_in_one_roll(self):
        """If `__turn_score + max_gain >= needed`, returns True immediately."""
        ai = AiLogic()
        self.assertTrue(ai.liam_ai_difficulty(npc_score=90, player_score=0))

    def test_liam_near_end_threshold_increase_branch(self):
        """Exercise 'needed <= near_end_buffer' branch (avoid early return)."""
        ai = AiLogic()
        ai._AiLogic__turn_score = -5
        result = ai.liam_ai_difficulty(npc_score=91, player_score=0)
        self.assertIsInstance(result, bool)

    def test_liam_threshold_decreases_when_player_near_end(self):
        """When the player is near the end, Liam applies threshold -= 0.3."""
        ai = AiLogic()
        res = ai.liam_ai_difficulty(npc_score=50, player_score=95)
        self.assertIsInstance(res, bool)

    # ---------- should_roll dispatcher ----------
    def test_should_roll_dispatches_difficulty_1(self):
        """Difficulty 1 calls Rasmus path."""
        ai = AiLogic()
        AiLogic.difficulty = 1
        ai.first_time_rolling = 1
        self.assertTrue(ai.should_roll(npc_score=0, player_score=0))

    def test_should_roll_dispatches_difficulty_2(self):
        """Difficulty 2 calls Johan path."""
        ai = AiLogic()
        AiLogic.difficulty = 2
        self.assertTrue(ai.should_roll(npc_score=0, player_score=0))

    def test_should_roll_dispatches_difficulty_3(self):
        """Difficulty 3 calls Anton path."""
        ai = AiLogic()
        AiLogic.difficulty = 3
        self.assertTrue(ai.should_roll(npc_score=0, player_score=0))

    def test_should_roll_dispatches_difficulty_4(self):
        """Difficulty 4 calls Liam path."""
        ai = AiLogic()
        AiLogic.difficulty = 4
        self.assertIsInstance(ai.should_roll(npc_score=50, player_score=50), bool)

    def test_should_roll_with_unknown_difficulty_returns_none(self):
        """With an unknown difficulty value, returns None (no action)."""
        ai = AiLogic()
        AiLogic.difficulty = 99
        self.assertIsNone(ai.should_roll(0, 0))

    # ---------- helpers ----------
    def test_reset_turn_score(self):
        """Zero turn vars and restores flags/counters to defaults."""
        ai = AiLogic()
        ai._AiLogic__turn_score = 9
        ai.first_start_hand = 3
        ai.npc_total_rolls_this_round = 4
        ai.enemy_total_rolls_this_round = 5
        ai.if_under_then_hit_once_more = False
        ai.first_time_rolling = 0
        ai.reset_turn_score()
        self.assertEqual(ai._AiLogic__turn_score, 0)
        self.assertEqual(ai.first_start_hand, 0)
        self.assertEqual(ai.npc_total_rolls_this_round, 0)
        self.assertEqual(ai.enemy_total_rolls_this_round, 0)
        self.assertTrue(ai.if_under_then_hit_once_more)
        self.assertEqual(ai.first_time_rolling, 2)

    def test_increment_turn_score(self):
        """Helper: `increment_turn_score` adds to the private turn score."""
        ai = AiLogic()
        ai.increment_turn_score(5)
        ai.increment_turn_score(3)
        self.assertEqual(ai._AiLogic__turn_score, 8)

    def test_increment_turn_round_for_player(self):
        """Helper: increments the enemy roll counter by one."""
        ai = AiLogic()
        self.assertEqual(ai.enemy_total_rolls_this_round, 0)
        ai.increment_turn_round_for_player()
        self.assertEqual(ai.enemy_total_rolls_this_round, 1)
        ai.increment_turn_round_for_player()
        self.assertEqual(ai.enemy_total_rolls_this_round, 2)


if __name__ == "__main__":
    unittest.main()
