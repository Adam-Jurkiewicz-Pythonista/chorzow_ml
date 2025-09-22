import os
import matplotlib.pyplot as plt

def przygotuj_dane_do_wyswietlenia(punkty_y):
    maximum = 0
    index_y = 0
    for ind, punkty in enumerate(punkty_y):
        if punkty > maximum:
            maximum = punkty
            index_y = ind

    odciete_y = punkty_y[index_y:]
    elementy_x = [ x for x in range(len(odciete_y))]
    return [elementy_x, odciete_y]

def wczytaj_dane_z_katalogu(nazwa_katalogu, maska=".txt"):
    if not os.path.isdir(nazwa_katalogu):
        return False

    for dirpath, dirname, files in os.walk(nazwa_katalogu):
        print(f"dirpath = {dirpath}")
        print(f"dirname = {dirname}")
        print(f"files = {files}")
        if maska in files:
            print(f"{maska=} / {files=}")


# tutaj start skryptu
katalog = "../Dane_txt"
wczytaj_dane_z_katalogu(katalog)