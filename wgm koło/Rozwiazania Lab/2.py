from pickletools import uint8
from PIL import Image, ImageOps
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

picture = Image.open('E:/V semestr/wpr_do_grafiki_maszynowej/lab2/mw.bmp')

def wstaw_obraz(picture, w_m, h_m, wsp):
    w0=100
    h0=50

    if wsp>1:
        tab_picture = np.asarray(picture)
        tab_new_picutre=np.zeros((wsp*h0, wsp*w0), dtype=np.uint8 )
        
        for i in range(h_m, h_m+50-1):
            for j in range(w_m, w_m+100-1):
                if(j<w0*wsp and i<h0*wsp):
                    tab_new_picutre[i][j] = tab_picture[i-h_m][j-w_m]

        tab_new_picutre=tab_new_picutre.astype(bool)
        picture_tab_new_picture = Image.fromarray(tab_new_picutre)  
        return picture_tab_new_picture

    else:
        print("niepoprawa wartosc wspolczynnika")
        return 0



# picture_in_function = wstaw_obraz(picture, 100, 120, 3)
# if picture_in_function:
#     picture_in_function.show()
#     picture_in_function.save('E:/V semestr/wpr_do_grafiki_maszynowej/lab2/Obraz1_zad1.bmp')


# picture_in_function2 = wstaw_obraz(picture, 10, 140, 4)
# if picture_in_function2:
#     picture_in_function2.show()
#     picture_in_function.save('E:/V semestr/wpr_do_grafiki_maszynowej/lab2/Obraz2_zad1.bmp')

# picture_in_function3 = wstaw_obraz(picture, 250, 100, 6)
# if picture_in_function3:
#     picture_in_function3.show()
#     picture_in_function.save('E:/V semestr/wpr_do_grafiki_maszynowej/lab2/Obraz3_zad1.bmp')


#zad3

def first_function(w, h): 
    dzielnik = 8
    t = (h, w)  
    tab = np.zeros(t, dtype=np.uint8)  
    grub = int(min(w, h) / dzielnik)  
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2] = 1
    r=1  
    for x in range(2,5):
        if (r==1):
            z3=z1-grub
            z4=z2-grub
            tab[grub*x:z3, grub*x:z4]=0
            r=0
            z1=z3
            z2=z4
        else:
            z3 = z1 - grub
            z4 = z2 - grub 
            tab[grub*x: z3, grub * x: z4] = 1 
            r=1
            z1=z3
            z2=z4
    return tab *255

frame = first_function(480, 320) 
picture_frame=Image.fromarray(frame)
# picture_frame.save('E:/V semestr/wpr_do_grafiki_maszynowej/lab2/Obraz_zad3_1.bmp')
picture_frame.show()


# def second_function(w, h): 
    
#     t = (h, w)  
#     dzielnik= 8
#     tab = np.ones(t, dtype=np.uint8)
#     grub = int(h / dzielnik)  
#     print(grub)
#     for k in range(dzielnik+4):  
#         for g in range(grub):
#             j = k * grub + g  
#             for i in range(h):
#                 tab[i, j] = k % 2  
#     tab = tab * 255  
#     return tab

    
# tab = second_function(480,320)
# picture_frame2 = Image.fromarray(tab)
# picture_frame2.show()
# picture_frame2.save('E:/V semestr/wpr_do_grafiki_maszynowej/lab2/Obraz_zad3_2.bmp')


# def third_funtion(w, h):
#     t = (w, h)
#     m=50
#     n=20
#     tabb = np.ones(t, dtype=np.int8)
#     tabb[0:n, 0:m]=0
#     tabb[n:h, m:w]=0
#     return tabb * 255


# tablica=third_funtion(480, 320)
# tablica = tablica.astype(np.uint8)
# obrazekk = Image.fromarray(tablica)
# obrazekk.show()
# obrazekk.save('E:/V semestr/wpr_do_grafiki_maszynowej/lab2/Obraz_zad3_3.bmp')


# def my_function(w, h):
#     t = (w, h)
#     tabbb = np.ones(t, dtype=np.int8)
#     a=20
#     b=50
#     c=80
#     d=110
    
#     tabbb[0:a, 0:b]=0
#     tabbb[a:c, b:d]=0
#     tabbb[c:230, d:290]=0
#     tabbb[230:290, 50:110]=0
#     tabbb[290:w, 110:h]=0
   

#     return tabbb * 255
    


# tabbb=my_function(480,320)
# tabbb = tabbb.astype(np.uint8)
# obrazek = Image.fromarray(tabbb)
# obrazek.show()
# obrazek.save('E:/V semestr/wpr_do_grafiki_maszynowej/lab2/Obraz_zad4.bmp')

    
 

    



    

