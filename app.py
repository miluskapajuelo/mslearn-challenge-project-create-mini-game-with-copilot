import sys
import random

# Check the number of command-line arguments
""" if len(sys.argv) > 1:
    # Access the first command-line argument (index 0 is the script name)
    option = sys.argv[1]
    print("Write one option to start he game, options: rock, paper, or scissors: ", option)
else:
    print("No command-line argument provided.")
 """
def game():
    choices = ["rock", "paper", "scissors"]
    user_counter = 0
    computer_counter = 0
    rounds = 0

   
    

    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        if user_choice not in choices:
            print("the option entered is invalid")
            break 
    
        computer_choice = random.choices(choices)[0]
        print(f"You chose {user_choice}.")
        print(f"The computer chose {computer_choice}.")
        rounds+= 1

        if user_choice == computer_choice:
            print("It's a tie!")
        elif(
            (user_choice == "rock" and computer_choice=="scissors") or
            (user_choice == "scissors" and computer_choice=="paper") or 
            (user_choice == "paper" and computer_choice=="rock")   
            ):
            user_counter+= 1
            print("you win!")
        else:
            print("you lost")
            computer_counter+= 1
    
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("you number of win games is: ", user_counter )
            print("you number rounds was: ", rounds )
            computer_choice = 0
            user_choice = 0
            break
            
   
game()

