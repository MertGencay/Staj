#For Döngüsü

x = [1,2,3,4,5,6,7,8,9,10,"Galatasaray"]
for i in x:
    print(i)

sayi = range(0,101)
for i in sayi:
    print(i)

#For Döngüsü Örnekleri
#Örnek-1
"""
sayi = range(1,1001)
for i in sayi:
    if i%2 == 0:
        print("{} Çift Bir Sayıdır.".format(i))
    elif i%2 == 1:
        print("{} Tek Bir Sayıdır.".format(i))
"""
#Örnek-2
"""
sayi2 = int(input("Lütfen bir tam sayı giriniz:"))
yaz = range(0,sayi2+1)
for i in yaz:
    print(i)
"""
"""
#Örnek-3
toplam = 0
sayi = range(0,100)
for i in sayi:
    toplam += i
print(toplam)
"""

#While Döngüsü

sayi = 0
while sayi <= 100:
    print(sayi)
    sayi += 1

sayi2 = 100
while sayi >= 0:
    print(sayi)
    sayi -= 1

#Break ve Continue

"""
x = "Galatasaray"
for i in x:
    if i == " ":  
        #break   #Boşluk ile karşılaşınca döngüyü sonlandırır
        continue #Boşluk ile karşılaşınca atlayıp döngüye devam eder
    print(i)
"""

#Break ve Continue Örnek
sayac = 2
for i in range(0,3):
    kullanici_adi = input("Kullanıcı Adı:")
    kullanici_sifre = input("Şifre:")
    SistemKA = "Galatasaray"
    SistemSif = "1905"
    if kullanici_adi == SistemKA and kullanici_sifre == SistemSif:
        print("Giriş Başarılı, Hoşgeldiniz...")
        break
    elif (kullanici_adi != SistemKA or kullanici_sifre != SistemSif) and sayac != 0:
        print("Hatalı Giriş Lütfen Tekrar Deneyiniz.Kalan Hakkınız {}".format(sayac))
        sayac -= 1
    else:
        print("Kalan Kullanım Hakkınız {} Kapatılıyor...".format(sayac))
