#!/usr/bin/env python3
import random

__author__ = "Tims Guynes"
__version__ = "0.1.0"

#receive input from player
play_selection = input("What do you pick today, Rock? Paper? Scissor? ")
#input must be rock, paper, or scissor


#error message if value is not any of these

#computer will randomly select one of the options
rps_list = ['rock', 'scissor', 'paper']
computer_selection = random.choice(rps_list)
#compare between user input and computer selection

def who_wins(play_selection):
    player_choise = play_selection.lower()

    '''if(play_selection.lower() == ("scissor") or play_selection.lower() == ("rock") or play_selection.lower() == ("paper")):
        print("yes, that's it")
    else:
        print("Wrong selection, try again")
    '''
    #if player selection == computer selection results in a tie
          
    #if player selection == scissor && comptuer selection == rock, player loses
    if player_choise == "scissor" and computer_selection == "rock":
        #print("Player chose " + player_choise + " " + "Computer chose " + computer_selection)
        return "Player, you lose"
    #if player selection == scissor && computer selection == paper, player wins
    elif player_choise == "scissor" and computer_selection == "paper":
        #print("Player chose " + player_choise + " " + "Computer chose " + computer_selection)
        return "Player, you win"
    #if player selection == paper && computer selection == scissor, player loses
    elif player_choise == "paper" and computer_selection == "scissor":
        #print("Player chose " + player_choise + " " + "Computer chose " + computer_selection)
        return "Player, you lose"
    #if player selection == paper && computer selection == rock, player wins
    elif player_choise == "paper" and computer_selection == "rock":
        #print("Player chose " + player_choise + " " + "Computer chose " + computer_selection)
        return "Player, you win"
    #if player selection == rock && computer selection == paper, player loses
    elif player_choise == "rock" and computer_selection == "paper":
        #print("Player chose " + player_choise + " " + "Computer chose " + computer_selection)
        return "Player, you lose"
    #if player selection == rock && computer selection == scissor, player wins
    elif player_choise == "rock" and computer_selection == "scissor":
        #print("Player chose " + player_choise + " " + "Computer chose " + computer_selection)
        return "Player, you win"
    elif player_choise == computer_selection:
        #print("Player chose " + player_choise + " " + "Computer chose " + computer_selection)
        return "It's a tie, Try again"  
    else:
        return "wrong selection type try again"

if __name__ == '__main__':
    print(who_wins(play_selection))
