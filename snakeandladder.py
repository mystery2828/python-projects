# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:07:56 2019

@author: user
"""
import random
snake ={15:2,29:11,42:9,58:23,75:65,92:3}
ladder = {5:25,13:44,22:74,35:46,47:62,52:84,67:98,72:90,81:95}

def letsplay(snake,ladder):
    pawn_pos = 1
    while pawn_pos<101:
        sumne = input('Press any key and Enter')
        dice = random.randint(1,6)
        print("You rolled {}".format(dice))
        pawn_pos+=dice
        #print("You are at {}".format(pawn_pos))
        if pawn_pos in snake:
            pawn_pos = snake[pawn_pos]
        elif pawn_pos in ladder:
            pawn_pos = ladder[pawn_pos] 
        print("You are at {}".format(pawn_pos))
    return pawn_pos
    
letsplay(snake,ladder)
