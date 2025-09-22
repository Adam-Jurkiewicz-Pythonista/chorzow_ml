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