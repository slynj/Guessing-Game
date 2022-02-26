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

sg.theme('BlueMono')
layout = [[sg.Button('Easy'), sg.Button('Medium'), sg.Button('Hard')],
          [sg.Text('input range: '), sg.Text(size=(15, 1), key='-RANGE-')],
          [sg.Input(key='-IN-'), sg.Button('Submit')],
          [sg.Text(key='-MSG-')],
          [sg.Button('Clear', key='-LEFT-'), sg.Exit()]
          ]

window = sg.Window('Number Guessing Game', layout)
mode = ''
event, values = window.read()
if event == sg.WIN_CLOSED or event == 'Exit':
    window.close()