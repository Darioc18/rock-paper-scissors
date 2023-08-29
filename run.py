# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os
import random

print("Welcome to Rock, Paper, Scissors Game")
def get_player_name():
     while True:
        try:
            player_name = input("Insert your name: \n")
            if player_name.strip() == "":
                raise ValueError("Please insert a valid name. Avoid using only " +
                                  "spaces or leaving it blank")
            return player_name
        except ValueError as exc:
            print(f"Invalid data: {exc}.\n")    




def get_player_choice(name):
    while True:
        try:
            player_choice = input(f"Hey {name}! Enter your choice ('r' for rock, 'p' for paper, 's' for scissors): \n").lower()
            if player_choice not in ['r', 'p', 's']:
                raise ValueError(f"You entered '{player_choice}'. Choose 'r' for rock, 'p' for paper, 's' for scissors")
            choice_mapping = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
            print(f"Your choice: {choice_mapping[player_choice]}")
            return player_choice
        except ValueError as exc:
            print(f"Invalid data: {exc}.\nPlease try again.\n")
                


def get_computer_choice():
    choices = ["r", "p", "s"]
    computer_choice = random.choice(choices)
    choice_mapping = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    print(f"Computer choice: {choice_mapping[computer_choice].capitalize()}")
    return computer_choice



def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("It's a tie!")
        return "It's a tie!"
    elif (player_choice == "r" and computer_choice == "s") or \
         (player_choice == "p" and computer_choice == "r") or \
         (player_choice == "s" and computer_choice == "p"):
        print("You win!")
        return "You win!"
    else:
        print("Computer wins!")
        return "Computer wins!"

def play_again(name):
    while True:
        play_again = input(f"Hey {name}! Do you want to play again? (y/n): ").lower()                  
        if play_again == "y":
                return True
        elif play_again == "n":            
            print("Thank you for playing!")
            return False
        else:
            print("Invalid input")

def get_max_games(name):
    while True:
        try:
            max_games = int(input(f"How many games do you want to play, {name}? (4, 7, or 10)\n"))
            if max_games not in [4, 7, 10]:
                raise ValueError(f"you entered '{max_games}'. Choose 4, 7, or 10")
            return max_games
        except ValueError as exc:
            print(f"Invalid data: {exc}.\n Please try again.\n")

def main():
    player_name = get_player_name()

    while True:
        os.system('cls||clear')
        score = 0
        max_games = get_max_games(player_name)
        current_round = 0

        while current_round < max_games: 
            player_choice = get_player_choice(player_name)
            computer_choice = get_computer_choice()

            result = determine_winner(player_choice, computer_choice)
            if result == "You win!":
                score += 100
                current_round += 1
                print(f"round {current_round}/{max_games}")
            elif result == "Computer wins!":
                score -= 50
                current_round += 1
                print(f"round {current_round}/{max_games}")
            else:
                current_round += 1 
                print(f"round {current_round}/{max_games}")
            
            if score < 0:
                print(f"Score: 0")
                score = 0
            else:
                print(f"Score: {score}")
            
        print(f"Final score: {score}")

        
        if not play_again(player_name):
            break
                
    

main()
