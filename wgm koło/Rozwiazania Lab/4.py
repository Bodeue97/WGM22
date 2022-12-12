import numpy.random
from PIL import Image, ImageOps, ImageChops
import numpy as np
import matplotlib.pyplot as plt


#zad1


im_1=Image.open('obraz.jpg')
print("tryb: ", im_1.mode)
print("format: ", im_1.format)
im_1.show()

# #zad2

T = np.array(im_1)

t_r = T[:,:,0]
t_g = T[:, :,1]
t_b = T[:, :, 2]

im_r = Image.fromarray(t_r)
im_g = Image.fromarray(t_g)
im_b = Image.fromarray(t_b)


im_2 = Image.merge('RGB',(im_r, im_g, im_b))

im_2.show()

print("porównanie obrazow im1 i im2 :")
tmp = ImageChops.difference(im_1, im_2)
tmp.show()

print("Porownanie -> ",im_1==im_2)



# zad3

im1_zad2 = Image.open('obraz.jpg')

r, g, b = im1_zad2.split()

im3 = Image.merge('RGB',(g, r, b))
im3.save('im3.jpg')
im3.save('im3.png')
im3.show()

obraz1 = Image.open("obraz1_1.png")
obraz2 = Image.open("obraz1_1.jpg")
obraz3 = Image.open("obraz1_1N.png")
obraz4 = Image.open("obraz1_1N.jpg")
obraz5 = Image.open("obraz1_2.png")
obraz6 = Image.open("obraz1_2.jpg")
obraz7 = Image.open("obraz1_2N.png")
obraz8 = Image.open("obraz1_2N.jpg")

porwonianie1 = ImageChops.difference(obraz1, obraz2)
porwonianie2 = ImageChops.difference(obraz3, obraz4)
porwonianie3 = ImageChops.difference(obraz5, obraz6)
porwonianie4 = ImageChops.difference(obraz7, obraz8)



plt.figure(figsize=(120, 80))
plt.subplot(4,4,1) 
plt.imshow(porwonianie1)
plt.axis('off')
plt.subplot(4,4,2) 
plt.imshow(porwonianie2)
plt.axis('off')
plt.subplot(4,4,3)
plt.imshow(porwonianie3)
plt.axis('off')
plt.subplot(4,4,4)
plt.imshow(porwonianie4)
plt.axis('off')
plt.subplots_adjust(wspace=0.02, hspace=0.02)
plt.savefig('fig1.png')
plt.show()

#zad4

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

obrazz=Image.open("mw.bmp")

tablica = color_initials(obrazz, [255,255,255])

obrazz_tmp = Image.fromarray(tablica)


temp_r, temp_g, temp_b = obrazz_tmp.split()

picture1 = Image.merge('RGB', (temp_r, temp_b, temp_g))
picture2 = Image.merge('RGB', (temp_g, temp_r, temp_b))
picture3 = Image.merge('RGB', (temp_b, temp_g, temp_r))


plt.figure(figsize=(120, 80))
plt.subplot(2,2,1) 
plt.imshow(obrazz_tmp)
plt.axis('off')
plt.subplot(2,2,2) 
plt.imshow(picture1)
plt.axis('off')
plt.subplot(2,2,3)
plt.imshow(picture2)
plt.axis('off')
plt.subplot(2,2,4)
plt.imshow(picture3)
plt.axis('off')
plt.subplots_adjust(wspace=0.02, hspace=0.02)
plt.savefig('fig2.png')
plt.show()

#zad5


im_tmp = Image.open("moje1.bmp")
im_tmp2 = Image.open("moje2.bmp")
im_tmp3 = Image.open("moje3.bmp")

im_tmp=im_tmp.convert('L')
im_tmp2=im_tmp2.convert('L')
im_tmp3=im_tmp3.convert('L')

obraz_zad5_1 = Image.merge('RGB', (im_tmp, im_tmp2, im_tmp3))
obraz_zad5_2 = Image.merge('RGB', (im_tmp, im_tmp3, im_tmp2))
obraz_zad5_3 = Image.merge('RGB', (im_tmp3, im_tmp2, im_tmp))
obraz_zad5_4 = Image.merge('RGB', (im_tmp3, im_tmp, im_tmp2))
obraz_zad5_5 = Image.merge('RGB', (im_tmp2, im_tmp, im_tmp3))
obraz_zad5_6 = Image.merge('RGB', (im_tmp2, im_tmp3, im_tmp))

plt.figure(figsize=(120, 80))
plt.subplot(3,3,1) 
plt.imshow(obraz_zad5_1)
plt.axis('off')
plt.subplot(3,3,2) 
plt.imshow(obraz_zad5_2)
plt.axis('off')
plt.subplot(3,3,3)
plt.imshow(obraz_zad5_3)
plt.axis('off')
plt.subplot(3,3,4)
plt.imshow(obraz_zad5_4)
plt.axis('off')
plt.subplot(3,3,5)
plt.imshow(obraz_zad5_5)
plt.axis('off')
plt.subplot(3,3,6)
plt.imshow(obraz_zad5_6)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig3.png')
plt.show()




































