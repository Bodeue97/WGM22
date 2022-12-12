from PIL import Image, ImageOps, ImageChops, ImageFilter
from PIL import ImageStat as stat
import numpy as np
import matplotlib.pyplot as plt

def statystyki(im) -> None:
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

obraz_medyczny = Image.open('stopa.jpg')
print(obraz_medyczny.mode)

obraz_medyczny=obraz_medyczny.convert('L')
print(obraz_medyczny.mode)
obraz_medyczny.show()

hit= obraz_medyczny.histogram()
plt.plot(range(256), hit[:], color='blue', alpha = 0.5)
plt.show()


#zad2

statystyki(obraz_medyczny)
histog = obraz_medyczny.histogram()
print(histog)


#zad3

def histogram_norm(picture) -> None:
    w ,h= picture.size
    liczba_pikseli = w*h
    print(liczba_pikseli)
    hist = picture.histogram()
    for i in range(len(hist)):
        hist[i]=hist[i]/liczba_pikseli
    return hist

tmp = histogram_norm(obraz_medyczny)
print(tmp)
plt.title('histogram znormalizowany')
plt.plot(range(256), tmp[:], color = 'g', alpha=0.5)
plt.show()

#zad4

def histogram_cumul(picture):
    histo_znormalizowany = histogram_norm(picture)
    hist_kumul = []
    hist_kumul.append(histo_znormalizowany[0])
    for i in range(1,len(histo_znormalizowany)):
        hist_kumul.append(hist_kumul[i-1]+histo_znormalizowany[i])
    return hist_kumul


tmp2 = histogram_cumul(obraz_medyczny)
print(tmp2)
plt.title('histogram skumulowany')
plt.plot(range(256), tmp2[:], color = 'r', alpha=0.5)
plt.show()

def histogram_equalization(picture):
    hist_cumul = histogram_cumul(picture)
    obraz = picture.point(lambda i: int(255*hist_cumul[i]))
    return obraz

tmp3 = histogram_equalization(obraz_medyczny)
tmp3.save('equalized.png')
tmp3.show()

obraz_test = ImageOps.equalize(obraz_medyczny)
obraz_test.save('equalized1.png')
obraz_test.show()

porownanie = ImageChops.difference(tmp3, obraz_test)
porownanie.show()

histogram1 = tmp3.histogram()
histogram2 = obraz_test.histogram()

im = Image.open('hist1.PNG')
im2 = Image.open('hist2.PNG')


plt.figure(figsize=(120, 80))
plt.subplot(2,2,1)
plt.imshow(im)
plt.axis('off')
plt.subplot(2,2,2)
plt.imshow(im2)
plt.axis('off')
plt.subplots_adjust(wspace=0.02, hspace=0.02)
plt.savefig('fig1.png')
plt.show()
print('\n')
print(statystyki(tmp3))
print('\n','=========================')
print(statystyki(obraz_test))

#zad7

obraz_medyczny_detail = obraz_medyczny.filter(ImageFilter.DETAIL)
obraz_medyczny_detail.show()

obraz_medyczny_shapren = obraz_medyczny.filter(ImageFilter.SHARPEN)
obraz_medyczny_shapren.show()

obraz_medyczny_contour = obraz_medyczny.filter(ImageFilter.CONTOUR)
obraz_medyczny_contour.show()

plt.figure(figsize=(120, 80))
plt.subplot(4,4,1)
plt.title('Detail')
plt.imshow(obraz_medyczny_detail, 'gray')
plt.axis('off')
plt.subplot(4,4,2)
plt.title('sharpen')
plt.imshow(obraz_medyczny_shapren, 'gray')
plt.axis('off')
plt.subplot(4,4,3)
plt.title('Contour')
plt.imshow(obraz_medyczny_contour, 'gray')
plt.axis('off')
plt.subplot(4,4,4)
plt.title('egalized1.png')
plt.imshow(obraz_test, 'gray')
plt.axis('off')
plt.subplots_adjust(wspace=0.02, hspace=0.02)
plt.savefig('filtry.png')
plt.show()
