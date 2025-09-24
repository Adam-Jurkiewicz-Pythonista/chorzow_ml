
import os
import cv2
import logging
import numpy as np
from sklearn.cluster import KMeans
from datetime import datetime

#ustawienie logowaia do pliku
logging.basicConfig(
    filename=f'obraz_00-{datetime.now().strftime('%Y%m%d-%H%M%S')}.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s'
)


def wczytaj_pliki_z_katalogu(nazwa_katalogu, typy_plikow=("jpg","bmp","jpeg"), min_wielkosc=1000):
    if not os.path.isdir(nazwa_katalogu):
        return False
    zwracane_pliki = []
    # rekurencyjnie sprawdza podkatalogi
    # https://github.com/abixadamj/helion-python/blob/main/Rozdzial_7/r7_00_walk.py
    for dirpath, dirname, files in os.walk(nazwa_katalogu):

        for each_file in files:
            ext = os.path.splitext(each_file)[1].lower()
            for maska in typy_plikow:
                if maska in ext:
                    plik_z_danymi = dirpath + "/" + each_file
                    if os.path.getsize(plik_z_danymi)>min_wielkosc:
                        zwracane_pliki.append(plik_z_danymi)

    return zwracane_pliki

def image_file_change2bw(file_image):
    if not os.path.isfile(file_image):
        print(f"File not found - {file_image}")
        return False, 0

    img = cv2.imread(file_image)
    log = f"{file_image=} {img.dtype=} {img.shape=}"
    print(log)
    logging.info(log)

    if img.dtype == np.uint8:
        return False, img
    try:
        return True, cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except Exception as e:
        print(e)
        return False, 0

def image_save2file(image_type, file_image):
    try:
        if not os.path.isfile(file_image):
            cv2.imwrite(file_image, image_type)
            return True
    except Exception as e:
        print(f"image_save2file - {e=}")
        return False

def image_read8bit(file_8bit):
    if not os.path.isfile(file_8bit):
        print(f"File not found - {file_8bit}")
        return False, 0
    # Wczytaj obraz w skali szarości
    img = cv2.imread(file_8bit)
    log = f"Loaded {file_8bit=} {img.dtype=} {img.shape=}"
    logging.info(log)
    return True, img

def image_kmean(file_8bit, clusters=4):
    img = cv2.imread(file_8bit, cv2.IMREAD_GRAYSCALE)
    # Spłaszcz obraz do 1-wymiarowej tablicy (lista pikseli)
    log = f"Kmean start {img=} {img.shape=}"
    logging.info(log)
    pixels = img.reshape(-1, 1)

    # Model KMeans
    kmeans = KMeans(n_clusters=clusters) # Liczba klastrów (odcieni)
    kmeans.fit(pixels)

    # Centroidy - reprezentatywne odcienie
    centers = kmeans.cluster_centers_.flatten().astype(np.uint8)

    # Przypisania klastrów dla pikseli
    labels = kmeans.labels_

    # Odtworzenie obrazu na podstawie centroidów (redukcja ilości odcieni)
    segmented_img = centers[labels].reshape(img.shape)

    logging.info(f"Done Kmean with {segmented_img} {segmented_img.shape=}")
    return segmented_img

def all_kmean(pliki_z_danymi):
    for plik_8bit in pliki_z_danymi:
        nazwa_bez_rozszerzenia = os.path.splitext(os.path.basename(plik_8bit))[0]
        katalog = os.path.dirname(plik_8bit) + "/kmean/"
        try:
            os.mkdir(katalog)
        except:
            pass
        # dla 2 klastrów widać dzialanie.....
        kmean_img = image_kmean(plik_8bit, clusters=2)
        image_save2file(kmean_img, katalog+nazwa_bez_rozszerzenia+"_kmean.png")




if __name__ == "__main__":
    katalog = "img/"
    pliki_8bit = []
    pliki = wczytaj_pliki_z_katalogu(katalog)
    print(f"{pliki=}")
    if pliki:
        for plik in pliki:
            katalog = os.path.dirname(plik) + "/"
            print(plik)
            file_ok, image = image_file_change2bw(plik)
            if file_ok:
                nazwa_bez_rozszerzenia = os.path.splitext(os.path.basename(plik))[0]
                plik_do_zapisu = katalog+nazwa_bez_rozszerzenia + "_bw.jpg"
                if image_save2file(plik_do_zapisu, image):
                    pliki_8bit.append(plik_do_zapisu)
            else:
                pliki_8bit.append(plik)
        else:
            logging.info(f"pliki_8bit - {pliki_8bit=}")


    # sprawdzanie kmean
    all_kmean(pliki_8bit)

