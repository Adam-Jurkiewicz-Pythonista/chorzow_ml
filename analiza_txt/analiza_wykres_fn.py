import os
import matplotlib.pyplot as plt

def przygotuj_dane_do_wyswietlenia(punkty_y, czas):
    maximum = 0
    index_y = 0
    for ind, punkty in enumerate(punkty_y):
        if punkty > maximum:
            maximum = punkty
            index_y = ind

    odciete_y = punkty_y[index_y:]
    odciete_x = [ (x+index_y) * czas for x in range(len(odciete_y))]

    return odciete_x, odciete_y

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
    nazwa_do_wykresu = naglowek[0].strip().replace(" ", "_")
    try:
        czas = float(naglowek[1].strip())
        fwhm = float(naglowek[3].strip())
    except:
        czas = 0
        fwhm = 0
    elementy_y = []
    for element in dane:
        dana = element.split()
        if type(dana) is not list:
            print("Problem ze splitem")
            return False, False, False, False

        for liczba in dana:
            try:
                elementy_y.append(int(liczba))
            except:
                pass

    return elementy_y, nazwa_do_wykresu, czas, fwhm

def wykonaj_wykres(elementy_x, elementy_y, nazwa_do_wykresu, nazwa_pliku, typ_wykresu='log'):
    nazwa_bez_rozszerzenia = os.path.splitext(os.path.basename(nazwa_pliku))[0]
    katalog = os.path.dirname(nazwa_pliku)
    plik_png = f"{katalog}/{nazwa_bez_rozszerzenia}-{nazwa_do_wykresu.strip()}.png"
    plt.xlim(elementy_x[0],elementy_x[-1])
    plt.bar(elementy_x, elementy_y)
    plt.yscale('log')
    plt.title(f"Wykres odcięty od maximum ({elementy_y[0]})- {nazwa_do_wykresu} - ({min(elementy_y)})")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig(plik_png, dpi=600)
    plt.clf() # czyści ram po zapisie pliku
    # print(f"{nazwa_do_wykresu=} / {len(elementy_y)=} {elementy_y=}")
    # plt.show()


# tutaj start skryptu
# plik_sprawdz = "../Dane_txt/CS_MCF15_294K.txt"
# elem_y, nazwa_wykresu = otworz_plik_wczytaj_dane(plik_sprawdz)
# print(elem_y)
#
katalog = "../Dane_txt"
pliki_do_sprawdzenia = wczytaj_dane_z_katalogu(katalog,min_wielkosc=1)
print(f"{pliki_do_sprawdzenia=}")
for plik_txt in pliki_do_sprawdzenia:
    elem_y, nazwa_wykresu, czas, fwhm = otworz_plik_wczytaj_dane(plik_txt)
    if elem_y is False:
        continue
    # print(f"{plik_txt=}")
    if len(elem_y) > 100:
        # print(f"{elem_y=}")
        lista_x, lista_y = przygotuj_dane_do_wyswietlenia(elem_y, czas)
        wykonaj_wykres(lista_x, lista_y,nazwa_wykresu, plik_txt)