#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module defines a game module in which the game is initialized from."""

import random
from time import sleep
from typing import List
from PigGame.dice_hand import DiceHand
from PigGame.ai_logic import AiLogic
from PigGame.data_handler import DataHandler
from PigGame.player import Player


class Game:
    """Represents the game object."""

    cheat_mode = False

    def __init__(self, dir_path="./PigGame/GameData"):
        """Initialize the game object, player and npc resources."""
        self.data_handler = DataHandler(dir_path)

        self.game_over = False

        self.ai = AiLogic()
        self.npc_score = 0
        self.npc_dice_hand = DiceHand()

        self.players: List[Player] = []
        self.dice_hand = DiceHand()
        self.game_over = False
        self.target_points = 100

    def npc_turn(self, player: Player):
        """Npc takes turn, sends result to the intelligence class."""
        turn_score = 0
        turn_history = "🐷----------Turn History For: Computer-AI----------🐷\n"

        while True:
            for _ in range(40):
                print("")
            print(turn_history)
            player_score = self.players[0].score
            if self.ai.should_roll(self.npc_score, player_score):
                self.npc_dice_hand.roll_dice()
                value = self.npc_dice_hand.get_last_roll()
                print(f"🤖 Mr AI rolled {self.npc_dice_hand.get_last_roll()[0]}"
                      f" and {self.npc_dice_hand.get_last_roll()[1]}"
                      f" {'\u2680\u2681\u2682\u2683\u2684\u2685'[value[0]-1]}"
                      f" {'\u2680\u2681\u2682\u2683\u2684\u2685'[value[1]-1]}")
            else:
                break

            if not self.rolled_one(self.npc_dice_hand.get_last_roll()[0],
                                   self.npc_dice_hand.get_last_roll()[1]):
                total_roll = sum(self.npc_dice_hand.get_last_roll())
                self.npc_score += (total_roll)
                turn_score += (total_roll)
                self.ai.increment_turn_score(total_roll)

                if self.npc_score >= self.target_points:
                    print(f"🤖 Mr AI reached {self.target_points} points. Game over 🤖\n")
                    self.game_over = True
                    self.ai.reset_turn_score()
                    self.data_handler.leaderboard_data.update_games_played(False, player)
                    break
                print(f"Mr AI's total score: {self.npc_score}")
                turn_history += (f"Rolled: {self.npc_dice_hand.get_last_roll()[0]}" +
                                 f" and {self.npc_dice_hand.get_last_roll()[1]}\n")
                sleep(1)

            elif (not self.rolled_two_ones(self.npc_dice_hand.get_last_roll()[0],
                                           self.npc_dice_hand.get_last_roll()[1])):
                self.ai.reset_turn_score()
                self.npc_score -= turn_score
                print("❌ Mr AI rolled 1. His score will "
                      f"be reset down to {self.npc_score} ❌")
                sleep(2.5)
                break
            else:
                self.npc_score = 0
                print(f"❌ Oh noooooo! Mr. AI rolled two 1's. "
                      f"Score will be reset down to {self.npc_score} ❌")
                sleep(2.5)
                break

    def player_turn(self, player: Player):
        """Player(s) takes turn rolling dice."""
        if Game.cheat_mode:
            player.score += self.target_points

        turn_score = 0
        turn_history = ("🐷----------Turn History For:" +
                        f"{player.get_username()}----------🐷\n")

        while True:
            for _ in range(40):
                print("")
            print(turn_history)

            self.dice_hand.roll_dice()
            self.ai.increment_turn_round_for_player()
            dice_points = self.dice_hand.get_last_roll()

            print(f"{player.get_username()} rolled {self.dice_hand.get_last_roll()[0]}"
                  f" and {self.dice_hand.get_last_roll()[1]}"
                  f" {'\u2680\u2681\u2682\u2683\u2684\u2685'[dice_points[0]-1]}"
                  f" {'\u2680\u2681\u2682\u2683\u2684\u2685'[dice_points[1]-1]}")

            # Evaluate if any roll is 1
            if (not self.rolled_one(dice_points[0],
                                    dice_points[1])):

                total_points = sum(dice_points)
                player.score += (total_points)
                turn_score += (total_points)
                if player.score >= self.target_points:
                    print(f"🎉 {player.get_username()} reached"
                          f" {self.target_points} points. "
                          f"{player.get_username()} wins! 🎉\n")
                    self.game_over = True
                    self.ai.reset_turn_score()
                    self.data_handler.leaderboard_data.update_ppt_and_turns(player, turn_score)
                    self.data_handler.leaderboard_data.update_games_played(True, player)

                    for p in self.players:
                        if p == player:
                            self.data_handler.leaderboard_data.update_games_played(True, player)
                        else:
                            self.data_handler.leaderboard_data.update_games_played(False, p)
                    break

                option = input(f"{player.get_username()}'s " +
                               f"Total score: {player.score}" +
                               "\n\nContinue? 'y'/'n' or 'quit' to quit\n")
                turn_history += (f"Rolled: {self.dice_hand.get_last_roll()[0]}" +
                                 f" and {self.dice_hand.get_last_roll()[1]}\n")
                match option:
                    case "y":
                        continue
                    case "n":
                        self.data_handler.leaderboard_data.update_ppt_and_turns(player, turn_score)
                        break
                    case "quit":
                        self.quit_game(player)  # Prompts quit message
                        break  # Breaks loop and returns to start()

            elif (not self.rolled_two_ones(self.dice_hand.get_last_roll()[0],
                                           self.dice_hand.get_last_roll()[1])):
                self.ai.reset_turn_score()
                self.data_handler.leaderboard_data.update_ppt_and_turns(player, 0)
                player.score -= turn_score
                print(f"❌ Dang it! {player.get_username()} rolled 1."
                      f"Score will be reset down to {player.score} ❌")
                sleep(2.5)
                break
            else:
                player.score = 0
                self.data_handler.leaderboard_data.update_ppt_and_turns(player, 0)
                print(f"❌ Oh noooooo! {player.get_username()} rolled two 1's. "
                      f"Score will be reset down to {player.score} ❌")
                sleep(2.5)
                break

    def reset_game(self):
        """Ensure game is reset and has correct players when starting new game."""
        self.game_over = False
        self.npc_score = 0
        self.players = None

    def quit_game(self, player: Player):
        """Prompts quit message, returns to player_turn method."""
        print(f"\n😢 {player.get_username()}...Giving up already? 😢\n")

        for y in range(11):
            print(f"\r⏳ Exiting to menu{'.' * y}", end="")
            sleep(0.1)
        print("\n")
        self.game_over = True

    def start(self, players, target_points, test_mode=False):
        """Decide which player starts first and keeps the game going."""
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
                        self.npc_turn(self.players[0])
                        if self.game_over:
                            break
                        print("")
                        self.player_turn(self.players[0])
                case 2:
                    while not self.game_over:
                        print("")
                        self.player_turn(self.players[0])
                        if self.game_over:
                            break
                        print("")
                        self.npc_turn(self.players[0])
        else:
            current_user_index = random.randint(0, 1)
            while not self.game_over:
                current_user_index = 1 if current_user_index == 0 else 0
                print("")
                self.player_turn(self.players[current_user_index])
                print("")

    def rolled_one(self, value_one, value_two):
        """Determine if player may continue or not."""
        if value_one == 1 or value_two == 1:
            return True
        return False

    def rolled_two_ones(self, value_one, value_two):
        """Determine if player may continue or not."""
        if value_one == 1 and value_two == 1:
            return True
        return False

    def game_status(self):
        """Monitor if game is finished or not."""
        return self.game_over
