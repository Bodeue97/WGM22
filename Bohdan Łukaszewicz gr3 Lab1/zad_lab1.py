
import numpy as np
from PIL import Image
import sys
np.set_printoptions(threshold=sys.maxsize)



obrazek = Image.open("inicjały.bmp")
# obrazek.show()
print("---------- informacje o obrazie")
print("tryb:", obrazek.mode)
print("format:", obrazek.format)
print("rozmiar:", obrazek.size)

dane_obrazka = np.asarray(obrazek)
# with open('inicjały.txt', 'w') as f:
#     f.write(str(dane_obrazka*1))
print("typ danych tablicy:", dane_obrazka.dtype)
print("rozmiar tablicy:", dane_obrazka.shape)
print("liczba elementow:", dane_obrazka.size)
print("wymiar tablicy:", dane_obrazka.ndim)
print("rozmiar wyrazu tablicy:", dane_obrazka.itemsize)



print("50:30:", dane_obrazka[30][50]*1)
print("90:40", dane_obrazka[40][90]*1)
print("99:0", dane_obrazka[0][99]*1)
#
# with open('inicjały2.txt', 'w') as f:
#     f.write(str(dane_obrazka*1))

file = open()
boolarr = np.fromstring()




