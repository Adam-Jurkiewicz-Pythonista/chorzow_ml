plik_wejsciowy = "../Dane_txt/CMSX.txt"
with open(plik_wejsciowy, encoding="utf-8") as plik:
    wykres = plik.readlines()

print(wykres)