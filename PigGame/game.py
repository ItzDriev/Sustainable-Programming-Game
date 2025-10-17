#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module defines a game module in which the game is initialized from."""

import random
from time import sleep
from typing import List
from PigGame.dice_hand import DiceHand
from PigGame.ai_logic import AiLogic
from PigGame.player import Player
from PigGame.utils.turn_manager import TurnManager


class Game:
    """Represents the game object."""

    cheat_mode = False
    dice_emoji = '\u2680\u2681\u2682\u2683\u2684\u2685'

    def __init__(self, dir_path="./PigGame/GameData"):
        """Initialize the game object, player and npc resources.

        :param dir_path: Directory path, eg. './PigGame/GameData'.
        :type dir_path: :py:obj:`str`
        """
        self.game_over = False

        self.ai = AiLogic()

        self.players: List[Player] = []
        self.dice_hand = DiceHand()
        self.turn_manager = TurnManager(dir_path, self.dice_emoji, self)
        self.game_over = False
        self.target_points = 100

    def reset_game(self):
        """Ensure game is reset and has correct players when starting new game."""
        self.game_over = False
        self.ai.score = 0
        self.players = None

    def quit_game(self, player: Player):
        """Prompts quit message, returns to player_turn method.

        :param player: Player quitting the game.
        :type player: Player
        """
        print(f"\n😢 {player.get_username()}...Giving up already? 😢\n")

        for y in range(11):
            print(f"\r⏳ Exiting to menu{'.' * y}", end="")
            sleep(0.1)
        print("\n")
        self.game_over = True

    def start(self, players, target_points, test_mode=False):
        """Decide which player starts first and keeps the game going.

        :param players: List of the current players of the game.
        :type players: List[Player]
        :param target_points: The ending amount of points for the game.
        :type target_points: :py:obj:`int`
        :param test_mode: Boolean indicating if game is started in test mode.
        :type test_mode: :py:obj:`bool`
        """
        if test_mode:
            return

        self.reset_game()

        self.target_points = target_points
        self.ai.round_end_number = target_points
        self.players = players

        # Decide who starts in a singleplayer game
        if len(self.players) == 1:
            match random.randint(1, 2):
                case 1:
                    while not self.game_over:
                        print("")
                        self.turn_manager.npc_turn(self.ai,
                                                   self.dice_hand,
                                                   self.players,
                                                   self.target_points)
                        if self.game_over:
                            break
                        print("")
                        self.turn_manager.player_turn(self.players[0],
                                                      self.dice_hand,
                                                      self.ai,
                                                      self.target_points,
                                                      self.players,
                                                      self.cheat_mode)
                case 2:
                    while not self.game_over:
                        print("")
                        self.turn_manager.player_turn(self.players[0],
                                                      self.dice_hand,
                                                      self.ai,
                                                      self.target_points,
                                                      self.players,
                                                      self.cheat_mode)
                        if self.game_over:
                            break
                        print("")
                        self.turn_manager.npc_turn(self.ai,
                                                   self.dice_hand,
                                                   self.players,
                                                   self.target_points)
        else:
            current_user_index = random.randint(0, 1)
            while not self.game_over:
                current_user_index = 1 if current_user_index == 0 else 0
                print("")
                self.turn_manager.player_turn(self.players[current_user_index],
                                              self.dice_hand,
                                              self.ai,
                                              self.target_points,
                                              self.players,
                                              self.cheat_mode)
                print("")

    def game_status(self):
        """Monitor if game is finished or not.

        :return: The game status
        :return type: :py:obj:`True` | :py:obj:`True`
        """
        return self.game_over
