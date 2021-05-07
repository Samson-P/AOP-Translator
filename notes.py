import PySimpleGUI as sg

sg.theme('Dark')
layout_notes = [
        [sg.Text('Внимание, ctrl + c, ctrl + v работают')],
        [sg.Text('только на английской раскладке.')],
        [sg.Text('По вопросам стучаться на мыло, Самсон:')],
        [sg.Text('europioid108000000000@gmail.com')],
        [sg.Cancel()]
]


question = sg.Window('О себе:)', layout_notes)
while True:
    k, b = question.read()
    if k in ('Cancel', None):
        break

del layout_notes, k, b, question