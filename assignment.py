# -----------------------------------------------------------------------------
# Name:        Number Guessing Game (guessing_game.py)
# Purpose:     A description of your program goes here.
#
# Author:      Lyn Jeong
# Created:     24-Feb-2022
# Updated:     1-Mar-2022
# -----------------------------------------------------------------------------
# I think this project deserves a level 4+ because ...
#
# Features Added:
#   ...
#   ...
#   ...
# -----------------------------------------------------------------------------

import PySimpleGUI as sg
import random

sg.theme('BlueMono')
layout = [[sg.Button('Reset'), sg.Text('x < NUM < y', text_color='white', justification="right", size=(80, 1), key='-NUM-')],
          [sg.Button('Easy'), sg.Button('Medium'), sg.Button('Hard')],
          [sg.Text('input range: '), sg.Text(key='-RANGE-')],
          [sg.Input(key='-IN-', justification='center'), sg.Button('Submit', bind_return_key=True)],
          [sg.Text(key='-MSG-')],
          [sg.Text(key='-RETRY-')],
          [sg.Button('Clear', key='-LEFT-'), sg.Button('Exit')]
          ]

window = sg.Window('Number Guessing Game', layout, element_justification='c')  #, element_justification='c'


def reset():
    global end, mode, counter, userNum, status, min, max, userNumStore  # global int variable that sets the end range of the numbers

    end = 0
    mode = ''
    counter = 0
    userNum = 0
    status = 'start'
    min = 'x'
    max = 'y'
    userNumStore = []


def resetMsg():
    window['-MSG-'].update("")
    window['-RETRY-'].update("")
    window['-RANGE-'].update("")
    window['-LEFT-'].update("Clear")
    window['-IN-'].update('')
    window['-NUM-'].update(f"{min} < NUM < {max}")


def modeSelect():  # sets the mode according to user input
    global end, mode, num
    noSkip = True

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

        else:
            window['-MSG-'].update('Please Select a Mode')
            noSkip = False

        if noSkip:
            window['-RANGE-'].update(f'0 to {end}')
            num = random.randint(0, end)  # Set the number according to the range selected


def compareNum():  # gets user input and compares it to the number chosen
    global userNum, counter, num, status, min, max, userNumStore  # stores user inputted number
    window['-NUM-'].update(f"{min} < NUM < {max}")

    if event == 'Submit':

        if mode == '':
            window['-MSG-'].update('Please Select a Mode')

        else:
            userNum = values['-IN-']  # get the input
            counter += 1  # counts the number of tries

            if not userNum.isnumeric():
                counter -= 1

                if '-' in userNum:
                    window['-MSG-'].update(f"The range is from 0-{end}")

                else:
                    window['-MSG-'].update(text_color='black')
                    window['-MSG-'].update("Please Input a Number")

            else:
                userNum = int(values['-IN-'])

                # Check if the number is out of the range
                if userNum > end:
                    window['-MSG-'].update(f"The range is from 0 - {end}")

                else:
                    # Check if the number is big/small/or the same
                    if userNum > num:
                        window['-MSG-'].update(text_color='brown')
                        window['-MSG-'].update("Try a smaller number!")
                        max = str(userNum)

                    elif userNum < num:
                        window['-MSG-'].update(text_color='red')
                        window['-MSG-'].update("Try a bigger number!")
                        min = str(userNum)

                    else:
                        window['-MSG-'].update(text_color='white')
                        window['-MSG-'].update(f"Congratulations! You guessed the number in {counter} tries")
                        window['-RETRY-'].update("Would you like to replay?")
                        window['-LEFT-'].update("Replay")
                        status = "finished"

                    userNumStore.append(userNum)

                    if len(userNumStore) != len(set(userNumStore)):
                        window['-MSG-'].update(text_color='black')
                        window['-MSG-'].update(f"You have already entered {userNum}")
                        counter -= 1
                        userNumStore.pop(-1)

                    window['-NUM-'].update(f"{min} < NUM < {max}")


def replayGame():   # ask for a replay and replays/ends the game
    global status
    if status == "finished" and event == '-LEFT-':
        reset()
        resetMsg()


def clearField():
    global status
    if status == "start" and event == '-LEFT-':
        window['-IN-'].update('')


def resetGame():
    if event == 'Reset':
        reset()
        resetMsg()


reset()

while True:
    event, values = window.read()

    modeSelect()
    compareNum()
    replayGame()
    clearField()
    resetGame()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
