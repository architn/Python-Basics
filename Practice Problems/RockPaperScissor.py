import random as rand

print("Welcome to Rock, Paper, Scissors Game")
print("Rules of the game:")
print("User plays against computer. User has to enter either of the choices: Rock, Paper or Scissor")
userName = input("Enter your name!\n")


def RockPaperScissorGame(userScore, computerScore):
    options = ["Rock", "Paper", "Scissors"]
    isUserPlayingRockPaperScissors = True

    while isUserPlayingRockPaperScissors:
        userChoice = input("Choose among one of Rock, Paper, Scissor. Press Q to Quit the game\n")
        computerChoice = rand.choice(options)

        if userChoice.lower() == "rock" and computerChoice.lower() == "paper":
            print("Computer wins this round!")
            computerScore = computerScore + 1
            print("User Score is: {}\nComputer Score is: {}".format(userScore, computerScore))
            RockPaperScissorGame(userScore, computerScore)

        elif userChoice.lower() == "rock" and (computerChoice.lower() == "scissors" or computerChoice.lower() == "scissor"):
            print("User wins this round!")
            userScore = userScore + 1
            print("User Score is: {}\nComputer Score is: {}".format(userScore, computerScore))
            RockPaperScissorGame(userScore, computerScore)

        elif userChoice.lower() == "paper" and (computerChoice.lower() == "scissors" or computerChoice.lower() == "scissor"):
            print("Computer wins this round!")
            computerScore = computerScore + 1
            print("User Score is: {}\nComputer Score is: {}".format(userScore, computerScore))
            RockPaperScissorGame(userScore, computerScore)

        elif userChoice.lower() == "paper" and computerChoice.lower() == "rock":
            print("User wins this round!")
            userScore = userScore + 1
            print("User Score is: {}\nComputer Score is: {}".format(userScore, computerScore))
            RockPaperScissorGame(userScore, computerScore)

        elif (computerChoice.lower() == "scissors" or computerChoice.lower() == "scissor") and computerChoice.lower() == "rock":
            print("Computer wins this round!")
            computerScore = computerScore + 1
            print("User Score is: {}\nComputer Score is: {}".format(userScore, computerScore))
            RockPaperScissorGame(userScore, computerScore)

        elif(computerChoice.lower() == "scissors" or computerChoice.lower() == "scissor") and computerChoice.lower() == "paper":
            print("User wins this round!")
            userScore = userScore + 1
            print("User Score is: {}\nComputer Score is: {}".format(userScore, computerScore))
            RockPaperScissorGame(userScore, computerScore)

        elif userChoice.lower() == computerChoice.lower():
            print("User and Computer both chose " + userChoice + ". Nobody wins this round")
            print("User Score is: {}\nComputer Score is: {}".format(userScore, computerScore))
            RockPaperScissorGame(userScore, computerScore)

        elif userChoice.lower() == "q":
            print("User has chosen to end the game.\nFinal Score -\n{}:{}\nComputer: {}".format(userName, userScore, computerScore))
            if userScore == computerScore:
                print("User and Computer have the same score! Its a draw")

            elif userScore > computerScore:
                print("User Wins!")

            else:
                print("Computer is the Winner. Sorry "+userName+"!")
            isUserPlayingRockPaperScissors = False
            exit(0)

        else:
            print("Invalid Combination. Select again")
            print(userChoice)
            print(computerChoice)
            RockPaperScissorGame(userScore, computerScore)


RockPaperScissorGame(0, 0)
