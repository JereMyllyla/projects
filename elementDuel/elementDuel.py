# The program is a more complex version of the rock-paper-scissors game. The game involves five elements, each with 2 strengths and 2 weaknesses.
## The computer randomly selects one element, after which the player also chooses one element.
## The program compares the choices and determines the round result (win/loss/draw), then calculates the life points for the players.
## The game continues until one of the players wins 5 rounds.
# By: Jere Myllylä, 2022

from random import randint

# Define the options used in the game, i.e., the elements.
options = ["Lightning", "Wind", "Water", "Earth", "Fire"]

# Defines the life points for the players.
playerLife = 5
computerLife = 5

# Defines the game as being in progress.
gameStatus = "on"
roundResult = "tie"
# The code that runs the game.
## Stay in the while loop as long as the game is in progress.
while gameStatus == "on":
## Randomly select an element for the computer for the next round.
    computerChoice = options[randint(0,4)]
    #FOR TESTING! Display the computer's choice to the player before their own selection. Enable by deleting the '#' from next line.
    #print(computerChoice)
## Display the life points for both players to the user.
    print(f"Player HP: {playerLife}")
    print(f"Opponent HP: {computerLife}")
## The user chooses an element for the round.    
    print("Choose your element for this round:")    
    i = 1
    for element in options:
        print(f"{i}: {element}")
        i += 1
## The try-except block prevents the user from entering incorrect input.         
    try:
        playerChoice = int(input())
        if playerChoice == 1:
            playerChoice = options[0]
        elif playerChoice == 2:
            playerChoice = options[1]
        elif playerChoice == 3:
            playerChoice = options[2]
        elif playerChoice == 4:
            playerChoice = options[3]        
        elif playerChoice == 5:
            playerChoice = options[4]
        else:
            print("Choose a number between 1-5!")
## If the computer and the user have the same element
        if playerChoice == computerChoice:
            roundResult = "tie"
## Define the actions for the elements when the computer and the user make different choices.
        elif playerChoice == "Lightning":
### If the computer's element is weak to the user's element, the user wins.
### Inform the user about the computer's chosen element.
            if computerChoice == "Wind" or computerChoice == "Water":
                print(f"Your opponent chose {computerChoice}. You win this round!")
                roundResult = "win"
### If the computer's element is strong against the user's element, the user loses.               
            else:
                print(f"Your opponent chose {computerChoice}. You lose this round!")
                roundResult == "lose"    
            
        elif playerChoice == "Wind":
            if computerChoice == "Earth" or computerChoice == "Water":
                print(f"Your opponent chose {computerChoice}. You win this round!")
                roundResult = "win"
            else:
                print(f"Your opponent chose {computerChoice}. You lose this round!")
                roundResult == "lose"    

        elif playerChoice == "Water":
            if computerChoice == "Earth" or computerChoice == "Fire":
                print(f"Your opponent chose {computerChoice}. You win this round!")
                roundResult = "win"
            else:
                print(f"Your opponent chose {computerChoice}. You lose this round!")
                roundResult == "lose"

        elif playerChoice == "Earth":
            if computerChoice  == "Lightning" or computerChoice == "Fire":
                print(f"Your opponent chose {computerChoice}. You win this round!")
                roundResult = "win"
            else:
                print(f"Your opponent chose {computerChoice}. You lose this round!")
                roundResult == "lose"      

        elif playerChoice == "Fire":
            if computerChoice  == "Wind" or computerChoice == "Lightning":
                print(f"Your opponent chose {computerChoice}. You win this round!")
                roundResult = "win"
            else:
                print(f"Your opponent chose {computerChoice}. You lose this round!")
                roundResult == "lose"  

## Define the actions for different round results (win/draw/loss).
### If the user wins, deduct 1 life point from the computer.
        if roundResult == "win":
            computerLife -= 1
### In a draw, nothing happens.            
        elif roundResult == "tie":
            print (f"You both chose {playerChoice}! It's a tie!")
### If the user loses, deduct one life point from them.               
        else:
            playerLife -=1

## Define the end state of the game.
### If the life points of the user or the computer drop to zero, inform the user of the game's outcome.               
        if playerLife < 1:
            print("You have lost the duel!")
### Ask if the user wants to play again. Input starting with the letter 'Y' restarts the game; any other input ends the game.            
            finish = input("Would you like to play again? (y/n): ")
            finish = finish.lower()
            finish = finish.startswith("y")
            if finish == True:
                playerLife = 5
                computerLife = 5
                gameStatus = "on"
            else:
                print("Thank you for playing!")
                gameStatus = "done"
        elif computerLife < 1:
            print("Congratulations, you have won the duel!")
            finish = input("Would you like to play again? (y/n): ")
            finish = finish.lower()
            finish = finish.startswith("y")
            if finish == True:
                playerLife = 5
                computerLife = 5
                gameStatus = "on"
            else:
                print("Thank you for playing!")
                gameStatus = "done"  
## Prompt the user to use the correct input.
    except ValueError:
        print("Choose a number between 1-5!")   
## Reset the round result.                      
    roundResult = "none"            