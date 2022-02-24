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

import PySimpleGUI as gui

gui.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [gui.Text('Some text on Row 1')],
            [gui.Text('Enter something on Row 2'), gui.InputText()],
            [gui.Button('Ok'), gui.Button('Cancel')]]

window = gui.Window('Number Guessing Game', layout)

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
