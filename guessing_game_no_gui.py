import random

end = 20        # global int variable that sets the end range of the numbers
counter = 0     # global int variable that counts the number of tries of the player


def modeSelect():   # sets the mode according to user input
    mode = input("select your mode [EASY, MEDIUM, HARD]: ").lower()     # EASY(0-20) | MEDIUM(0-50) | HARD(0-100)
    global end

    if mode != "easy":
        if mode == "medium":
            end = 50
        elif mode == "hard":
            end = 100
        else:
            print("Please input one of the following modes {EASY, MEDIUM, HARD")
            modeSelect()  # Restart the function if the input does not match


def inputNum():     # gets user input and compares it to the number chosen
    global userNum
    userNum = input(f"select a number between 0-{end}: ")
    global counter
    counter += 1

    if not userNum.isnumeric():
        print("Please input a number")
        inputNum()
    else:
        userNum = int(userNum)

    if userNum > end or userNum < 0:   # If the user puts a number out of range, give them a warning
        print(f"The range is from 0-{end}")
        inputNum()
    else:
        if userNum > num:
            print("Try a smaller number!")
            inputNum()
        elif userNum < num:
            print("Try a bigger number!")
            inputNum()
        else:
            print(f"congratulations! You guessed the number in {counter} tries")


def replayGame():
    replay = input("Would you like to play again? [YES, NO]: ").lower()
    if replay == "yes":
        guessingGame()
    elif replay == "no":
        print("Thank you for playing :)")
    else:
        print("Please input YES or NO")
        replayGame()


def guessingGame():
    global num
    global counter

    counter = 0
    modeSelect()                  # Select the mode
    num = random.randint(0, end)  # Set the number according to the range selected
    inputNum()                    # Get a number from the player
    replayGame()                  # Ask if player wants to replay the game


guessingGame()


