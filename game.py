# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 21:47:01 2020

@author: Marek
"""

import os

import random

def razzle_throw():
    score = 0
    dice = 0
    while dice < 8:
        dice += 1 
        score += random.randint(1, 6)
    else:
        return score

input("Press ENTER to open RAZZLE DAZZLE BOARD")
#os.system('img001.png')
print("""Hello! Wanna play a game of RAZZLE DAZZLE? Here are the rules:
    Your initial money is 50 dollars.
    I throw 8 dices and sum the dots, and we check the sum on the RAZZLE DAZZLE BOARD. Each throw costs a dollar (at start). 
    You aim to get the prize, which value is 100 dollars!
    The rules are simple; if your number on the razzle board is red, you get the specified number points. 
    If it's black, you get nothing.
    If it's green, the prize value is increased by $100, but its cost in points stays the same. 
    You get the prize if you get up to 100 points.   
    But beware! If you roll 29, your payment doubles!""")
    
  
def razzle_dazzle(my_money=50, throw=0, payment=1, points=0, prize_points=100, prize_value=100):
   green = (18, 38, 19, 37, 36, 21, 35, 20)
   points_5 = (40, 17, 39)
   points_15 = (15, 41)
   points_20 = (14, 42)
   points_30 = (11, 45, 16)
   points_50 = (10, 12, 13, 43, 44, 46)
   points_100 = (8, 48, 9, 47)
   
        
   while my_money > 0:
       input('press ENTER')
       my_money -= payment
       score = razzle_throw()
       throw += 1
       if prize_points <= points:
           print ("Yeah! You won the prize of", prize_value, "dollars for", prize_points, "points collected!")
           points -= prize_points
           my_money += prize_value
       else:
            if score in green:
                prize_value += 100
            elif score in points_5:
                points += 5
                print("Score! 5 points!")
            elif score in points_15:
                points += 15
                print("Score! 15 points!")
            elif score in points_20:
                points += 20
                print("Score! 20 points!")
            elif score in points_30:
                points += 30
                print("Score! 30 points!")
            elif score in points_50:
                points += 50
                print("Score! 50 points, that's 50% more to a reward!")
            elif score in points_100:
                points += 100
                print("Score! 100 points! Amazing!")
            print("throw:", throw,"Score:", score, "Money:", my_money, "Points:", points, "Payment:", payment, "Prize value:", prize_value)
            if score == 29:
                payment = payment*2
                print('29! Your fee doubles!')

   else:
       return print('You are broke!')


razzle_dazzle()
input("Press ENTER to exit")      
      
      
      
   
