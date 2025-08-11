#Sayı Tahmin Oyunu
import random

sayı = random.randint(1,101)
hak = 10

while hak > 0:
    tahmin = int(input("Lütfen pozitif bir tam sayı (1-100) girin:"))
    if tahmin < 0:
        print("Girdiğiniz sayı pozitif bir tam sayı değildir!")
        continue
    hak -= 1
    if sayı == tahmin:
        print("Doğru tahmin ettiniz, Tebrikler.")
        break
    elif sayı > tahmin:
        print("Yukarı, Kalan Hakkınız {}".format(hak))
    else:
        print("Aşağı, Kalan Hakkınız {}".format(hak))
    if hak == 0:
        print("Hakkınız kalmamıştır, Doğru sayı {} olacaktır.".format(sayı))