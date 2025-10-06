#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module defines a game module in which the game is initialized from"""

import random
from guess import dice_hand

class Game:
    """Represents the game object"""
    
    def __init__(self, players_array = ["johan","niklas"], leaderboard = None):
        
        """Initialize the game object, player and npc resources"""
        self.players = {}

        for player in players_array:
            self.players[player] = {"Score" : 0, "Hand" : dice_hand.DiceHand()}
         
        self.npc_score = 0
        self.npc_hand = dice_hand.DiceHand()
        
        self.game_over = False
        
    def npc_turn(self):
        
        """Npc takes turn, sends result to the intelligence class."""
        while True:
            
            self.npc_hand.roll_dice()
            value = self.npc_hand.get_last_roll()
            print (f"Mr AI rolled {value}")

            if self.evaluate(value):
                self.npc_score += value

                if (self.npc_score >= 100):
                    print ("Mr AI reached 100 points. Game over")
                    self.game_over = True
                    break

                print (f"Mr AI's total score: {self.npc_score}")
                continue  # Placeholder for continue-logic

            else:
                self.npc_score = 0
                print ("Mr AI rolled 1. His score will be reset.")
                break
                  
    def player_turn(self):
        
        """Player(s) takes turn rolling dice"""
        for player, item in self.players.items():
            if self.game_over:
                break

            while True: 
                item["Hand"].roll_dice()
                value = item["Hand"].get_last_roll()
                print (f"{player} rolled {value}")
                
                if (self.evaluate(value)):
                    item["Score"] += value
                    
                    if item["Score"] >= 100:
                        print (f"{player} reached 100 points. {player} wins!")
                        self.game_over = True
                        break
                        
                    option = input (f"{player} Total score: {item['Score']} Continue? y/n")
                    
                    match option:
                        case "y":
                            continue
                        case "n":
                            break
                        case "cheat":
                            item["Score"] += 90
                            continue
                else:
                    print (f"Dang it! {player} rolled 1. Score will be reset")
                    item["Score"] = 0
                    break
                
    def start(self):
        
        """Decide which player starts first"""
        match random.randint(1,2):
            case 1: return
            case 2: self.npc_turn()
            
    def evaluate(self, value, ):
        
        """Determine if player may continue or not"""
        if value == 1:
            return False
        else: 
            return True
    
    def game_status(self):
        
        """Monitor if game is finished or not"""
        return self.game_over
        
    