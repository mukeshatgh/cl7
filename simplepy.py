import PySimpleGUI as sg                        # Part 1 - The import

# Define the window's contents
layout = [  [sg.Text("What's your name?")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Text("What is Your age?")],
            [sg.Input()],
            [sg.Button('Ok')],
            [sg.Button('1')] ,
            [sg.Button('2')] ,
            [sg.Button('3')] ,
            [sg.Button('4')]  ]

# Create the window
window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered
print('Hello', values[0], "! Your Age is",values[1])

# Finish up by removing from the screen
window.close()        