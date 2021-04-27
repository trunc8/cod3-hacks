import hashlib
import PySimpleGUI as sg
import os
import re

def hash(fname, method):
    if method == 'SHA1':
        hash = hashlib.sha1()
    elif method == 'MD5':
        hash = hashlib.md5()
    elif method == 'SHA256':
        hash = hashlib.sha256()
    
    with open(fname) as handle:
        for line in handle:
            hash.update(line.encode(encoding = 'utf-8'))
    return(hash.hexdigest())


sg.change_look_and_feel('LightBlue3')

layout = [
    [sg.Text('File 1: '),
    sg.InputText(),
    sg.FileBrowse(),
    sg.Checkbox('SHA1'),
    sg.Checkbox('MD5')],
    [sg.Text('File 2: '),
    sg.InputText(),
    sg.FileBrowse(),
    sg.Checkbox('SHA256')],
    [sg.Output(size=(80,20))],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Compare Files', layout)

while True:
    event, values = window.read()
    if event in (None, 'Exit', 'Cancel'):
        break
    if event=='Submit':
        # print(event, values)
        filepaths = []
        methods = []
        file1 = None
        file2 = None
        valid = None
        if values[0] and values[3]:
            # print(values[0])
            # print(values[3])
            file1 = re.findall('\/.+\.+.', values[0])
            file2 = re.findall('\/.+\.+.', values[3])
            valid = 1
            if (not file1 and file1 is not None) or not os.path.isfile(values[0]):
                print('Error: Invalid filepath for File 1')
                valid = 0
            elif (not file2 and file2 is not None) or not os.path.isfile(values[3]):
                print('Error: Invalid filepath for File 2')
                valid = 0
            elif not (values[1] or values[2] or values[4]):
                print('Error: No algorithm selected')
                valid = 0
            elif valid == 1:
                print('Info: Valid paths entered')
                if values[1]:
                    methods.append('SHA1')
                if values[2]:
                    methods.append('MD5')
                if values[4]:
                    methods.append('SHA256')
                
                filepaths.append(values[0]) # File 1
                filepaths.append(values[3]) # File 2
                # print(methods)
                # print(filepaths)

                for method in methods:
                    print(f'>> {method} Comparison')
                    print(f'Hash of File 1 is {hash(filepaths[0], method)}')
                    print(f'Hash of File 2 is {hash(filepaths[1], method)}')
                    if hash(filepaths[0], method) == hash(filepaths[1], method):
                        print(f'The two files are identical relying on {method} method\n')
                    else:
                        print(f'The two files are different relying on {method} method\n')
            else:
                print('Error: Please choose 2 files')