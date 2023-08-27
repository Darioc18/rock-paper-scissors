# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

print("Welcome to this Rock, Paper, Scissors Game")
player_name = input("Insert your name: ")
# games_number = input("How many games? ")


def get_player_choice():
    try:
        player_choice = input("Enter your choice ('r' for rock, 'p' for paper, 's' for scissors): ").lower()
        if player_choice not in ['r', 'p', 's']:
            raise ValueError(f"You entered '{player_choice}'. Choose 'r' for rock, 'p' for paper, 's' for scissors")
        choice_mapping = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
        print(f"Your choice: {choice_mapping[player_choice]}")
        return player_choice
    except ValueError as e:
        print(f"Invalid data: {e}.\n Please try again.\n")
                


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    print(f"Computer choice: {computer_choice.capitalize()}")
    return computer_choice



def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("It's a tie!")
        return "It's a tie!"
    elif (player_choice == "r" and computer_choice == "s"):
        print("You win!")
        return "You win!"
    elif (player_choice == "p" and computer_choice == "r"):
        print("You win!")
        return "You win!"
    elif (player_choice == "s" and computer_choice == "p"):
        print("You win!")
        return "You win!"
    else:
        print("Computer wins!")
        return "Computer wins!"



def main():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    determine_winner(player_choice, computer_choice)
    

main()
