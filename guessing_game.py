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

sg.theme('BlueMono')    # Theme colour set to blue

# Elements in the window.
layout = [
    [sg.Text('Guessing Game')],
    [sg.Text('Enter something on Row 2'), sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')]
]

window = sg.Window('Number Guessing Game', layout, margins=(100, 50))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
