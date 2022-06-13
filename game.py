# To stimulate the computer choices import random.
import random

# initialize counter
player_score = 0
cpu_score = 0
while True:

    # Take user input
    # while True:
    userAction = (input("Enter a choice (Rock, Paper, Scissors):\n").title())
    # while True:
    if not userAction:
        print("Choice cannot be empty or have wrong input, please enter valid choice")
        break

    print("\n...Computer's turn...")
    print("...waiting...")
    print("...Computer has choosen...")


    # Computer choose an action
    possibleActions = ["Rock", "Paper", "Scissors"]
    computerAction = random.choice(possibleActions)

    # prints the user choice and the computer choice
    print (f"\nPlayer chose {userAction} : CPU chose {computerAction}.\n")

    # Determiner a win, a tie or a loss
    if userAction == computerAction:
        print(f"Both players selected {userAction}. It's a tie!")

    elif userAction == "Rock":
        if computerAction == "Scissors":
            print("Rock smashes Scissors! Ta-da! You win!!!")
            player_score +=1
        else:
            print("Paper covers Rock! Uh-Uh You lose and Computer wins!")
            cpu_score += 1

    elif userAction == "Paper":
        if computerAction == "Rock":
            print("Paper covers Rock! Ta-da! You win!!!")
            player_score +=1
        else:
            print("Scissors cuts Paper! Uh-Uh You lose and Computer wins!")
            cpu_score += 1

    elif userAction == "Scissors":
        if computerAction == "Paper":
            print("Scissors cuts Paper! Ta-da! You win!!!")
            player_score +=1
        else:
            print("Rock smashes Scissors! Uh-Uh You lose and Computer wins!")
            cpu_score += 1

    print(f"\nFinal Score: \n   PLAYER: {player_score} \n   CPU: {cpu_score}\n")
    # Choose to play again and avoid continuous play
    playAgain = input("Play Again? (y or n):\n")
    if playAgain.lower() != "y":
       break
    # else:
    #     print(f"\nFinal Score: \n   PLAYER: {player_score} \n   CPU: {cpu_score}\n")
