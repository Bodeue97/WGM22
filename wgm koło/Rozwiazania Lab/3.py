from PIL import Image
import numpy as np

def first_function_3_1_lab2(w, h, kolor_ramki, kolor):
    dzielnik = 8
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    grub = int(min(w, h) / dzielnik)
    tab[:]=kolor_ramki
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2] = kolor
    r=1
    for x in range(2,5):
        if (r==1):
            z3=z1-grub
            z4=z2-grub
            tab[grub*x:z3, grub*x:z4]=kolor_ramki
            r=0
            z1=z3
            z2=z4
        else:
            z3 = z1 - grub
            z4 = z2 - grub
            tab[grub*x: z3, grub * x: z4] = kolor
            r=1
            z1=z3
            z2=z4
    return tab

tab=first_function_3_1_lab2(300,200,100,200)
obrazek=Image.fromarray(tab)
obrazek.show()
# obrazek.save(r'E:/V semestr/wpr_do_grafiki_maszynowej/lab3/obraz1_1N.jpg')
# obrazek.save(r'E:/V semestr/wpr_do_grafiki_maszynowej/lab3/obraz1_1N.png')



def my_function_3_4_lab2(w, h,kolor,kolor_2):
    t = (w, h)
    tabbb = np.ones(t, dtype=np.int8)
    tabbb[: :]=kolor
    a = 20
    b = 50
    c = 80
    d = 110

    tabbb[0:a, 0:b] = kolor_2
    tabbb[a:c, b:d] = kolor_2
    tabbb[c:230, d:290] = kolor_2
    tabbb[230:290, 50:110] = kolor_2
    tabbb[290:w, 110:h] = kolor_2

    return tabbb


tab2=my_function_3_4_lab2(400,200,100,200)
tab2=tab2.astype(np.uint8)
obrazek2=Image.fromarray(tab2)
obrazek2.show()
# obrazek2.save(r'E:/V semestr/wpr_do_grafiki_maszynowej/lab3/obraz1_2N.jpg')
# obrazek2.save(r'E:/V semestr/wpr_do_grafiki_maszynowej/lab3/obraz1_2N.png')


def second_function_3_2_lab2(obraz):
    tab = np.asarray(obraz)
    h, w = tab.shape[0], tab.shape[1]
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i,j]=255 - tab[i,j]
            return tab_neg


obrazek_zad_3_2_lab2 = Image.open(r'E:\V semestr\wpr_do_grafiki_maszynowej\lab3\Obraz_zad3_2.bmp')
tab3=second_function_3_2_lab2(obrazek_zad_3_2_lab2)
tab3=tab3.astype(np.uint8)
obrazek3=Image.fromarray(tab3)
obrazek3.show()
# obrazek3.save(r'E:/V semestr/wpr_do_grafiki_maszynowej/lab3/obraz2N.jpg')
# obrazek3.save(r'E:/V semestr/wpr_do_grafiki_maszynowej/lab3/obraz2N.png')


def color_initials(obraz, kolor_bialy):
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if t_obraz[i, j] == False:
                tab[i, j] = [200+j+(i*7),50+i+(j*5),0+(i*j)*10]
            else:
                tab[i, j] = kolor_bialy
    return tab


obrazz = Image.open(r'E:\V semestr\wpr_do_grafiki_maszynowej\lab3\mw.bmp')

tab4=color_initials(obrazz, [255,255,255])

obrazz_color=Image.fromarray(tab4)
obrazz_color.show()
obrazz_color.save(r'E:/V semestr/wpr_do_grafiki_maszynowej/lab3/obraz3.jpg')
obrazz_color.save(r'E:/V semestr/wpr_do_grafiki_maszynowej/lab3/obraz3.png')
