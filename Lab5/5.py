from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("baby_yoda.jpg")
inic = Image.open("inicjały.bmp")
cpy = im.copy()

def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]

def wstaw_inic(obraz, inicjaly,  m, n, kolor):

    w, h = obraz.size
    w_z, h_z = inicjaly.size
    inicArr = np.asarray(inicjaly)

    for i, j in zakres(w_z, h_z):
        if i + m < w and j + n < h:
            if inicArr[j][i] == False:
                obraz.putpixel((i + m, j + n), kolor)
            else:
                obraz.putpixel((i+m, j+n), (255,255,255))

    return obraz

wstaw_inic(cpy, inic, 730, 575, 200).save("obaz1.jpg")


#
# def wstaw_inic_maska(obraz, inicjaly, m, n, a, b, c):
#     obraz1 = obraz.copy()
#     w, h = obraz.size
#     w0, h0 = inicjaly.size
#     for i, j in zakres(w0, h0):
#         if i + m < w and j + n < h:
#             if inicjaly.getpixel((i, j)) == 0:
#                 p = obraz.getpixel((i + m, j + n))
#                 obraz1.putpixel((i + m, j + n), (p[0] + a, p[1] + b, p[2] + c))
#     return obraz1
#
#
#
#
#
#
#
#
#
#
# def wstaw_inic_load(obraz, inicjaly,  m, n, kolor):
#
#     w, h = obraz.size
#     w_z, h_z = inicjaly.size
#
#     ob1=obraz.load()
#     ob2=inicjaly.load()
#
#
#     for i, j in zakres(w_z, h_z):
#         if i + m < w and j + n < h:
#             if inicjaly.getpixel((i,j)) == 0:
#                 ob1[i+m, j+n]=kolor
#
#     return obraz
#
#
#
#
#
# def wstaw_inic_maska(obraz, inicjaly, m, n, a, b, c):
#     obraz1 = obraz.copy()
#     w, h = obraz.size
#     w0, h0 = inicjaly.size
#     ob1 =
#     for i, j in zakres(w0, h0):
#         if i + m < w and j + n < h:
#             if inicjaly.getpixel((i, j)) == 0:
#                 p = obraz.getpixel((i + m, j + n))
#                 obraz1.putpixel((i + m, j + n), (p[0] + a, p[1] + b, p[2] + c))
#     return obraz1