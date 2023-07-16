# Rock-Paper-Scissors by Vaidas Razgaitis
import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Choose <rock/paper/scissors>: ").lower()
    computer_choice = random.choice(choices)

    # error check on user input string
    while user_choice not in choices:
        user_choice = input("Please input only <rock/paper/scissors>: ").lower()
    
    # Outcome: USER VICTORY 
    if user_choice == "rock" and computer_choice == "scissors":
        print(f'the computer chose {computer_choice}. You win!')
    elif user_choice == "scissors" and computer_choice == "paper":
        print(f'the computer chose {computer_choice}. You win!')
    elif user_choice == "paper" and computer_choice == "rock":
        print(f'the computer chose {computer_choice}. You win!')

    # Outcome: COMPUTER VICTORY
    elif computer_choice == "rock" and user_choice == "scissors":
        print(f'the computer chose {computer_choice}. The computer wins :(')
    elif computer_choice == "scissors" and user_choice == "paper":
        print(f'the computer chose {computer_choice}. The computer wins :(')
    elif computer_choice == "paper" and user_choice == "rock":
        print(f'the computer chose {computer_choice}. The computer wins :(')

    # Outcome: TIE
    elif user_choice == computer_choice:
        print(f"Computer also chose {computer_choice}. Let's settle this.")
        # recursively call the funciton to play again
        rock_paper_scissors()

def play_again():
    choice = input("Would you like to play again? <y/n> ").lower()
    return choice == "y"

while True:
    rock_paper_scissors()
    if not play_again():
        print('\nThanks for playing.\n')
        break
    