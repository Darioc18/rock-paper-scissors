# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("Welcome to this Rock, Paper, Scissors Game")
player_name = input("Insert your name: ")
# games_number = input("How many games? ")


def get_player_choice():
    while True:
        try:
            player_choice = input("Enter your choice ('r' for rock, 'p' for paper, 's' for scissors): ").strip().lower()
            if player_choice not in ['r', 'p', 's']:
                raise ValueError(f"You entered '{player_choice}'. Choose 'r' for rock, 'p' for paper, 's' for scissors.")
            print(player_choice)
            break
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
                


# def get_computer_choice():

# def determine_winner():

def main():
    get_player_choice()

main()
