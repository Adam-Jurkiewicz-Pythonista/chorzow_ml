import PySimpleGUI as sg
from analiza_gui_fn import *

layout = [
    [sg.Text('Wybierz folder z plikami:'), sg.Input(key='-FOLDER-', change_submits=True), sg.FolderBrowse()],
    [sg.Button('Ok'), sg.Button('Cancel')]
]

window = sg.Window('Wykonanie plików graficznych', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event == '-FOLDER-':
        folder_path = values['-FOLDER-']
        print(f'Selected folder: {folder_path}')
    if event == 'Ok':
        print(f'Folder confirmed: {values["-FOLDER-"]}')
        # wywołamy program generujący pliki
        pliki_do_sprawdzenia = wczytaj_dane_z_katalogu(values["-FOLDER-"], min_wielkosc=300)
        print(f"{pliki_do_sprawdzenia=}")
        if pliki_do_sprawdzenia:
            for plik_txt in pliki_do_sprawdzenia:
                elem_y, nazwa_wykresu, czas, fwhm = otworz_plik_wczytaj_dane(plik_txt)
                if elem_y is False:
                    continue
                # print(f"{plik_txt=}")
                if len(elem_y) > 100:
                    # print(f"{elem_y=}")
                    lista_x, lista_y = przygotuj_dane_do_wyswietlenia(elem_y, czas)
                    wykonaj_wykres(lista_x, lista_y, nazwa_wykresu, plik_txt)
        break

window.close()
