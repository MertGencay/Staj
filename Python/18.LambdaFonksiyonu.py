#Lambda Fonksiyonu

def toplam(x,y):
    sonuc = x+y
    return sonuc

print(toplam(5,7))

toplam2 = lambda x,y:x+y
print(toplam2(5,7))

kare = lambda sayı:sayı**2
liste = [1,3,5,7,9]
sonuc = list(map(kare,liste))
print(sonuc)