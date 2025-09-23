import PySimpleGUI as sg

layout = [
    [sg.Text('Select a folder:'), sg.Input(key='-FOLDER-', change_submits=True), sg.FolderBrowse()],
    [sg.Button('Ok'), sg.Button('Cancel')]
]

window = sg.Window('Folder Browse Example', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event == '-FOLDER-':
        folder_path = values['-FOLDER-']
        print(f'Selected folder: {folder_path}')
    if event == 'Ok':
        print(f'Folder confirmed: {values["-FOLDER-"]}')
        break

window.close()
