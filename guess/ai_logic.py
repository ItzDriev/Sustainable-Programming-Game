#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module for ai rolling logic."""


class AiLogic:
    """Halloj."""
    def __init__(self):
        """Halloj."""
        self.__turn_score = 0
        self.first_start_hand = 0
        self.difficulty = 1
        self.__target = 0

    def rasmus_ai_difficulty(self, npc_score, player_score):
        """Halloj."""
        self.first_start_hand += 1

        if npc_score >= 90:  # Kommer att kolla så att inte ai stannar närmare än 90+
            return True

        if self.first_start_hand == 1:
            self.__target = 15
            self.__target -= max(min(npc_score // 25, 4), 0)  # Denna kommer att börja på 0, sedan efter varje 25 så kommer 1 adderas, så de gör desto nämre Ai'n är
            # desto säkrare kommer den vara, så 25 -1, 50 -2, 75 -3

            diff = npc_score - player_score  # Denna kommer kolla ifall motståndaren är långt borta, är de 20+ så läggs 5 på risk, är motståndaren 20 bak, så kommer ai köra säkrare
            if diff >= 20:
                self.__target -= 3
            elif diff <= -20:
                self.__target += 5
        return self.end_turn_or_keep_going()

    def johan_ai_difficulty(self, npc_score, player_score):
        """Halloj."""
        pass

    def anton_ai_difficulty(self, npc_score, player_score):
        """Halloj."""
        pass

    def liam_ai_difficulty(self, npc_score, player_score):
        """Halloj."""
        pass

    def should_roll(self, npc_score, player_score):
        """Halloj."""
        match self.difficulty:
            case 1:
                return self.rasmus_ai_difficulty(npc_score, player_score)
            case 2:
                return self.johan_ai_difficulty(npc_score, player_score)
            case 3:
                return self.anton_ai_difficulty(npc_score, player_score)
            case 4:
                return self.liam_ai_difficulty(npc_score, player_score)

    def end_turn_or_keep_going(self):
        """Halloj."""
        if self.__turn_score < self.__target:  # Här väljs det ifall Ai'n ska slå igen eller stanna
            return True
        self.reset_turn_score()
        return False

    def reset_turn_score(self):
        """Halloj."""
        self.__turn_score = 0
        self.first_start_hand = 0

    def increment_turn_score(self, score):
        """Halloj."""
        self.__turn_score += score
