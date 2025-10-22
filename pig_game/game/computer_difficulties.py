#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ComputerDifficulties module."""


class ComputerDifficulties:
    """Defines difficulty logics."""

    round_end_number = 100
    near_end_buffer = 10

    def __init__(self, computer):
        """Initialize state.

        :param computer: Owning computer instance.
        :type computer: Computer
        """
        self.__turn_score = 0
        self.first_start_hand = 0
        self.enemy_total_rolls_this_round = 0
        self.npc_total_rolls_this_round = 0
        self.if_under_then_hit_once_more = True
        self.first_time_rolling = 0
        self.computer = computer

    def easy_mode(self, player_score, computer_score):
        """Difficulty easy mode.

        :param player_score: Player's total score.
        :type player_score: int
        :param computer_score: Computer's total score.
        :type computer_score: int
        :return: Whether to roll.
        :rtype: bool
        """
        if self.first_time_rolling > 0:
            self.first_time_rolling -= 1
            return True
        if player_score > computer_score:
            if self.npc_total_rolls_this_round < self.enemy_total_rolls_this_round:
                self.npc_total_rolls_this_round += 1
                return True
            if self.if_under_then_hit_once_more:
                self.if_under_then_hit_once_more = False
                return True
        if computer_score > self.round_end_number - self.near_end_buffer:
            return True
        self.reset_turn_score()
        return False

    def medium_mode(self, player_score, computer_score):
        """Difficulty medium mode.

        :param player_score: Player's total score.
        :type player_score: int
        :param computer_score: Computer's total score.
        :type computer_score: int
        :return: Whether to roll.
        :rtype: bool
        """
        self.first_start_hand += 1

        target_points_for_turn = 0

        if computer_score >= self.round_end_number - self.near_end_buffer:
            return True

        if self.first_start_hand == 1:
            target_points_for_turn = 15
            target_points_for_turn -= max(min(computer_score // 25, 4), 0)

            diff = computer_score - player_score
            if diff >= 20:
                target_points_for_turn -= 3
            elif diff <= -20:
                target_points_for_turn += 5

        if self.__turn_score < target_points_for_turn:
            return True
        self.reset_turn_score()
        return False

    def hard_mode(self, player_score, computer_score):
        """Difficulty hard_mode.

        :param player_score: Player's total score.
        :type player_score: int
        :param computer_score: Computer's total score.
        :type computer_score: int
        :return: Whether to roll.
        :rtype: bool
        """
        self.first_start_hand += 1

        target_points_for_turn = 0

        diff = computer_score - player_score

        if self.first_start_hand == 1:
            target_points_for_turn = 16
            target_points_for_turn -= max(min(computer_score // 20, 4), 0)

            if diff >= 20:
                target_points_for_turn -= 4
            elif diff <= -20:
                target_points_for_turn += 6

            if computer_score >= self.round_end_number - self.near_end_buffer:
                target_points_for_turn -= 2

            target_points_for_turn = max(6, min(target_points_for_turn, 22))

        push_buffer = 3 if diff < 0 else 0

        if self.__turn_score < target_points_for_turn + push_buffer:
            return True

        self.reset_turn_score()
        return False

    def extreme_mode(self, player_score, computer_score):
        """Difficulty extreme mode.

        :param player_score: Player's total score.
        :type player_score: int
        :param computer_score: Computer's total score.
        :type computer_score: int
        :return: Whether to roll.
        :rtype: bool
        """
        needed = self.round_end_number - computer_score
        diff = computer_score - player_score

        p_safe = 25 / 36
        p_bust = 10 / 36
        p_wipe = 1 / 36
        safe_mean_gain = 8
        max_gain = 12

        if self.__turn_score + max_gain >= needed:
            return True

        ev_next = (
            p_safe * safe_mean_gain
            - p_bust * self.__turn_score
            - p_wipe * (self.__turn_score + computer_score)
        )

        threshold = 0.02 * diff

        if needed <= self.near_end_buffer:
            threshold += 0.2

        if player_score >= self.round_end_number - self.near_end_buffer:
            threshold -= 0.3

        if ev_next > threshold:
            return True

        self.reset_turn_score()
        return False

    def reset_turn_score(self):
        """Reset all variables after AI played his turn."""
        self.__turn_score = 0
        self.first_start_hand = 0
        self.npc_total_rolls_this_round = 0
        self.enemy_total_rolls_this_round = 0
        self.if_under_then_hit_once_more = True
        self.first_time_rolling = 2

    def increment_turn_score(self, score):
        """Increase the current turn score.

        :param score: Amount to add.
        :type score: int
        """
        self.__turn_score += score

    def increment_turn_round_for_player(self):
        """Increments turn score for player."""
        self.enemy_total_rolls_this_round += 1
