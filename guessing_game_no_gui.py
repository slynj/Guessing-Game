import random

end = 20


def modeSelect():   # sets the mode according to user input
    mode = input("select your mode [EASY, MEDIUM, HARD]: ")     # EASY(0-20) | MEDIUM(0-50) | HARD(0-100)
    global end

    if mode != "EASY":
        if mode == "MEDIUM":
            end = 50
        elif mode == "HARD":
            end = 100
        else:
            print("Please input the correct mode in ALL CAPS")
            modeSelect()  # Restart the function if the input does not match


def inputNum():
    global userNum
    userNum = int(input(f"select a number between 0-{end}: "))
    global counter
    counter += 1

    if userNum > end:
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
    replay = input("Would you like to play again?: ")
    if replay == "yes" or "Yes" or "YES":
        guessingGame()
    else:
        print("thank you for playing :)")


def guessingGame():
    global num

    modeSelect()                  # Select the mode
    num = random.randint(0, end)  # Set the number according to the range selected
    inputNum()                    # Get a number from the player
    replayGame()                  # Ask if player wants to replay the game


guessingGame()












