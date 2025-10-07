#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class AiLogic:
    
    def __init__(self):
        self.__turn_score = 0
        self.first_start_hand = 0

    def should_roll(self, npc_score, player_score):
        """Determines if AI should roll."""

        self.first_start_hand += 1


        if (npc_score >= 90): #Kommer att kolla så att inte ai stannar närmare än 90+
            return True


        if self.first_start_hand == 1:
            self.__target = 15
            self.__target -= max(min(npc_score // 25, 4), 0) #Denna kommer att börja på 0, sedan efter varje 25 så kommer 1 adderas, så de gör desto nämre Ai'n är
            #desto säkrare kommer den vara, så 25 -1, 50 -2, 75 -3

            diff = npc_score - player_score #Denna kommer kolla ifall motståndaren är långt borta, är de 20+ så läggs 5 på risk, är motståndaren 20 bak, så kommer ai köra säkrare
            if diff >= 20:
                self.__target -= 3
            elif diff <= -20:
                self.__target +=5
        

        if (self.__turn_score < self.__target): #Här väljs det ifall Ai'n ska slå igen eller stanna
            return True
        else:
            self.reset_turn_score()
            return False
        
    def reset_turn_score(self):
        self.__turn_score = 0
        self.first_start_hand = 0


    def increment_turn_score(self, score):
        self.__turn_score+=score
