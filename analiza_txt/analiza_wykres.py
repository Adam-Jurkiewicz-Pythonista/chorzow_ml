plik_wejsciowy = "../Dane_txt/CMSX.txt"
with open(plik_wejsciowy, encoding="utf-8") as plik:
    wykres = plik.readlines()

# print(wykres)
naglowek = wykres[0:4]
dane = wykres[4:]

# print(f"{naglowek}")
# print(f"{naglowek=}")
# print(f"{dane=}")

elementy_y = []
for element in dane:
    dana = element.split(" ")
    for liczba in dana:
        try:
            elementy_y.append(int(liczba))
        except:
            pass

print(f"{elementy_y=}")