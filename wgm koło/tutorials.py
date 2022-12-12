from PIL import Image  # Python Imaging Library
import numpy as np



#Lab1 wczytywanie z tablicy i z obrazu
# ---------- wczytywanie obrazu zapisanego w różnych formatach .bmp, .jpg, .png oraz pobieranie informacji o obrazie  -------------------
obrazek = Image.open("lab1/obrazek.bmp")  # wczytywanie obrazu
obrazek.show()
print("---------- informacje o obrazie")
print("tryb:", obrazek.mode)
print("format:", obrazek.format)
print("rozmiar:", obrazek.size)

# ---------- wczytywanie obrazu do tablicy oraz pobieranie informacji o tablicach ------------------------------
dane_obrazka = np.asarray(obrazek)
print("---------------- informqcje o tablicy obrazu----------------")
print("typ danych tablicy:", dane_obrazka.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy:", dane_obrazka.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
print("liczba elementow:", dane_obrazka.size)  # liczba elementów tablicy
print("wymiar tablicy:", dane_obrazka.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...
print("rozmiar wyrazu tablicy:",
      dane_obrazka.itemsize)  # pokazuje ile bajtów trzeba do zapisu wartości elementu
print("pierwszy wyraz:", dane_obrazka[0][0])
print("drugi wyraz:", dane_obrazka[1][0])
print("***************************************")
print(dane_obrazka)  # mozna odkomentować, zeby zobaczyć tablicę

# ------------------------   wczytywanie obrazu do tablicy z jednoczesnym okresleniem typu danych ---------------------
dane_obrazka1 = dane_obrazka * 1  # zmienia typ bool na int
print(dane_obrazka1)
ob_d = Image.fromarray(dane_obrazka)  # tworzenie obrazu z tablicy dane_obrazka (typ bool)
# ----- wyswietlanie informacji o obrazie -----------------------------
print("-------informacje o obrazie ob_d ------------")
print("tryb:", ob_d.mode)
print("format:", ob_d.format)
print("rozmiar:", ob_d.size)
ob_d.show()

print("-------informacje o obrazie ob_d1 ------------")
ob_d1 = Image.fromarray(dane_obrazka1)  # tworzenie obrazu z tablicy dane_obrazka1 (typ int)
# ----- wyswietlanie informacji o obrazie -----------------------------
print("tryb:", ob_d1.mode)
print("format:", ob_d1.format)
print("rozmiar:", ob_d1.size)
ob_d1.show()
# WAŻNE PYTANIE NA NASTEPNE ZAJECIA!!!  DLACZEGO ob_d1 widać jako obraz czarny?


# ---------------- zapisywanie obrazu do pliku -----------------
ob_d.save(
    "lab1/obraz_zapisany.bmp")  # jako argument podajemy nazwę pliku wraz z rozszerzeniem, bo w zależności od tego w jakim formacie zapiszemy otrzymamy różne tablice obrazu

print("-------------------------------------------")

# wczytywanie tablicy z pliku UWAGA! plik txt powinien zawierac same zera i jedynki oddzielane spacjami bez dodatkowych znaków jak w pliku dane.txt
t1 = np.loadtxt("lab1/dane.txt", dtype=np.bool_)
t2 = np.loadtxt("lab1/dane.txt", dtype=np.int_)

# w zależnosci od tego, jakie operacje chcemy zrobić na tablicy, wybieramy jedną z powyższych postaci tablicy
print("typ danych tablicy t1:", t1.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy t1 :", t1.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
print("wymiar tablicy t1 :", t1.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...

print("typ danych tablicy t2:", t2.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy t2 :", t2.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
print("wymiar tablicy t2 :", t2.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...

print("---- porównywanie tablic ------")
nowa_t1 = np.loadtxt("lab1/dane1.txt", dtype=np.bool_)  # wczytanie tablicy z pliku dane1.txt
nowa_t1_1 = nowa_t1 * 1  # zamiana bool na tablice zero-jedynkową
print("----- nowa_t1 ---------")
print(nowa_t1)
print("------ nowa_t1_1 --------")
print(nowa_t1_1)
porownanie = nowa_t1 == nowa_t1_1  # zwraca TRUE jesli tablice są identyczne (przy czym True = 1, False = 0), w przeciwnym przypadku False
czy_rowne = porownanie.all()
print("czy tablice sa równe? ", czy_rowne)

print("------ drugi przykład -------------------")
nowa_t2 = np.loadtxt("lab1/dane1.txt", dtype=np.int_)  # wczytanie tablicy z pliku dane1.txt
print("--- nowa_t2 -----------")
print(nowa_t2)
print("----- t2 ---------")
print(t2)
porownanie2 = t2 == nowa_t2  # tablica, która ma wartośc True jesli elementy w odpowieednich miejscach sa równe i False w p.p.
print("------ tablica porownanie -------")
print(porownanie2)

# zliczanie ile jest równych elementów
print("wszystkich elementów tablicy t2 jest: ", t2.size)
print("wszystkich elementów tablicy nowa_t2 jest: ", nowa_t2.size)
print("równych elementów jest: ", np.sum(t2 == nowa_t2))  # zlicza ile elementów jest takich samych
print("równych elementów jest: ", np.sum(porownanie2))  # zlicza ile elementów jest takich samych (drugi sposób)

# zapis tablicy do pliku
t2_text = open('lab1/t2.txt', 'w')
for rows in t2:
    for item in rows:
        t2_text.write(str(item) + ' ')
    t2_text.write('\n')

t2_text.close()

#Lab2 wstawianie w obraz, ramki itd


inicjaly = Image.open("lab2/bs.bmp") # wczytywanie obrazu
# obrazek.show()
print("tryb", inicjaly.mode)
print("format", inicjaly.format)
print("rozmiar", inicjaly.size)


t_inicjaly = np.asarray(inicjaly)
print("typ danych tablicy", t_inicjaly.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy", t_inicjaly.shape)  # rozmiar tablicy - warto porównac z wymiarami obrazka
print("***************************************")

def wstaw_inicjaly(t_inicjaly):
    h0, w0 = t_inicjaly.shape
    print(h0,w0)
    t = (2*h0, 2*w0) # rozmiar tablicy
    tab = np.zeros(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
    for i in range(25, 25+h0-1):
        for j in range(50, 50+w0-1):
            tab[i][j]=t_inicjaly[i-25][j-50]
    tab = tab.astype(bool)
    po_wstawieniu = Image.fromarray(tab)
    return po_wstawieniu
po_wstawieniu = wstaw_inicjaly(t_inicjaly)
po_wstawieniu.show()

def rysuj_ramke(w, h, dzielnik):
    t = (h, w)  # rozmiar tablicy
    tab = np.zeros(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
    grub = int(min(w, h) / dzielnik)  # wyznaczenie grubości  ramki
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2] = 1  # skrócona wersja ustawienia wartości dla prostokatnego fragmentu tablicy [zakresy wysokości, zakresy szerokości] tablicy
    return tab * 255  # alternatywny sposób uzyskania tablicy obrazu czarnobiałego ale w trybie odcieni szarości


tab = rysuj_ramke(120, 60, 8)
im_ramka = Image.fromarray(tab)
im_ramka.show()

def rysuj_pasy_poziome(w, h, dzielnik): # w, h   -  rozmiar obrazu
    t = (h, w)  # rozmiar tablicy
    tab = np.ones(t, dtype=np.uint8)
    # jaki bedzie efekt, gdy np.ones zamienimy na np.zeros?
    grub = int(h / dzielnik)  # liczba pasów = 9 o grubości 10
    print(grub)
    for k in range(dzielnik):  # uwaga k = 0,1,2,3,4,5,8   bez dziewiatki
        for g in range(grub):
            i = k * grub + g  # i - indeks wiersza, j - indeks kolumny
            for j in range(w):
                tab[i, j] = k % 2  # reszta z dzielenia przez dwa
    tab = tab * 255 # alternatywny sposób uzyskania tablicy obrazu czarnobiałego ale w trybie odcieni szarości
    obraz = Image.fromarray(tab)  # tworzy obraz
    obraz.show()

rysuj_pasy_poziome(400, 630, 9)





#Lab3  Tryby obrazów i wartości w tablicach



# obrazy w odcieniach szarości
def rysuj_ramke_szare(w, h, dzielnik, kolor_ramki, kolor):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor_ramki  # wypełnienie tablicy szarym kolorem o wartości kolor_ramki
    grub = int(min(w, h) / dzielnik)  # wyznaczenie grubości  ramki
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2] = kolor  # wypełnienie podtablicy kolorem o wartości kolor
    return tab


tab = rysuj_ramke_szare(120, 60, 8, 100, 200)
im_ramka = Image.fromarray(tab)
im_ramka.show()


def rysuj_pasy_poziome_szare(w, h, dzielnik, zmiana_koloru):  # w, h   -  rozmiar obrazu
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    grub = int(h / dzielnik)
    for k in range(dzielnik):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                tab[i, j] = (k * zmiana_koloru) % 256
    return tab


tab1 = rysuj_pasy_poziome_szare(300, 200, 100, 10)
obraz1 = Image.fromarray(tab1)
obraz1.show()


def negatyw_szare(tab):  # tworzy tablicę dla negatywu
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i, j] = 255 - tab[i, j]
    return tab_neg


tab_neg = negatyw_szare(tab1)
obraz_neg = Image.fromarray(tab_neg)
obraz_neg.show()


def rysuj_po_przekatnej_szare(w):  # rysuje kwadratowy obraz
    t = (w, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(w):
        for j in range(w):
            tab[i, j] = (i + j) % 256
    return tab


tab = rysuj_po_przekatnej_szare(512)
im = Image.fromarray(tab)
im.show()


def rysuj_ramki_szare(w, zmiana_koloru):
    t = (w, w)
    tab = np.zeros(t, dtype=np.uint8)
    kolor = 255 - int(w / 2) + 1
    z = w
    for k in range(int(w / 2)):
        for i in range(k, z - k):
            for j in range(k, z - k):
                tab[i, j] = kolor
        kolor = kolor + zmiana_koloru
    return tab


tab = rysuj_ramki_szare(300, 5)
im = Image.fromarray(tab)
im.show()


# obrazy kolorowe
def rysuj_ramke_kolor(w, h, dzielnik, kolor_ramki, kolor):  # kolor_ramki, kolor podajemy w postaci [r, g, b]
    t = (h, w, 3)  # rozmiar tablicy
    tab = np.ones(t, dtype=np.uint8)  # deklaracja tablicy
    tab[:] = kolor_ramki  # wypełnienie tablicy kolorem czerwonym
    grub = int(min(w, h) / dzielnik)  # wyznaczenie grubości  ramki
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2, 0] = kolor[0]  # wypełnienie wartości kanału R liczbą r
    tab[grub:z1, grub:z2, 1] = kolor[1]  # wypełnienie wartości kanału G liczbą g
    tab[grub:z1, grub:z2, 2] = kolor[2]  # wypełnienie wartości kanału R liczbą r
    # tab[grub:z1, grub:z2] = kolor # wersja równoważna
    return tab


tab = rysuj_ramke_kolor(120, 60, 8, [0, 0, 255], [100, 200, 0])
im_ramka = Image.fromarray(tab)
im_ramka.show()


def rysuj_pasy_poziome_3kolory(w, h, dzielnik):  # funkcja rysuje pasy poziome na przemian czerwony, zielony, niebieski
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    grub = int(h / dzielnik)
    for k in range(dzielnik):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                if k % 3 == 0:
                    tab[i, j] = [255, 0, 0]
                elif k % 3 == 1:
                    tab[i, j] = [0, 255, 0]
                else:
                    tab[i, j] = [0, 0, 255]
    return tab


tab1 = rysuj_pasy_poziome_3kolory(300, 200, 20)
obraz1 = Image.fromarray(tab1)
obraz1.show()


def rysuj_pasy_poziome_kolor(w, h, dzielnik, kolor,
                             zmiana_koloru):  # funkcja rysuje pasy poziome, przy czym kazda składowa koloru zwieksza się o "zmiana_koloru"
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor
    grub = int(h / dzielnik)
    for k in range(dzielnik):
        r = (kolor[0] + k * zmiana_koloru) % 256
        g = (kolor[1] + k * zmiana_koloru) % 256
        b = (kolor[2] + k * zmiana_koloru) % 256
        for m in range(grub):
            i = k * grub + m
            for j in range(w):
                tab[i, j] = [r, g, b]
    return tab


tab1 = rysuj_pasy_poziome_kolor(300, 200, 20, [100, 200, 0], 32)
obraz1 = Image.fromarray(tab1)
obraz1.show()


def koloruj_obraz(obraz, kolor):
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape
    t =(h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if t_obraz[i, j] == False:
                tab[i, j] = kolor
            else:
                tab[i, j] = [255, 255, 255]
    return tab

gwiazdka = Image.open("lab3/gwiazdka.bmp")
obraz2 = Image.fromarray(koloruj_obraz(gwiazdka, [120, 240, 50]))
obraz2.show()

def rysuj_ramki_kolorowe(w, zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    t = (w, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    kolor_r = 0
    kolor_g = 0
    kolor_b = 0
    z = w
    for k in range(int(w / 2)):
        for i in range(k, z - k):
            for j in range(k, z - k):
                tab[i, j] = [kolor_r, kolor_g, kolor_b]
        kolor_r = kolor_r + zmiana_koloru_r
        kolor_g = kolor_g + zmiana_koloru_g
        kolor_b = kolor_b + zmiana_koloru_b
    return tab


tab = rysuj_ramki_kolorowe(300, 2, 4, 6)
obraz3 = Image.fromarray(tab)
obraz3.show()



#Lab4 pobieranie i mieszanie kanałów rgb, kompresja obrazów




im = Image.open('lab4/jesien.jpg')
print("tryb", im.mode)
print("format", im.format)
print("rozmiar", im.size)
h, w = im.size
im.show()

# tablica obrazu
T = np.array(im)
#tablica kanału r
t_r = T[:, :, 0]
im_r = Image.fromarray(t_r) # obraz w odcieniuach szarości kanału r
print("tryb", im_r.mode)
#tablica kanału g
t_g = T[:, :, 1]
im_g = Image.fromarray(t_g) # obraz w odcieniuach szarości kanału g
print("tryb", im_g.mode)
#tablica kanału b
t_b = T[:, :, 2]
im_b = Image.fromarray(t_b) # obraz w odcieniuach szarości kanału b
print("tryb", im_b.mode)


# przedstawienie 4 obrazów w jednym oknie plt
plt.figure(figsize=(32, 16))
plt.subplot(2,2,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(im)
plt.axis('off')
plt.subplot(2,2,2)
plt.imshow(im_r, "gray")
plt.axis('off')
plt.subplot(2,2,3)
plt.imshow(im_g, "gray")
plt.axis('off')
plt.subplot(2,2,4)
plt.imshow(im_b, "gray")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('lab4/figura1.png')
plt.show()




# Kanały pobrane jako obrazy
r, g, b = im.split()  # powstają obrazy
print("tryb", r.mode)
print("tryb", g.mode)
print("tryb", b.mode)
diff_r = ImageChops.difference(r, im_r)
diff_g = ImageChops.difference(g, im_g)
diff_b = ImageChops.difference(b, im_b)


plt.figure(figsize=(32, 16))
plt.subplot(3,4,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(im)
plt.axis('off')
plt.subplot(3,4,2)
plt.imshow(im_r, "gray")
plt.axis('off')
plt.subplot(3,4,3)
plt.imshow(im_g, "gray")
plt.axis('off')
plt.subplot(3,4,4)
plt.imshow(im_b, "gray")
plt.axis('off')
plt.subplot(3,4,5)
plt.imshow(im)
plt.axis('off')
plt.subplot(3,4,6)
plt.imshow(r, "gray")
plt.axis('off')
plt.subplot(3,4,7)
plt.imshow(g, "gray")
plt.axis('off')
plt.subplot(3,4,8)
plt.imshow(b, "gray")
plt.axis('off')
plt.subplot(3,4,9)
plt.imshow(im)
plt.axis('off')
plt.subplot(3,4,10)
plt.imshow(diff_r, "gray")
plt.axis('off')
plt.subplot(3,4,11)
plt.imshow(diff_g, "gray")
plt.axis('off')
plt.subplot(3,4,12)
plt.imshow(diff_b, "gray")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.show()

# zapis kanałów do tablic
r_T = np.array(r)
g_T = np.array(g)
b_T = np.array(b)

# porównanie tablic
print("--------porównanie tablic--------------")
porownanie = r_T == t_r
czy_rowne = porownanie.all()
print(czy_rowne)
print("----------------------")



im1 = Image.merge('RGB', (im_r, im_g, im_b))
im2 = Image.merge('RGB', (r, g, b)) # zamień r na im_r i sprawdź efekt
# im1.show()
# im2.show()
diff_im = ImageChops.difference(im1,im2)
diff_im.show()

# mieszanie kanałow
im3 = Image.merge('RGB', (r, b, g))
im3.show()



# konwersja na  obraz w odcieniach szarości
w1 = 0.3
w2 = 0.8
w3 = 0.2
szary = w1 * r_T + w2 * g_T + w3 * b_T
szary_im = Image.fromarray(szary)
szary_im.show()


# własna tablica "L" jako kanał
t = (w, h)
A = np.zeros(t, dtype=np.uint8)
A_im = Image.fromarray(A)

im4 = Image.merge('RGB', (r, A_im, b))
im4.show()


# własna tablica "L" jako kanał - drugi przykład
B = np.ones(t, dtype=np.uint8)
for i in range(w):
    for j in range(h):
        B[i, j] = (i + j) % 256

B_im = Image.fromarray(B)
B_im.show()
im6 = Image.merge('RGB', (B_im, g, b))
im6.show()




#Lab5  metody   getpixel, putpixel, load, point


im = Image.open('lab5/baby_yoda.jpg')
print("tryb obrazu", im.mode)
print("rozmiar", im.size)
im.show()


def zakres(w, h):  # funkcja, która uprości podwójna petle for
    return [(i, j) for i in range(w) for j in range(h)]


# ***********************************************************************************************************************8
# zmiana wartości pikseli za pomocą metod getpixel i putpixel
def pobierz_kolor_pixela(obraz, m, n):  # m, n współrzędne punktu na obrazie
    w, h = obraz.size
    if m < w and n < h:
        kolor = obraz.getpixel((m, n))
    return kolor


print(pobierz_kolor_pixela(im, 260, 200))


def wstaw_pixel_w_punkt(obraz, m, n, kolor):  # m, n współrzędne punktu na obrazie, kolor -  dane pixela do wstawienia
    w, h = obraz.size
    if m < w and n < h:
        obraz.putpixel((m, n), kolor)
    return obraz


def wstaw_pixel_w_zakresie(obraz, m, n, kolor, w_z, h_z):  # w miejscu m,n wstawia kwadrat o boku 100 w kolorze "kolor"
    w, h = obraz.size
    for i, j in zakres(w_z, h_z):
        if i + m < w and j + n < h:
            obraz.putpixel((i + m, j + n), kolor)
    return obraz


def rozjasnij_obraz_putpixel(obraz, a, b, c):  # zmienia wartości każdego kanału
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i, j in zakres(w, h):
        p = obraz.getpixel((i, j))
        obraz1.putpixel((i, j), (p[0] + a, p[1] + b, p[2] + c))
    return obraz1


def rozjasnij_obraz_w_zakresie(obraz, m, n, a, b, c, w_z, h_z):  # w miejscu m,n "rozjaśnia" prostokat o wymiaraxh w_z, h_z
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i, j in zakres(w_z, h_z):
        if i + m < w and j + n < h:
            p = obraz.getpixel((i + m, j + n))
            obraz1.putpixel((i + m, j + n), (p[0] + a, p[1] + b, p[2] + c))
    return obraz1


def skopiuj_obraz_w_zakresie(obraz, m, n, m1, n1, w_z, h_z):  # kopiuje prostokat o wymiarach w_z, h_z z miejsca m,n i wstawia w miejscu m1,n1
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i, j in zakres(w_z, h_z):
        if i+m < w and j+n < h:
            p = obraz.getpixel((i + m, j + n))
            if i + m1 < w and j + n1 < h:
                obraz1.putpixel((i + m1, j + n1), p)
    return obraz1


def rozjasnij_obraz_z_maska(obraz, maska, m, n, a, b, c):  # w miejscu m, n zmienia tylko te pixele, które odpowiadają czarnym pixelom maski, maska jest obrazem czarnobiałym
    obraz1 = obraz.copy()
    w, h = obraz.size
    w0, h0 = maska.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if maska.getpixel((i, j)) == 0:
                p = obraz.getpixel((i + m, j + n))
                obraz1.putpixel((i + m, j + n), (p[0] + a, p[1] + b, p[2] + c))
    return obraz1


def dodaj_szum(obraz, n, kolor1, kolor2):  # dodawanie szumu typu salt and pepper
    w, h = obraz.size
    x, y = np.random.randint(0, w, n), np.random.randint(0, h,
                                                         n)  # powtarza n razy losowanie z zakresu 0,w i z zakresu 0,h
    for (i, j) in zip(x, y):  # zip robi pary z list x,y
        obraz.putpixel((i, j), (kolor1 if np.random.rand() < 0.5 else kolor2))  # salt-and-pepper
    return obraz


#
im1 = im.copy()
im2 = im.copy()
im3 = im.copy()
im4 = im.copy()
im5 = im.copy()
maska = Image.open('lab5/gwiazdka.bmp')
im6 = im.copy()

plt.title("1. wstaw_pixel_w_zakresie")
plt.axis('off')
plt.imshow(wstaw_pixel_w_zakresie(im1, 200, 100, (200, 200, 200), 100, 100))
plt.show()

plt.title("2. rozjasnij_obraz_putpixel")
plt.axis('off')
plt.imshow(rozjasnij_obraz_putpixel(im2, 50, 20, -10))
plt.show()

plt.title("3. rozjasnij_obraz_w_zakresie")
plt.axis('off')
plt.imshow(rozjasnij_obraz_w_zakresie(im3, 200,100, 50, 20, -10, 100, 100))
plt.show()

plt.title("4. skopiuj_obraz_w_zakresie")
plt.axis('off')
plt.imshow(skopiuj_obraz_w_zakresie(im4, 70, 300, 240, 200, 60, 60))
plt.show()

# plt.title("4.1 skopiuj_obraz_w_zakresie")
# plt.axis('off')
# plt.imshow(skopiuj_obraz_w_zakresie(im4, 40, 300, 750, 500, 100, 100))
# plt.show()

plt.title("5. rozjasnij_obraz_z_maska")
plt.axis('off')
plt.imshow(rozjasnij_obraz_z_maska(im5, maska, 200, 100, 50, 20, -10))
plt.show()


plt.title("6.  dodaj_szum")
plt.axis('off')
plt.imshow(dodaj_szum(im6, 50000, (0, 0, 0), (255, 255, 255)))
plt.show()


# ****************************************************************
# zmiana wartości pikseli za pomocą metody  load


# funkcja wykorzystująca inne funkcje na wartościach pikseli
def zastosuj_funkcje(image, func):
    w, h = image.size
    pixele = image.load()
    for i, j in zakres(w, h):
        pixele[i, j] = func(pixele[i, j])


def przestaw_kolory(pixel):
    return (pixel[1], pixel[2], pixel[0])


def filtr_liniowy(image, a, b): # a, b liczby całkowite
    w, h = image.size
    pixele = image.load()
    for i, j in zakres(w, h):
        pixele[i, j] = (pixele[i, j][0]* a + b, pixele[i, j][1]* a + b, pixele[i, j][2]* a + b)


im7 = im.copy()
zastosuj_funkcje(im7, przestaw_kolory)
plt.title("7. Metoda load i funkcja przestaw_kolory  ")
plt.axis('off')
plt.imshow(im7)
plt.show()

im8 = im.copy()
filtr_liniowy(im8, 2, -100)
plt.title("8. Metoda load i funkcja filtr_liniowy ")
plt.axis('off')
plt.imshow(im8)
plt.show()

# ****************************************************************


# zmiana wartości pikseli za pomocą metody  point
im9 = im.copy()
im9 = im9.point(lambda i: i + 100)
plt.title("9.  Metoda point - rozjasnij ")
plt.axis('off')
plt.imshow(im9)
plt.show()


# ****************************************************************

# obcięcie wartości pixeli do pewnej wartości wsp

def efekt_plakatu(im, wsp):
    return im.point(lambda
                        i: i > wsp and 255)  # sztuczka Pythona - jeżeli nieprawda, że i > wsp wstaw 0 a w przeciwnym przypadku wstaw 255


def efekt_plakatu_rownowaznie(im, wsp):
    r, g, b = im.split()
    # każdy z kanałow zmieniamy na obraz czarnobiały w trybie "L"
    r1 = r.point(lambda i: i > wsp and 255)
    r1.show()
    g1 = g.point(lambda i: i > wsp and 255)
    b1 = b.point(lambda i: i > wsp and 255)
    return Image.merge("RGB", (r1, g1, b1))


plt.title("10.   Metoda point - efekt plakatu ")
plt.axis('off')
plt.imshow(efekt_plakatu(im, 100))
plt.show()
# --------------------

# dlaczego poniższe polececiania nie rozjasniaja obrazu tak jak funkcja "rozjaśnij"
obraz = im.copy()
T = np.array(obraz, dtype='uint8')
T += 100
obraz_wynik = Image.fromarray(T, "RGB")
plt.title("11.   Zmiana wartosci tablicy ")
plt.axis('off')
plt.imshow(obraz_wynik)
plt.show()



#Lab7  filtrowanie obrazów


im = Image.open('lab7/baby_yoda.jpg')
print("tryb obrazu", im.mode)
print("rozmiar", im.size)

#  Class   PIL.ImageFilter.Kernel(size, kernel, scale=None, offset=0) -- scale jest zazwyczaj sumą wyrazów w kernel, w algorytmie kernel normalizujemy dzieląc przez scale
fe = im.filter(ImageFilter.FIND_EDGES) # filtruje obraz im
fe.show()
print(ImageFilter.FIND_EDGES.filterargs)  # wyświetla argumenty, w tym rozmiar i  wartości tablicy Kernel

ImageFilter.FIND_EDGES.filterargs = ((3, 3), 1, 0, (-1, -1, -1, -1, 6, -1, -1, -1, -1)) # pozwala zmieniac wartości listy Kernel, skalę i offset.
fe1 = im.filter(ImageFilter.FIND_EDGES) # filtruje obraz im
fe1.show()

ImageFilter.FIND_EDGES.filterargs = ((3, 3), 1, 0, (-1, -1, -1, -1, 8, -1, -1, -1, -1)) # pozwala zmieniac wartości listy Kernel, skalę i offset.
fe3 = im.filter(ImageFilter.FIND_EDGES) # filtruje obraz im
fe3.show()
fe_ker = im.filter(ImageFilter.Kernel(size = (3, 3), kernel = (-1, -1, -1, -1, 8, -1, -1, -1, -1), scale=1, offset=0))
fe_ker.show()
roznica = ImageChops.difference(fe3, fe_ker)
roznica.show()


#Lab8 statystyki obrazu, histogram, filtrowanie przez histogram


def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe


#************************************************************************************************************
im = Image.open('brain.png')
print(im.mode)
statystyki(im)

plt.title("brain oryginalny ")
plt.axis('off')
plt.imshow(im, 'gray')
plt.show()

szary = im.convert("L")
statystyki(szary)
#print(szary.histogram())

im_equalized1 = ImageOps.equalize(szary, mask=None) # https://pillow.readthedocs.io/en/stable/reference/ImageOps.html
plt.title("brain wyrównany ")
plt.axis('off')
plt.imshow(im_equalized1, 'gray')
plt.show()
statystyki(im_equalized1)



#________________________________________________________________

im = Image.open('mgla.jpg') # obraz kolorowy

im.show()

statystyki(im)
hist = im.histogram()
plt.title("histogram - mgła ")
plt.bar(range(256), hist[:256], color='r', alpha=0.5)
plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
plt.show()

r, g, b = im.split()
# wyrównanie każdego kanału oddzielnie
r_eq = ImageOps.equalize(r)
g_eq = ImageOps.equalize(g)
b_eq = ImageOps.equalize(b)
im1 = Image.merge('RGB', (r_eq, g_eq, b_eq))
im1.show()

# wyrównaie obrazu RGB
im_equalized1 = ImageOps.equalize(im, mask=None)
im_equalized1.show()

#porównanie
diff=ImageChops.difference(im_equalized1, im1)
print("statystyki róznicy -------------------------------")
statystyki(diff)

# konwersja na szary i wyrównanie
im3 = im.convert("L")
im3.show()
im3_eq = ImageOps.equalize(im3)
im3_eq.show()



#Lab9  RGBA, CMYK, YCbCr, HSV, metoda paste




# LA kanał alfa dodany do obrazu L, RGBA kanał alfa dodany do obrazu RGB
shrek = Image.open("Shrek_Fiona.png")
tryby = ['1', 'L', 'LA',  'RGB','RGBA','CMYK','YCbCr','HSV',"I",'F']
plt.figure(figsize=(16, 16))
i=1
for t in tryby:
    file_name = "tryb_"+ str(t)
    im_c = shrek.convert(t)
    plt.subplot(4, 3, i)
    plt.title(str(file_name))
    plt.imshow(im_c, "gray")
    plt.axis('off')
    i +=1
plt.show()

r,g,b,a = shrek.split()
a.show()

shrek_RGB = Image.new('RGB', shrek.size, (255,255,255)) # nowy obraz wypełniony na biało
shrek_RGB.paste(shrek, (0, 0), a)
print('tryb obrazu', shrek_RGB.mode)
shrek_RGB.show()

shrek_RGB.putalpha(a)
shrek_RGB.show()

tlo = Image.open('tlo.png')
print(shrek.size, tlo.size)
tlo = tlo.resize(shrek.size, 1)
print(shrek.size, tlo.size)
tlo.show()

tlo0 = tlo.copy()
tlo0.paste(shrek, (200,300))
tlo0.show()

tlo1 = tlo.copy()
tlo1.paste(shrek, (0, 0), a) #shrek wklejony w tlo1 z maska a (kanał alpha obrazu shrek)
tlo1.show()

shrek1 = shrek.copy()
shrek1.paste(tlo, (0, 0), a) #  tlo wklejone w shrek1  z maska a
shrek1.show()





