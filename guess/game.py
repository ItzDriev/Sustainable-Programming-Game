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
        self.npc_hand = DiceHand()

        self.dice_hand = DiceHand()
        
        self.game_over = False
        
    def npc_turn(self):
        
        """Npc takes turn, sends result to the intelligence class."""
        turn_score = 0
        turn_history = "----------Turn History For: Computer-AI----------\n"

        while True:
            for i in range(40):
                print("")
            print(turn_history)
            player_score = self.players[0].score
            
            if self.ai.should_roll(self.npc_score, player_score):
                self.npc_hand.roll_dice()
                value = self.npc_hand.get_last_roll()
                print (f"Mr AI rolled {value}")
            else:
                break

            if self.evaluate(value):
                self.npc_score += value
                turn_score+= value
                self.ai.increment_turn_score(value)

                if (self.npc_score >= 100):
                    print ("Mr AI reached 100 points. Game over")
                    self.game_over = True
                    self.ai.reset_turn_score()
                    break

                
                print (f"Mr AI's total score: {self.npc_score}")
                turn_history+=f"Rolled: {self.npc_hand.get_last_roll()}\n"
                sleep(1)
                continue  # Placeholder for continue-logic

            else:
                self.ai.reset_turn_score()
                self.npc_score -= turn_score
                print (f"Mr AI rolled 1. His score will be reset down to {self.npc_score}")
                sleep(2.5)
                break
                  
    def player_turn(self, player):

        
        """Player(s) takes turn rolling dice"""

        if self.game_over:
            return
        
        turn_score = 0
        turn_history = f"----------Turn History For: {player.get_username()}----------\n"

        while True: 
            for i in range(40):
                print("")
            print(turn_history)

            self.dice_hand.roll_dice()
            value = self.dice_hand.get_last_roll()
            print (f"{player.get_username()} rolled {value}")
            
            if (self.evaluate(value)):
                player.score += value
                turn_score += value
                if  player.score >= 100:
                    print (f"{player.get_username()} reached 100 points. {player.get_username()} wins!")
                    self.game_over = True
                    break
                    
                option = input (f"{player.get_username()}'s Total score: {player.score} \n\nContinue? y/n: ")
                turn_history+=f"Rolled: {self.dice_hand.get_last_roll()}\n"
                match option:
                    case "y":
                        continue
                    case "n":
                        break
                    case "cheat":
                        player.score += 90
                        continue
            else:
                player.score -= turn_score
                print (f"Dang it! {player.get_username()} rolled 1. Score will be reset down to {player.score}")
                sleep(2.5)
                break
                
    def start(self, players, test_mode=False):
        """Decide which player starts first"""
        #Temporary Score Reset for when game ends so a new game can be started, propert method for this will be implemented later
        self.game_over = False
        self.npc_score=0
        
        self.players=players
        who_starts = 0

        if test_mode: return

        if len(self.players) == 1: 
            match random.randint(1,2):
                case 1: 
                    self.player_turn(self.players[0])
                    who_starts = 1
                case 2: 
                    self.npc_turn()
                    who_starts = 2

            
            match who_starts:
                case 1:
                    while not self.game_over:
                        print("")
                        self.npc_turn()
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
                        self.npc_turn()

                
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



        
            
    def evaluate(self, value, ):
        
        """Determine if player may continue or not"""
        if value == 1:
            return False
        else: 
            return True
    
    def game_status(self):
        
        """Monitor if game is finished or not"""
        return self.game_over
        
    