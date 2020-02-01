#!/usr/bin/python3
# -*-coding:UTF-8 -*

# Creating a roulette casino program

from math import ceil
from random import randrange

# Starting with a variable stack -> stackplayer
stack = 1000

# Starting a variable wich value == True while game is on -> game_on = True
continue_game = True

# print a welcome and recapitulatory message => print("Welcome to the table, your stack is ", stack," $")
print("Welcome to the table, your stack is ", stack," $")
# Strating the general game loop
while continue_game:

# Phase 1: (Choose a number)
# Starting loop => while variable < 0 and variable > 49
# Initialize variable 
# The player choose a number beetween 0 and 49 => variable = input("")
# Init a Try block to test if the variable is an int
# Check if variable is an integer => variable = int(variable)
# if its not then throw an exception and continue (Wich mean that we go back on the start of the loop again)
# Else, check if the number is beetween 0 and 49 => if variable >0 and <= 49
    cNumber = -1
    while cNumber < 0 or cNumber > 49:
        
        cNumber = input("Choose a number beetween 0 and 49 :")
        try:
            cNumber = int(cNumber)
        except ValueError:
            print("NAN : Not A Number !")
            cNumber = -1
            continue
        # if cNumber < 0 or Cnumber > 49:
        #     print("Your number is out of range, try again !")
        if cNumber < 0:
            print("Ce nombre est négatif")
        if cNumber > 49:
            print("Ce nombre est supérieur à 49")


# Phase 2: (Choose a bet)
# Initialize bet variable => bet = -1
# Initialize the loop => while bet <= 0 and bet > stack
# The player choose a bet => bet = input("")
# Init a Try bloc to test if the variable is int
# Check if bet is an integer => bet = int(bet)
# if its not throw an exception => Throw exception then continue(continue for go back on start of the loop)
# Else, check if the number is is better than 0 and lower than stack => if bet > 0 and bet < stack
# stack -= bet

    bet = 0
    while bet <= 0 or bet > stack:
        bet = input("Choose a bet : ")
        try:
            bet = int(bet)
        except ValueError:
            print("NAN : Not A Number !")
            bet = -1
            continue
        if bet <= 0 or bet > stack:
            print("Invalid bet: your bet have to be superior than 0 and lower than your stack !")


# Phase 3: (Determine the winning number)
# Wnumber = Wnumber.randrange(0, 49)
# Print a message : print("The roulette is rolling ... and the winning number is ...", Wnumber)

    Wnumber = randrange(0, 50)
    print("The roulette is rolling ... and the winning number is ...", Wnumber)

# Phase 4: (Allocation of winnings)

# if: choosen number match with Wnumber then : stack += bet * 3
# elif: choosen number and Wnumber have the same color: if Wnumber % 2 == variable % 2 (This is the same color) 
# then: stack += ceil(bet/2)
# else: stack -= bet

    if cNumber == Wnumber:
        stack += bet * 3
        print("Perfect match : You win ", bet * 3, " $ !!! Your stack is now : ",stack," $")
    elif cNumber % 2 == Wnumber % 2:
        stack += ceil(bet / 2)
        print("Correct color : You win ", ceil(bet / 2), " $ !!! Your stack is now : ",stack," $")
    else:
        stack -= bet
        print("You loose your bet. Your stack is now : ", stack, " $")
        
# Phase 5: (Check global parameters of the game)
# if stack <= 0:
# print("Vous n'avez plus d'argent pour miser, le jeux s'arrete !!")
# Global variable = False
# else:
#print("Vous avez a present ",stack," $")
# Ask player if he want to leave with is earnings => leave = input("Do you want to leave the game ? press "Q" for leaving or press any other letter)
# Put the variable leave in minus => leave = leave.lower()
# If input == "q": 
# print("You leave the game, Bye :)")
# then exit the game => global variable = False


    if stack <= 0:
        print("You have no more money. Game Over !")
        continue_game = False
    else:
        leave = input("Do you want to continue ? Y/N ")
        leave = leave.lower()
        if leave == "n":
            print("See you next time ! :)")
            continue_game = False




