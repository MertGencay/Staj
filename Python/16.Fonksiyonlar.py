#Fonksiyonlar

def toplam(x,y):
    sonuc = x+y
    print(sonuc)  

toplam(5,7)

def toplam(x,y):
    sonuc = x+y
    return sonuc  

print(toplam(5,7) + toplam(6,8))

def toplam(*x):
    sayac = 0
    for i in x:
        sayac += i
    return sayac

print(toplam(1,3,5,7,8,9))

def isim(*y):
    return "Merhaba,benim adım {},soyadım {}".format(y[0],y[1])

print(isim("Mert","Gençay"))

def kalori(**meyve): #sözlük tipinde döndürür
    return meyve

print(kalori(elma=45,armut=50))

def kimlik(**bilgi):
    for i in bilgi.keys():
        print(i)
    for i in bilgi.values():
        print(i)

kimlik(ad="Mert",soyad="Gençay",yas=21)