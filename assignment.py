# -----------------------------------------------------------------------------
# Name:        Number Guessing Game (guessing_game.py)
# Purpose:     A description of your program goes here.
#
# Author:      Lyn Jeong
# Created:     24-Feb-2022
# Updated:     1-Mar-2022
# -----------------------------------------------------------------------------
# I think this project deserves a level XXXXXX because ...
#
# Features Added:
#   ...
#   ...
#   ...
# -----------------------------------------------------------------------------

import PySimpleGUI as sg
import random

sg.theme('BlueMono')
layout = [[sg.Button('Easy'), sg.Button('Medium'), sg.Button('Hard')],
          [sg.Text('input range: '), sg.Text(size=(15, 1), key='-RANGE-')],
          [sg.Input(key='-IN-'), sg.Button('Submit')],
          [sg.Text(key='-MSG-')],
          [sg.Text(key='-RETRY-')],
          [sg.Button('Clear', key='-LEFT-'), sg.Exit()]
          ]

window = sg.Window('Number Guessing Game', layout)


def reset():
    global end  # global int variable that sets the end range of the numbers
    global mode
    global counter  # global int variable that counts the number of tries of the player
    global userNum
    end = 0
    mode = ''
    counter = 0
    userNum = 0


def modeSelect():  # sets the mode according to user input
    global end, mode, num
    if mode == '':
        if event == 'Easy':
            mode = 'Easy'
            end = 20

        elif event == 'Medium':
            mode = 'Medium'
            end = 50

        elif event == 'Hard':
            mode = 'Hard'
            end = 100

        window['-RANGE-'].update(f'0 to {end}')
        num = random.randint(0, end)  # Set the number according to the range selected


def inputNum():  # gets user input and compares it to the number chosen
    global userNum, counter, num  # stores user inputted number

    if event == 'Submit':
        userNum = values['-IN-']  # get the input
        counter += 1  # counts the number of tries

        if not userNum.isnumeric():
            window['-MSG-'].update("Please Input a Number")
        else:
            userNum = int(values['-IN-'])

            # Check if the number is out of the range
            if userNum > end or userNum < 0:
                window['-MSG-'].update(f"The range is from 0-{end}")

            else:
                # Check if the number is big/small/or the same
                if userNum > num:
                    window['-MSG-'].update("Try a smaller number!")
                elif userNum < num:
                    window['-MSG-'].update("Try a bigger number!")
                else:
                    window['-MSG-'].update(f"Congratulations! You guessed the number in {counter} tries")


'''
def replayGame():   # ask for a replay and replays/ends the game
    replay = input("Would you like to play again? [YES, NO]: ").lower()
    if replay == "yes":
        guessingGame()
    elif replay == "no":
        print("Thank you for playing :)")
    else:
        print("Please input YES or NO")
        replayGame()


def guessingGame():               # The whole game with all the functions in order
    global num
    global counter

    counter = 0
    modeSelect()                  # Select the mode
    num = random.randint(0, end)  # Set the number according to the range selected
    inputNum()                    # Get a number from the player
    replayGame()                  # Ask if player wants to replay the game


guessingGame()                    # Play the Game
'''

reset()
while True:
    event, values = window.read()

    modeSelect()
    inputNum()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
