import random

player_wins = 0
computer_wins = 0
total_rounds = 3
round_count = 0

print("==============================================n\n")
print("Welcome to the game of Rock, Paper, Scissors!\n")
print("==============================================\n")

print("The rules are simple: \n")
print("The goal is to outsmart the computer by selecting the winning choice.\n")
print("Good luck and have fun!\n")

while True:
    player = input("Enter your choice (rock, paper, or scissors): ")
    choice = ["rock", "paper", "scissors"]
    
    if player not in choice: 
        print("Invalid input, Please enter a valid choice.")
        continue 
    
    computer = random.choice(choice)

    print(f"The player chose: {player} and the computer chose: {computer}\n")

    if player == computer:
         print("It's a tie!")
    elif (
         (player == "rock" and computer == "scissors") or 
         (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
        ):
        print("You won!")
        player_wins += 1

    else :
        print("You lose!")
        computer_wins += 1
        
    round_count += 1
    
    if round_count == total_rounds: 
        print("\nEnd of the game!")
        print(f"\nPlayer wins: {player_wins}")
        print(f"\nComputer wins: {computer_wins}")
        
        user_input = input("Do you want to play again? (yes/no): ")

        if user_input not in ["yes", "no"]:
            print("Invalid input, Please enter a valid choice.")
            continue 
        
        if user_input == "no":
            print("Thanks for playing! \o/")
            break
        else:
            print("Let's play again!\n")
            round_count = 0  
            player_wins = 0  
            computer_wins = 0

