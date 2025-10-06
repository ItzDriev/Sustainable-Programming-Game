#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module defines how the AI thinks"""

npc_score = 0 #Detta är totalt vad AI har
value = 0 # Detta är vad vi fick denna rundan regristrerad
new_round = True # Detta är för att kolla ifall det är en ny runda eller inte
total_value_this_round = 0 #Detta är hur mycket den totala summan är denna rundan
item = 0 # Detta är spelarens totala poäng
win_target = 100 - npc_score #Denna är mest ifall man är nära nog så ska inte ai stanna på 99 eller likande


def ai_logic_for_rolling(npc_score, item, total_value_this_round):
    if (win_target == 10): #Kommer att kolla så att inte ai stannar närmare än 90+
        return True
    

    target -= max(min(npc_score // 25, 4), 0) #Denna kommer att börja på 0, sedan efter varje 25 så kommer 1 adderas, så de gör desto nämre Ai'n är
    #desto säkrare kommer den vara, så 25 -1, 50 -2, 75 -3

    diff = npc_score - item #Denna kommer kolla ifall motståndaren är långt borta, är de 20+ så läggs 5 på risk, är motståndaren 20 bak, så kommer ai köra säkrare
    if diff >= 20:
        target += 5
    elif diff <= -20:
        target -=3
    

    if (total_value_this_round < target): #Här väljs det ifall Ai'n ska slå igen eller stanna
        return True
    else:
        return False


class ai_logic:
    target = 15 # Detta är target som ai'n kommer försöka fokusera på som ändras beroende på motståndarens poäng
    if (new_round==True):
        total_value_this_round = 0
    total_value_this_round += value
    ai_logic_for_rolling(npc_score, item, total_value_this_round)