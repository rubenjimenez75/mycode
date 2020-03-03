#!/usr/bin/env python

round = 0
answer = " "

while round < 3 and answer != "Brian":
    round +=round 1
    print('Finish the movie title, "Monty Python\'s The Life of _ _ _ _ _"')
    answer = input("Your guess--> ")

    if answer == 'Brian':
        print('Correct')
        break

    elif round==3:
        print("Sorry, the answer was Brian.")
        break

    else:
        print("Sorry! Try again!")
