#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module for ai rolling logic."""


class AiLogic:
    """Handles how the AI thinks."""

    difficulty = 0

    def __init__(self):
        """Declare variables."""
        self.__turn_score = 0
        self.first_start_hand = 0
        self.__target = 0
        self.enemy_total_rolls_this_round = 0
        self.npc_total_rolls_this_round = 0
        self.if_under_then_hit_once_more = True
        self.first_time_rolling = 0
        self.round_end_number = 100
        self.near_end_buffer = 10

    def rasmus_ai_difficulty(self, npc_score, player_score):
        """Logic for difficulty 1 (Rasmus difficulty)."""
        if self.first_time_rolling > 0:
            self.first_time_rolling -= 1
            return True
        if player_score > npc_score:
            if self.npc_total_rolls_this_round < self.enemy_total_rolls_this_round:
                self.npc_total_rolls_this_round += 1
                return True
            if self.if_under_then_hit_once_more:
                self.if_under_then_hit_once_more = False
                return True
        if npc_score > self.round_end_number - self.near_end_buffer:
            return True
        self.reset_turn_score()
        return False

    def johan_ai_difficulty(self, npc_score, player_score):
        """Logic for difficulty 2 (Johans difficulty)."""
        self.first_start_hand += 1

        if npc_score >= self.round_end_number - self.near_end_buffer:
            return True

        if self.first_start_hand == 1:
            self.__target = 15
            self.__target -= max(min(npc_score // 25, 4), 0)

            diff = npc_score - player_score
            if diff >= 20:
                self.__target -= 3
            elif diff <= -20:
                self.__target += 5

        if self.__turn_score < self.__target:
            return True
        self.reset_turn_score()
        return False

    def anton_ai_difficulty(self, npc_score, player_score):
        """Logic for difficulty 3 (Anton difficulty)."""
        self.first_start_hand += 1

        diff = npc_score - player_score

        if self.first_start_hand == 1:
            self.__target = 16
            self.__target -= max(min(npc_score // 20, 4), 0)
            # Comment just in case AI doesnt work properly
            # like this although I dont see a reason why it would break
            # diff=npc_score - player score used to be here,
            # moved it out of if statement

            if diff >= 20:
                self.__target -= 4
            elif diff <= -20:
                self.__target += 6

            if npc_score >= self.round_end_number - self.near_end_buffer:
                self.__target -= 2

            self.__target = max(6, min(self.__target, 22))

        push_buffer = 3 if diff < 0 else 0

        if self.__turn_score < self.__target + push_buffer:
            return True

        self.reset_turn_score()
        return False

    def liam_ai_difficulty(self, npc_score, player_score):
        """Logic for difficulty 4 (Liam difficulty)."""
        needed = self.round_end_number - npc_score
        diff = npc_score - player_score

        # safe (no 1s) = 25/36, mean safe gain ≈ 8
        # single 1 (turn bust) = 10/36  -> lose current turn score
        # double 1 (wipe total) = 1/36  -> lose current turn score + total score
        p_safe = 25 / 36
        p_bust = 10 / 36
        p_wipe = 1 / 36
        safe_mean_gain = 8
        max_gain = 12

        if self.__turn_score + max_gain >= needed:
            return True

        # Expected value of one more roll vs banking now
        ev_next = (
            p_safe * safe_mean_gain
            - p_bust * self.__turn_score
            - p_wipe * (self.__turn_score + npc_score)
        )

        threshold = 0.02 * diff  # +0.4 at +20 lead, -0.4 at -20 behind

        if needed <= self.near_end_buffer:
            threshold += 0.2

        if player_score >= self.round_end_number - self.near_end_buffer:
            threshold -= 0.3

        if ev_next > threshold:
            return True

        self.reset_turn_score()
        return False

    def should_roll(self, npc_score, player_score):
        """Dice which difficulty function that should be played."""
        match AiLogic.difficulty:
            case 1:
                return self.rasmus_ai_difficulty(npc_score, player_score)
            case 2:
                return self.johan_ai_difficulty(npc_score, player_score)
            case 3:
                return self.anton_ai_difficulty(npc_score, player_score)
            case 4:
                return self.liam_ai_difficulty(npc_score, player_score)

    def reset_turn_score(self):
        """Reset all variables after AI played his turn."""
        self.__turn_score = 0
        self.first_start_hand = 0
        self.npc_total_rolls_this_round = 0
        self.enemy_total_rolls_this_round = 0
        self.if_under_then_hit_once_more = True
        self.first_time_rolling = 2

    def increment_turn_score(self, score):
        """Increment score for current turn."""
        self.__turn_score += score

    def increment_turn_round_for_player(self):
        """Increments turn score for player."""
        self.enemy_total_rolls_this_round += 1
