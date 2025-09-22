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

def wczytaj_dane_z_katalogu(nazwa_katalogu, maska=".txt", min_wielkosc=100):
    if not os.path.isdir(nazwa_katalogu):
        return False
    zwracane_pliki = []
    for dirpath, dirname, files in os.walk(nazwa_katalogu):

        for each_file in files:
            if maska in each_file:
                plik_z_danymi = dirpath + "/" + each_file
                if os.path.getsize(plik_z_danymi)>min_wielkosc:
                    zwracane_pliki.append(plik_z_danymi)

    return zwracane_pliki


def otworz_plik_wczytaj_dane(nazwa_pliku):

    # to-do: napisać ifa, jesli bra pliku to return False




# tutaj start skryptu
katalog = "../Dane_txt"
pliki_do_sprawdzenia = wczytaj_dane_z_katalogu(katalog,min_wielkosc=1)
print(f"{pliki_do_sprawdzenia=}")