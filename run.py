# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

print("Welcome to Rock, Paper, Scissors Game")
player_name = input("Insert your name: ")
# games_number = input("How many games? ")


def get_player_choice():
    while True:
        try:
            player_choice = input(f"Hey {player_name}! Enter your choice ('r' for rock, 'p' for paper, 's' for scissors): ").lower()
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
    elif (player_choice == "r" and computer_choice == "scissors") or \
         (player_choice == "p" and computer_choice == "rock") or \
         (player_choice == "s" and computer_choice == "paper"):
        print("You win!")
        return "You win!"
    else:
        print("Computer wins!")
        return "Computer wins!"

def play_again():
    while True:
        play_again = input(f"Hey {player_name}! Do you want to play again? (y/n): ").lower()                  
        if play_again == "y":
                return True
        elif play_again == "n":            
            print("Thank you for playing!")
            return False
        
        # try:
        #     if play_again != "y" and "n":
        #         raise ValueError(f"you entered '{play_again}'. Choose 'y' for yes or 'n' for no")
        #     return play_again
        # except ValueError as e:
        #     print(f"Invalid data: {e}.\n")


def main():
    while True: 
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        determine_winner(player_choice, computer_choice)

        if not play_again():
            break         
    

main()
