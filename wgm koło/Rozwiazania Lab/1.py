from cmath import pi
from PIL import Image
import numpy as np
import sys
import random
np.set_printoptions(threshold=sys.maxsize)

picture = Image.open("C://Users//Maciek//Desktop//Projekt1//inicjaly.bmp")
picture.show()

list_picture_info = []

tmp = picture.mode
tmp2 = "Tryb obrazka -> "
list_picture_info.append(tmp2+tmp)

tmp3 = picture.format
tmp4 = "Format obrazka -> "
list_picture_info.append(tmp4+tmp3)

tmp5 = picture.size
tmp5=str(tmp5)
tmp6 = "Rozmiar obrazka -> "
list_picture_info.append(tmp6+tmp5)

print(list_picture_info)

data_picture = np.asarray(picture)

# data_picture1 = data_picture*1
# f = open("inicjaly.txt", mode='w')
# data_picture1 = str(data_picture1)
# f.writelines(data_picture1)
# f.close()

print("typ danych tablicy -> ", data_picture.dtype)  
print("rozmiar tablicy -> ", data_picture.shape)  
print("liczba elementow -> ", data_picture.size)  
print("wymiar tablicy -> ", data_picture.ndim)
print("rozmiar wymiaru tablicy -> ", data_picture.itemsize)

temp = random.randint(0, 45)
temp2 = random.randint(0, 45)


print(f"Wartość piksela1 ({temp2}, {temp}) -> ", data_picture[temp][temp2])

temp3 = random.randint(0, 45)
temp4 = random.randint(0, 45)

print(f"Wartość piksela2 ({temp4}, {temp3}) -> ", data_picture[temp3][temp4])

print("Wartość piksela o adresie (50,30) -> ", data_picture[30][50])
print("Wartość piksela o adresie (90,40) -> ", data_picture[40][90])
print("Wartość piksela o adresie (99,0) -> ", data_picture[0][99])
print("Wartość piksela o adresie (22,9) -> ", data_picture[9][22]) #sprawdzenie dla wartości zero z tablicy, czy program działa poprawnie

picture_booltype = np.loadtxt('inicjaly.txt', dtype=np.bool_)

print("Porówanie obrazka inicjaly.bmp z obrazkiem typu bool_ -> ",np.array_equal(data_picture, picture_booltype))

picture_inttype = np. loadtxt('inicjaly.txt', dtype=np.int_)

print("Porówanie obrazka inicjaly.bmp z obrazkiem typu int_ -> ",np.array_equal(data_picture, picture_inttype))

picture_from_array = Image.fromarray(picture_inttype)
picture_from_array.show()


















