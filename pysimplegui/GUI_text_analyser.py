import PySimpleGUI as sg
import os
import re

def text_analyser(fname):
    words=characters=0
    with open(fname) as handle:
        for line in handle:
            characters += len(line)
            words += len(re.findall(r'\w+', line)) 
    return [words, characters]

sg.change_look_and_feel('LightBlue3')

layout = [
    [sg.Text('File: '),
    sg.InputText(),
    sg.FileBrowse(),
    ],
    [sg.Output(size=(88,20))],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Text Analyser', layout)

while True:
    event, values = window.read()
    # print('1:',event, values)
    if event in (None, 'Exit', 'Cancel'):
        break
    if event=='Submit':
        file_name = None
        valid = 0
        # print('2: ',values[0])
        if values[0]:
            file_name = re.findall('\/.+\/.+\.+.', values[0])
            # print('3: ',file_name)
            valid = 1
            if (not file_name and file_name is not None) or not os.path.isfile(values[0]):
                print('Error: Invalid file path')
                valid = 0
            elif valid==1:
                print('Info: Filepath is valid')
                [words, characters] = text_analyser(values[0])
                print(f'Words: {words} \t Characters: {characters}')
            else:
                print('Please choose a file')
                window.close()