import matplotlib.pyplot as plt

plik_wejsciowy = "../Dane_txt/CMSX.txt"
with open(plik_wejsciowy, encoding="utf-8") as plik:
    wykres = plik.readlines()

# print(wykres)
naglowek = wykres[0:4]
dane = wykres[4:]

nazwa_do_wykresu = naglowek[0].strip()

elementy_y = []
for element in dane:
    dana = element.split(" ")
    for liczba in dana:
        try:
            elementy_y.append(int(liczba))
        except:
            pass

elementy_x = [ x for x in range(len(elementy_y))]

# Tworzenie wykresu słupkowego
plt.bar(elementy_x, elementy_y)
plt.yscale('log')
# Dodanie tytułu i etykiet osi
plt.title(f"Przykładowy wykres słupkowy - {nazwa_do_wykresu} ")
plt.xlabel("x")
plt.ylabel("y")

# Zapis wykresu do pliku
plt.savefig("wykres_slupkowy.png")

# Wyświetlenie wykresu
plt.show()