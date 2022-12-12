# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt

# def zakres(w, h):
#     return [(i, j) for i in range(w) for j in range(h)]

# def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
#     ob_tmp = obraz.copy()
#     w, h = obraz.size
#     w_z, h_z = inicjaly.size

#     for i, j in zakres(w_z, h_z):
#         if i + m < w and j + n < h:
#             ob_tmp.putpixel((i+m, j+n), kolor)
#             if inicjaly.getpixel((i,j))==0:
#                 ob_tmp.putpixel((i+m, j+n), (255,0,0))
#     return ob_tmp


# def wstaw_inicjaly_maska(obraz, inicjaly, m,n,x,y,z):
#     obraz1 = obraz.copy()
#     w, h = obraz.size
#     w0, h0 = inicjaly.size
#     for i, j in zakres(w0, h0):
#         if i + m < w and j + n < h:
#             if inicjaly.getpixel((i, j)) == 0:
#                 p = obraz.getpixel((i + m, j + n))
#                 obraz1.putpixel((i + m, j + n), (p[0] + x, p[1] + y, p[2] + z))
#     return obraz1

# def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
#     w, h = obraz.size
#     ob_tmp = obraz.copy()
#     w_z, h_z = inicjaly.size
#     pix1=ob_tmp.load()
#     pix2=inicjaly.load()

#     for i, j in zakres(w_z, h_z):
#         if i + m < w and j + n < h:
#             pix1[i+m,j+n]=kolor
#             if pix2[i,j]==0:
#                pix1[i+m,j+n]=(255,0,0)
#     return ob_tmp

# def wstaw_inicjaly_maska_load(obraz, inicjaly, m,n,x,y,z):
#     obraz1 = obraz.copy()
#     w, h = obraz.size
#     w0, h0 = inicjaly.size
#     pix1 = obraz1.load()
#     pix2 = inicjaly.load()
#     pix3 = obraz.load()

#     for i, j in zakres(w0, h0):
#         if i + m < w and j + n < h:
#             if pix2[i,j]==0:
#                 p = pix3[i+m,j+n]
#                 pix1[i+m,j+n]=(p[0] + x, p[1] + y, p[2] + z)
#     return obraz1



# def kontrast(obraz, wsp_kontrastu):
#     if wsp_kontrastu > 100 or wsp_kontrastu < 0:
#         return False
#     else:
#         mn=((255+wsp_kontrastu)/255)**2
#         tmp=obraz.point(lambda i: 128+(i-128)*mn)
#     return tmp

# def transformacja_logarytmiczna(obraz):
#     tmp=obraz.point(lambda i: 255*np.log(1+i/255))
#     return tmp

# def transformacja_gamma(obraz, gamma):
#     if gamma<0:
#         return False
#     else:
#         tmp=obraz.point(lambda i: (i/255)**(1/gamma)*255)
#     return tmp

# # def funkcja_zad5(tab, w,h):

# #     tab2=np.zeros((w,h), dtype=np.uint8)
# #     for i in range(0,w):
# #         for j in range(0,h):
# #             tab[i,j]=1
            
# #     return tab
    
    
    
        


# obraz = Image.open('obraz.jpg')
# inicjaly = Image.open('inicjaly.bmp')


# test = wstaw_inicjaly(obraz, inicjaly, 2900, 1950, (255,255,255))
# test.save('obraz1.png')
# test.show()

# test2 = wstaw_inicjaly_maska(obraz, inicjaly, 1500,1000, 100,200,300)
# test2.save('obraz2.png')
# test2.show()

# test3 = wstaw_inicjaly_load(obraz,inicjaly,2900,1950,(255,255,255))
# test3.show()

# test4 = wstaw_inicjaly_maska_load(obraz, inicjaly, 1500,1000, 100,200,300)
# test4.show()

# test5 = kontrast(obraz, 80)
# if test5 != False:
#     test5.show()
# else:
#     print('Niepoprawny współczynnik kontrastu')

# test6 = transformacja_logarytmiczna(obraz)
# test6.show()

# test7 = transformacja_gamma(obraz, 35)
# if test7 != False:
#     test7.show()
# else:
#     print('Niepoprawny współczynnik gamma')

# T = np.array(obraz, dtype='uint8')
# T+=100
# obraz_wynik=Image.fromarray(T, "RGB")
# obraz_wynik.show()

# test8=obraz.point(lambda i: i+100)
# test8.show()


# tab = np.asarray(obraz)
# w,h = obraz.size


# temp = funkcja_zad5(tab,w ,h)
# test9=Image.fromarray(temp)

# test9.show()

wynik = (1/21.586)+(1/0.9705)+(1/1.5042)+(1/5.631)
print(wynik)