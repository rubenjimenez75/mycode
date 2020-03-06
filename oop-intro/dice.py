#!/usr/bin/env python3
import random

player1_dice = []
player2_dice = []

for i in range(3): ## number of times it will roll, or run through the loop
    player1_dice.append(random.randint(1,6)) # randint, will roll through integers 1 thru 6
    player2_dice.append(random.randint(1,6))

print("Ruben rolled" + str(player1_dice))
print("Dustin  rolled" + str(player2_dice))

if sum(player1_dice) == sum(player2_dice):
    print("Draw")
elif sum(player1_dice) > sum(player2_dice):
    print("Ruben wins, try again Sucka!!")
else:
    print("Boo!! Dustin wins :(")

