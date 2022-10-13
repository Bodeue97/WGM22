from PIL import Image
import numpy as np
import sys


np.set_printoptions(threshold=sys.maxsize)




def wstaw_obraz(img, w, h, wsp):
    imgArr=np.asarray(img)*1
    zeroWidth=100*wsp
    zeroHeight=50*wsp
    zeroArr=np.zeros((zeroHeight, zeroWidth), dtype=np.uint8)

    for i in range(h, h+49):
        for j in range(w,w+99):
            if(j<zeroWidth and i < zeroHeight):
                zeroArr[i][j] = imgArr[i - h][j - w]
    zeroArr = zeroArr.astype(bool)
    result = Image.fromarray(zeroArr)
    return result

#
#
#
#
# img = Image.open("inicjały.bmp")
#
# wstaw_obraz(img, 0,0, 1).show()



def zad1(Callable wstaw):
