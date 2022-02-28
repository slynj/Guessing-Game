# -----------------------------------------------------------------------------
# Name:        Number Guessing Game (guessing_game.py)
# Purpose:     A description of your program goes here.
#
# Author:      Lyn Jeong
# Created:     24-Feb-2022
# Updated:     1-Mar-2022
# -----------------------------------------------------------------------------
# I think this project deserves a level 4+ because I met all the expectation and
# also challenged my self to add different features to the original guessing game.
# I further on added a graphic user interface using PySimpleGUI.
#
# Features Added:
#   1) Graphic Interface
#   2) Mode Selection
#   3) Counts 'How many tries it took'
#   4) Detects Non-Numeric Inputs
#   5) Detects Numbers That Has Already Been Inputted
#   6) Detects if the Input is Below/Above Selected Range
#   7) Displays the Range of What the Number Could be (x < NUM < Y)
#   8) Reset Button
#   9) Clear Button
#  10) Exit Button
# -----------------------------------------------------------------------------

# import systems needed
import PySimpleGUI as sg
import random

sg.theme('BlueMono')  # Blue Theme of the Window
layout = [
    [sg.Button('Reset'), sg.Text('x < NUM < y', text_color='white', justification="right", size=(80, 1), key='-NUM-')],
    [sg.Button('Easy'), sg.Button('Medium'), sg.Button('Hard')],
    [sg.Text('input range: '), sg.Text(key='-RANGE-')],
    [sg.Input(key='-IN-', justification='center'), sg.Button('Submit', bind_return_key=True)],
    [sg.Text(key='-MSG-')],
    [sg.Text(key='-RETRY-')],
    [sg.Button('Clear', key='-LEFT-'), sg.Button('Exit')]
]  # Layout of the Window by Row

# Draws the Window
window = sg.Window('Number Guessing Game', layout, element_justification='c')


# Resets all the variable values
def reset():
    global end, mode, counter, userNum, status, min, max, userNumStore

    end = 0           # Sets the end range of the number
    mode = ''         # Mode (easy, medium, hard)
    counter = 0       # Counts the tries
    userNum = 0       # Player's number inputted
    status = 'start'  # Current status of the game (start, finish)
    min = 'x'         # Smallest value the user guessed (indicates that the number is greater than this value)
    max = 'y'         # Largest value the user guessed (indicates that the number is greater than this value)
    userNumStore = [] # Stores user's guesses


# Resets all the text of the window
def resetMsg():
    window['-MSG-'].update("")        # Updates the message section to BLANK
    window['-RETRY-'].update("")      # Updates the retry section to BLANK
    window['-RANGE-'].update("")      # Updates the range section to BLANK
    window['-LEFT-'].update("Clear")  # Changes back to 'Clear' button from 'Replay' Button
    window['-IN-'].update('')         # Updates input box to BLANK
    window['-NUM-'].update(f"{min} < NUM < {max}")  # Resets to x < NUM < y


# Sets the mode according to the button pressed
def modeSelect():
    global end, mode, num
    noSkip = True  # Stores if the user has started the game without selecting the mode

    # If mode is blank,
    if mode == '':
        # If button is easy, range is 20
        if event == 'Easy':
            mode = 'Easy'
            end = 20

        # If button is medium, range is 50
        elif event == 'Medium':
            mode = 'Medium'
            end = 50

        # If button is hard, range is 100
        elif event == 'Hard':
            mode = 'Hard'
            end = 100

        # if they did not select the mode, notify them through MSG section
        else:
            window['-MSG-'].update('Please Select a Mode')
            noSkip = False

        # if they have selected a mode,
        if noSkip:
            window['-RANGE-'].update(f'0 to {end}')  # display the range
            num = random.randint(0, end)  # and set the number according to the range selected


# Gets user input and compares it to the number chosen
def compareNum():
    global userNum, counter, num, status, min, max, userNumStore
    window['-NUM-'].update(f"{min} < NUM < {max}")

    # If the user pressed the button Submit,
    if event == 'Submit':

        # But if the mode is blank, notify them
        if mode == '':
            window['-MSG-'].update(text_color='black')      # Set text colour to black
            window['-MSG-'].update('Please Select a Mode')  # Notify Player

        else:
            userNum = values['-IN-']  # stores from the input box
            counter += 1  # counts the number of tries

            # if the input is not a number
            if not userNum.isnumeric():
                # cancel the count
                counter -= 1

                # Clear the input field
                window['-IN-'].update('')

                # Set text colour to black
                window['-MSG-'].update(text_color='black')

                # if a number is negative, notify the range
                if '-' in userNum:
                    window['-MSG-'].update(f"The range is from 0-{end}")  # notify the player

                else:
                    window['-MSG-'].update("Please Input a Number")  # notify the player

            else:
                userNum = int(values['-IN-'])  # convert their input to a integer

                # Check if the number is out of the range
                if userNum > end:
                    counter -= 1                # Cancel counter
                    window['-IN-'].update('')   # Clear the input field
                    window['-MSG-'].update(text_color='black')
                    window['-MSG-'].update(f"The range is from 0 - {end}")

                # Check if the number is big/small/or the same
                else:
                    # if it is bigger,
                    if userNum > num:
                        window['-MSG-'].update(text_color='brown')       # change the text colour to brown
                        window['-MSG-'].update("Try a smaller number!")  # notify the player
                        max = str(userNum)  # update max num

                    # if it is smaller,
                    elif userNum < num:
                        window['-MSG-'].update(text_color='red')        # change the text colour to red
                        window['-MSG-'].update("Try a bigger number!")  # notify the player
                        min = str(userNum)  # update min num

                    # if it is equal,
                    else:
                        window['-MSG-'].update(text_color='white')
                        window['-MSG-'].update(f"Congratulations! You guessed the number in {counter} tries")
                        window['-RETRY-'].update(
                            "Would you like to replay?")   # notify the player and ask if they want to replay
                        window['-LEFT-'].update("Replay")  # update the clear button to appear as a replay button
                        status = "finished"                # update the status

                    # Clear the input field
                    window['-IN-'].update('')

                    # Add the user number in the list to record their number
                    userNumStore.append(userNum)

                    # if there are duplicate number in the stored list,
                    if len(userNumStore) != len(set(userNumStore)):
                        window['-MSG-'].update(text_color='black')  # change text colour
                        window['-MSG-'].update(f"You have already entered {userNum}")  # notify them
                        counter -= 1            # cancel the count
                        userNumStore.pop(-1)    # delete the duplicated number

                    window['-NUM-'].update(f"{min} < NUM < {max}")  # update the range display


# ask for a replay and replays/ends the game
def replayGame():
    global status

    # if the game is finished and the user presses the 'Replay',
    if status == "finished" and event == '-LEFT-':
        reset()  # Reset variables
        resetMsg()  # Reset messages window


# Clears the input field
def clearField():
    global status

    # if the user is playing, and the 'Clear' Button was pressed
    if status == "start" and event == '-LEFT-':
        window['-IN-'].update('')  # update field to BLANK


# Reset the game
def resetGame():
    # if the reset button was pressed,
    if event == 'Reset':
        reset()  # reset variables
        resetMsg()  # reset message windows


# start the program by resetting variables and messages (DEFAULT)
reset()

# Loop this until it breaks
while True:
    # Read event(button pressed) and values(the input values) from the window
    event, values = window.read()

    # Execute the functions
    modeSelect()
    compareNum()
    replayGame()
    clearField()
    resetGame()

    # if 'Exit' button pressed or the window is closed, break this loop
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

# Close the Window
window.close()
