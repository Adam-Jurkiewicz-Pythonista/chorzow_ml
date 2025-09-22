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
    return odciete_y

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
    with open(nazwa_pliku, encoding="utf-8") as plik:
        wczytane_dane = plik.readlines()

    naglowek = wczytane_dane[0:4]
    dane = wczytane_dane[4:]
    nazwa_do_wykresu = naglowek[0].strip()
    elementy_y = []
    for element in dane:
        dana = element.split(" ")
        for liczba in dana:
            try:
                elementy_y.append(int(liczba))
            except:
                pass

    return elementy_y, nazwa_do_wykresu

def wykonaj_wykres(elementy_y, nazwa_do_wykresu, typ_wykresu='log'):
    elementy_x = [x for x in range(len(elementy_y))]
    plt.bar(elementy_x, elementy_y)
    plt.yscale('log')
    plt.title(f"Wykres odcięty od maximum ({elementy_y[0]})- {nazwa_do_wykresu} - ({min(elementy_y)})")
    plt.xlabel("x")
    plt.ylabel("y")


# tutaj start skryptu
katalog = "../Dane_txt"
pliki_do_sprawdzenia = wczytaj_dane_z_katalogu(katalog,min_wielkosc=1)
print(f"{pliki_do_sprawdzenia=}")