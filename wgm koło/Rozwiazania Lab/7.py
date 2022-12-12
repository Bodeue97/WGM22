from PIL import Image, ImageFilter, ImageChops
import numpy as np
import matplotlib.pyplot as plt

#zad1

def filtruj(obraz, kernel, scale):
    kopia = obraz.copy()
    obraz_pix = obraz.load()
    kopia_pix = kopia.load()
    w, h = obraz.size
    dlugosc_kernel = len(kernel)
    temp = int(dlugosc_kernel/2)
    for i in range(temp, w-temp):
        for j in range(temp, h-temp):
            tmp = [0,0,0]
            for x in range(dlugosc_kernel):
                for y in range(dlugosc_kernel):
                    xn = i+x-dlugosc_kernel
                    yn = j+y-dlugosc_kernel
                    pixel=obraz_pix[xn, yn]
                    tmp[0] +=pixel[0]*kernel[x][y]
                    tmp[1] += pixel[1] * kernel[x][y]
                    tmp[2] += pixel[2] * kernel[x][y]
            kopia_pix[i, j]=(int(tmp[0]/scale), int(tmp[1]/scale), int(tmp[2]/scale))
    return kopia



obraz_org = Image.open('obraz.jpg')
obraz_kopia2 = obraz_org.copy()
obraz = obraz_org.convert('L')
obraz_kopia1 = obraz.copy()

obraz_kopia1.show()

kernel = [[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1]]
scale = 16

blur = filtruj(obraz_org, kernel, scale)

#zad2

print("blur -> ",ImageFilter.BLUR.filterargs)
blur1 = obraz_org.filter(ImageFilter.BLUR)
blur_porownanie=ImageChops.difference(blur,blur1)

plt.figure(figsize=(32,64))
plt.subplot(1,3,1)
plt.title("blur")
plt.imshow(blur)
plt.axis('off')
plt.subplot(1,3,2)
plt.title("blur1")
plt.imshow(blur1)
plt.axis('off')
plt.subplot(1,3,3)
plt.title("blur\nporownanie")
plt.imshow(blur_porownanie)
plt.axis('off')
plt.subplots_adjust(wspace=0.3, hspace=0.3)
plt.savefig("fig1.png")
plt.show()

#zad3

print(ImageFilter.EMBOSS.filterargs)

sobel_1 = (-1,0,1,-2,0,2,-1,0,1)
sobel_2 = (-1,-2,-1,0,0,0,1,2,1)

ImageFilter.EMBOSS.filterargs = ((3,3), 1, 128, sobel_1)

tmp_obr = obraz_kopia1.filter(ImageFilter.EMBOSS)

ImageFilter.EMBOSS.filterargs = ((3,3),1 ,128, sobel_2)
tmp_obr2 = obraz_kopia1.filter(ImageFilter.EMBOSS)

plt.figure(figsize=(64,32))
plt.subplot(1,3,1)
plt.title("obraz po konwersji na L ")
plt.imshow(obraz_kopia1, 'gray')
plt.axis('off')
plt.subplot(1,3,2)
plt.title("obraz podpunkt a")
plt.imshow(tmp_obr, 'gray')
plt.axis('off')
plt.subplot(1,3,3)
plt.title('obraz podpunkt b')
plt.imshow(tmp_obr2, 'gray')
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig2.png')
plt.show()


#zad4

tmp_ob = obraz_kopia2.filter(ImageFilter.DETAIL)
tmp_ob2 = obraz_kopia2.filter(ImageFilter.EDGE_ENHANCE_MORE)
tmp_ob3 = obraz_kopia2.filter(ImageFilter.SHARPEN)
tmp_ob4 = obraz_kopia2.filter(ImageFilter.SMOOTH_MORE)

obraz_por1 = ImageChops.difference(tmp_ob, obraz_org)
obraz_por2 = ImageChops.difference(tmp_ob2, obraz_org)
obraz_por3 = ImageChops.difference(tmp_ob3, obraz_org)
obraz_por4 = ImageChops.difference(tmp_ob4, obraz_org)




plt.figure(figsize=(32,16))
plt.subplot(1,8,1)
plt.title('DETAIL')
plt.imshow(tmp_ob)
plt.axis('off')
plt.subplot(1,8,2)
plt.title('porównanie')
plt.imshow(obraz_por1)
plt.axis('off')
plt.subplot(1,8,3)
plt.title('EDGE_ENHANCE_MORE')
plt.imshow(tmp_ob2)
plt.axis('off')
plt.subplot(1,8,4)
plt.title('porównanie')
plt.imshow(obraz_por2)
plt.axis('off')
plt.subplot(1,8,5)
plt.title('SHARPEN')
plt.imshow(tmp_ob3)
plt.axis('off')
plt.subplot(1,8,6)
plt.title('porównanie')
plt.imshow(obraz_por3)
plt.axis('off')
plt.subplot(1,8,7)
plt.title('SMOOTH_MORE')
plt.imshow(tmp_ob3)
plt.axis('off')
plt.subplot(1,8,8)
plt.title('porównanie')
plt.imshow(obraz_por4)
plt.axis('off')
plt.subplots_adjust(wspace=0.3, hspace=0.3)
plt.savefig('fig3.png')
# plt.show()

zm1=obraz_org.filter(ImageFilter.GaussianBlur(radius=2))
zm2=obraz_org.filter(ImageFilter.UnsharpMask(radius=2,percent=150,threshold=3))
zm3=obraz_org.filter(ImageFilter.MedianFilter(size=3))
zm4=obraz_org.filter(ImageFilter.MinFilter(size=3))
zm5=obraz_org.filter(ImageFilter.MaxFilter(size=3))

zm1p=ImageChops.difference(obraz_org,zm1)
zm2p=ImageChops.difference(obraz_org,zm2)
zm3p=ImageChops.difference(obraz_org,zm3)
zm4p=ImageChops.difference(obraz_org,zm4)
zm5p=ImageChops.difference(obraz_org,zm5)

plt.figure(figsize=(32,8))
plt.subplot(5,2,1)
plt.title("GaussianBlur(radius=2)")
plt.imshow(zm1,"gray")
plt.axis('off')
plt.subplot(5,2,2)
plt.title("porównanie")
plt.imshow(zm1p,"gray")
plt.axis('off')
plt.subplot(5,2,3)
plt.title("UnsharpMask(radius=2,percent=150,threshold=3)")
plt.imshow(zm2,"gray")
plt.axis('off')
plt.subplot(5,2,4)
plt.title("porównanie")
plt.imshow(zm2p,"gray")
plt.axis('off')
plt.subplot(5,2,5)
plt.title("MedianFilter(size=3)")
plt.imshow(zm3,"gray")
plt.axis('off')
plt.subplot(5,2,6)
plt.title("porównanie")
plt.imshow(zm3p,"gray")
plt.axis('off')
plt.subplot(5,2,7)
plt.title("MinFilter(size=3)")
plt.imshow(zm4,"gray")
plt.axis('off')
plt.subplot(5,2,8)
plt.title("porównanie")
plt.imshow(zm4p,"gray")
plt.axis('off')
plt.subplot(5,2,9)
plt.title("nFilter(size=3)")
plt.imshow(zm5,"gray")
plt.axis('off')
plt.subplot(5,2,10)
plt.title("porównanie")
plt.imshow(zm5p,"gray")
plt.axis('off')
plt.savefig("fig4.png")
# plt.show()


