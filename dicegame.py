"""
    Question:
    Write a program to design a Dice game. There should be two players. 
    Ask the users to enter their names and roll the dice(four times each). 
    Display the scores and calculate the final score and print the name of the winner.
    
"""


import random     # for random function
import time     # for pauses during dice roll
class Player:   # Class for player
    score=0
    name=""
    def __init__(self,name):
        self.name=name
    
print("Enter name of player 1:")
name = input()
player1 = Player(name)        

print("Enter name of player 2:")
name = input()
player2 = Player(name) 

for turn in range(1,5):  #Game Loop    
    print("******** Round {} **********".format(turn))   
    print("{} is rolling".format(player1.name))
    time.sleep(1)
    score = random.randint(1,6) # finds random value between 1 and 6
    print("{} got {}".format(player1.name,score))
    player1.score+=score
    print("{} is rolling".format(player2.name))
    time.sleep(1)
    score = random.randint(1,6)
    print("{} got {}".format(player2.name,score))
    player2.score+=score

print("****** Total Score ********")
print("{} : {}".format(player1.name,player1.score))
print("{} : {}".format(player2.name,player2.score))
if(player1.score>player2.score):
    print(player1.name + " wins!")
else:
    print(player2.name + " wins!")