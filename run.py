# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Imports
import os
import random
import ascii_art
import time
import sys
from colorama import Fore, Back, Style
from colorama import init

# Automate colorama color changes reset
# Solution found at https://stackoverflow.com/questions/43649051/a-way-to-not-have-to-reset-the-color-style-in-colorama-every-time
init(autoreset=True)

# Constant to style terminal
R = Fore.RED
LG = Fore.LIGHTGREEN_EX
RESET = Style.RESET_ALL




def get_player_name():
     while True:
        try:
            player_name = input("Insert your name: \n")
            if player_name.strip() == "":
                raise ValueError("Please insert a valid name. Avoid using only"
                                  " spaces or leaving it blank")
            return player_name
        except ValueError as exc:
            print(R + f"Invalid data: {exc}.\n")    




def get_player_choice(name):
    while True:
        try:
            player_choice = input(f"Hey {name}! Enter your choice"
                                  " ('r' for rock, 'p' for paper,"
                                  " 's' for scissors): \n").lower()
            if player_choice not in ['r', 'p', 's']:
                raise ValueError(f"You entered '{player_choice}'."
                                 " Choose 'r' for rock, 'p' for paper,"
                                 " 's' for scissors")
            choice_mapping = {'r': LG +'Rock' + RESET + ascii_art.ROCK, 'p': LG + 'Paper' + RESET + ascii_art.PAPER, 's': LG + 'Scissors'+ RESET + ascii_art.SCISSORS}
            shoot()
            print(f"Your choice: {choice_mapping[player_choice]}")
            return player_choice
        except ValueError as exc:
            print(R + f"Invalid data: {exc}.\nPlease try again.\n")             


def get_computer_choice():
    choices = ["r", "p", "s"]
    computer_choice = random.choice(choices)
    choice_mapping = {'r': LG + 'Rock' + RESET + ascii_art.ROCK, 'p': LG + 'Paper' + RESET + ascii_art.PAPER, 's': LG + 'Scissors' + RESET + ascii_art.SCISSORS}
    print(f"Computer choice: {choice_mapping[computer_choice]}")
    return computer_choice



def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        # print("It's a tie!")
        return "It's a tie!"
    elif (player_choice == "r" and computer_choice == "s") or \
         (player_choice == "p" and computer_choice == "r") or \
         (player_choice == "s" and computer_choice == "p"):
        # print("You win!")
        return "You win!"
    else:
        # print("Computer wins!")
        return "Computer wins!"

def play_again(name):
    while True:
        play_again = input(f"Hey {name}!"
                           " Do you want to play again? (y/n): ").lower()                  
        if play_again == "y":
                return True
        elif play_again == "n":
            return False
        else:
            print("Invalid input")

def get_max_games(name):
    while True:
        try:
            max_games = int(input(f"How many games do you want to play, {name}?"
                                  " 4, 7, or 10?\n"))
            if max_games not in [4, 7, 10]:
                raise ValueError(f"you entered '{max_games}'."
                                 " Choose 4, 7, or 10")
            return max_games
        except ValueError as exc:
            print(R + f"Invalid data: {exc}.\nPlease try again.\n")

def clear_terminal():
    """
    Clears the terminal.
    """
    os.system('cls||clear')

def instructions():
    clear_terminal()
    print(ascii_art.INSTRUCTIONS)
    print("\n• PLAYER vs COMPUTER:\n  You will be playing against the computer.\n"

    "\n• OPTIONS:\n  Choose one of three options: Rock, Paper," 
    " or Scissors.\n"

    "\n• RULES:\n"
    "  Rock beats Scissors (Rock crushes Scissors).\n"
    "  Scissors beats Paper (Scissors cut Paper).\n"
    "  Paper beats Rock (Paper covers Rock).\n"

    "\n• NUMBER OF GAMES:\n  Players can choose to play 4, 7, or 10 games.\n"

    "\n• SCORING:\n"
    "  If you win a game, you earn 100 points.\n"
    "  If you lose a game, you lose 50 points.\n"
    "  If it's a tie, both player and computer get 0 points.\n"

    "\nHave Fun: Rock-paper-scissors is a simple and fun game of chance!\n")
    
def select_instructions():
    print(LG + "1 ► Play")
    print(LG + "2 ► How to play\n")
    while True:
        selection = input("Select an option: \n")
        if selection == "1":
            return 
        elif selection == "2":
            instructions()
            input("Press Enter to return to the game...")
            clear_terminal()
            main()
        else:
            print(R + "Invalid selection")    

def shoot():
    clear_terminal()
    time.sleep(0.2)
    print("\nRock")
    time.sleep(0.8)
    print("Paper")
    time.sleep(0.8)
    print("Scissors\n")
    time.sleep(0.8)
    print("Shoot!")
    time.sleep(0.2)
    typed_text_effect("...\n", 0.5)
    time.sleep(0.2)

def typed_text_effect(string, sleep):
    for letter in string:
        time.sleep(sleep)
        sys.stdout.write(letter)
        sys.stdout.flush()
...     

        

def main():
    print(LG + ascii_art.TITLE)
    print("Welcome to Rock, Paper, Scissors Game\n")

    select_instructions()
    player_name = get_player_name()


    while True:
        clear_terminal()

        print(LG + ascii_art.TITLE)
        
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
                print(f"You won round {current_round}/{max_games}")
            elif result == "Computer wins!":
                score -= 50
                current_round += 1
                print(f"Computer won round {current_round}/{max_games}")                
            else:
                current_round += 1 
                print(f"It's a tie! round {current_round}/{max_games}")                
            
            if score < 0:
                print(LG + f"Score: 0\n")
                score = 0
            else:
                print(LG + f"Score: {score}\n")
            
        print(LG + f"Final score: {score}")

        
        if not play_again(player_name):
            clear_terminal()
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()