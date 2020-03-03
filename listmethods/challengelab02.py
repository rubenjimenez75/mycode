#!/usr/bin/env python3
col_list= ["blue", "Columbus"]

user_input = input("What is your name?")

col_list.append(1492) #this line will add 1492
col_list.append(user_input) #this line will append user input to col_list
print(f"In {col_list[2]}, {col_list[1]} sailed the ocean blue. {col_list[2]} fell off the boat.")
