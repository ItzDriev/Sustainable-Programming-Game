#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module defines a game module in which the game is initialized from"""

import random
from time import sleep
from guess.dice_hand import DiceHand
from guess.ai_logic import AiLogic
from guess.data_handler import DataHandler
from guess.player import Player

class Game:
    """Represents the game object"""
    
    def __init__(self, leaderboard = None, dir_path="./guess/GameData"):
        """Initialize the game object, player and npc resources"""
        
        self.data_handler = DataHandler(dir_path)
        
        self.ai = AiLogic()
        self.npc_score = 0
        self.npc_dice_one = DiceHand()
        self.npc_dice_two = DiceHand()

        self.players = []
        self.dice_one = DiceHand()
        self.dice_two = DiceHand()
        
        self.game_over = False
        
    def npc_turn(self, difficulty):
        
        """Npc takes turn, sends result to the intelligence class."""
        turn_score = 0
        turn_history = "🐷----------Turn History For: Computer-AI----------🐷\n"

        while True:
            for i in range(40):
                print("")
            print(turn_history)
            player_score = self.players[0].score
            
            if self.ai.should_roll(self.npc_score, player_score, difficulty):
                self.npc_hand.roll_dice()
                value = self.npc_hand.get_last_roll()
                print(f"🤖 Mr AI rolled {value} {'\u2680\u2681\u2682\u2683\u2684\u2685'[value-1]}")
            else:
                break

            if self.evaluate(self.npc_dice_one.get_last_roll(), self.npc_dice_two.get_last_roll()):
                total_roll = self.npc_dice_one.get_last_roll() + self.npc_dice_two.get_last_roll()
                self.npc_score += (total_roll)
                turn_score += (total_roll) 
                self.ai.increment_turn_score(total_roll)

                if (self.npc_score >= 100):
                    print ("🤖 Mr AI reached 100 points. Game over 🤖")
                    self.game_over = True
                    self.ai.reset_turn_score()
                    break

                
                print (f"Mr AI's total score: {self.npc_score}")
                turn_history+=f"Rolled: {self.npc_dice_one.get_last_roll() + self.npc_dice_two.get_last_roll()}\n"
                sleep(1)
                continue  # Placeholder for continue-logic

            else:
                self.ai.reset_turn_score()
                self.npc_score -= turn_score
                print (f"❌ Mr AI rolled 1. His score will be reset down to {self.npc_score} ❌")
                sleep(2.5)
                break
                  
    def player_turn(self, player):
        """Player(s) takes turn rolling dice"""

        if self.game_over:
            return
        
        turn_score = 0
        turn_history = f"🐷----------Turn History For: {player.get_username()}----------🐷\n"

        while True: 
            for i in range(40):
                print("")
            print(turn_history)

            self.dice_one.roll_dice()
            self.dice_two.roll_dice()
            self.ai.increment_turn_round_for_player()
            value = self.dice_hand.get_last_roll()
            print (f"{player.get_username()} rolled {value}  {'\u2680\u2681\u2682\u2683\u2684\u2685'[value-1]}")
            
            print (f"{player.get_username()} rolled {self.dice_one.get_last_roll()} and {self.dice_two.get_last_roll()}!")
            
            #Evaluate if any roll is 1
            if (self.evaluate(self.dice_one.get_last_roll(), self.dice_two.get_last_roll())):
                total_roll = (self.dice_one.get_last_roll() + self.dice_two.get_last_roll())
                player.score += (total_roll)
                turn_score += (total_roll)
                if  player.score >= 100:
                    print (f"🎉 {player.get_username()} reached 100 points. {player.get_username()} wins! 🎉")
                    self.game_over = True
                    self.ai.reset_turn_score()
                    break
                
                #Needs a quit method    
                option = input (f"{player.get_username()}'s Total score: {player.score} \n\nContinue? 'y'/'n' or 'quit' to quit\n")
                turn_history+=f"Rolled: {self.dice_one.get_last_roll() + self.dice_two.get_last_roll()}\n"
                match option:
                    case "y":
                        continue
                    case "n":
                        break
                    case "quit":
                        self.quit()
                    case "cheat":
                        player.score += 90
                        continue
            else:
                self.ai.reset_turn_score()
                player.score -= turn_score
                print (f"❌ Dang it! {player.get_username()} rolled 1. Score will be reset down to {player.score} ❌")
                sleep(2.5)
                break
    
    def reset_game(self, players):
        """Ensures game is reset and has correct players when starting new game"""
        self.game_over = False
        self.npc_score = 0
        self.players = players
        
        return
                   
    def start(self, players, test_mode=False):
        """Decide which player starts first"""
        
        if (self.reset_game(players)):
            who_starts = 0

        if test_mode: 
            return
        
        #Decide who starts in a singleplayer game 
        if len(self.players) == 1: 
            match random.randint(1,2):
                case 1: 
                    self.player_turn(self.players[0])
                    who_starts = 1
                case 2: 
                    self.npc_turn(difficulty)
                    who_starts = 2
                    
            match who_starts:
                case 1:
                    while not self.game_over:
                        print("")
                        self.npc_turn(difficulty)
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
                        self.npc_turn(difficulty)

                
        else:
            match random.randint(1,2):
                case 1: 
                    self.player_turn(self.players[0])
                    current_user_index = 0
                case 2: 
                    self.player_turn(self.players[1])
                    current_user_index = 1

            while not self.game_over:
                if current_user_index == 0:
                    current_user_index = 1
                else:
                    current_user_index = 0
                print("")
                self.player_turn(self.players[current_user_index])
                print("")

    def evaluate(self, value_one, value_two ):
        """Determine if player may continue or not"""
        if value_one == 1 or value_two == 1:
            return False
        return True

    def game_status(self):  
        """Monitor if game is finished or not"""
        return self.game_over
    