import PySimpleGUI as sg
import sys
import subprocess
import pyperclip


def translator(input_text):
    for i in range(len(input_text)):
        if input_text[i] == 'а':
            input_text = input_text[:i] + 'a' + input_text[i + 1:]
        if input_text[i] == 'р':
            input_text = input_text[:i] + 'p' + input_text[i + 1:]
        if input_text[i] == 'о':
            input_text = input_text[:i] + 'o' + input_text[i + 1:]
    return input_text


def frame():
    sg.theme('Dark')
    layout = [
        [sg.Button('перевод'), sg.Button('перезапуск')],
        [sg.Text('Ниже введите текст для замены букв "о", "а" и "р".')],
        [sg.InputText(pyperclip.paste(), size=(60, 10))],
        [sg.Text('После замены мы получаем вот это:')],
        [sg.Output(size=(60, 15))],
        [sg.Cancel(), sg.Button('справка')]
    ]
    window = sg.Window('переводчик', layout)
    while True:
        event, values = window.read()
        if event == 'перевод':
            print(translator(values[0]))
        if event == 'справка':
            subprocess.Popen([sys.executable, 'notes.py'])
        if event == 'Cancel':
            layout2 = [
                [sg.Text('Хотите выйти из программы?')],
                [sg.Text('Не сохраненные данные будут потеряны.')],
                [sg.Button('да'), sg.Cancel()]
            ]
            question = sg.Window('Осторожно!', layout2)
            k, b = question.read()
            question.close()
            if k == 'да':
                window.close()
                return 0
                break
            del layout2, k, b, question
        if event in (None, None):
            return 0
            break
        if event == 'перезапуск':
            layout2 = [
                [sg.Text('Хотите перезапустить окно?')],
                [sg.Text('Введенный текст будет потерян =/')],
                [sg.Button('да'), sg.Cancel()]
            ]
            question = sg.Window('Внимание!', layout2)
            k, b = question.read()
            question.close()
            if k == 'да':
                window.close()
                return 1
                break

            del layout2, k, b, question


while True:
    out = frame()
    if out == 0:
        break
