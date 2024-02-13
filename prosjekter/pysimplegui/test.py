import PySimpleGUI as sg
import os

file_path = os.path.realpath(__file__)
print(file_path)

# All the stuff inside your window.
layout = [  [sg.Text('Fil leser!')],
            [sg.Text('Skriv inn fil: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('Fil valgt: ', values[0])
    try:
        with open(values[0], "r") as file:
            tekst = file.read()
        print(tekst)
    except:
        print("Filen finnes ikke")

window.close()