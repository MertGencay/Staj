#Fonksiyon Argümanlar Örnek

def ortalama(*args):
    sonuc = 0
    for i in args:
        sonuc += i
        sonuc2 = sonuc / len(args)
    return round(sonuc2,3)
    
print(ortalama(5,10,14))

def ortalama(*args,x):
    sonuc = 0
    for i in args:
        sonuc += i
        sonuc2 = sonuc / len(args)
    if sonuc2 > x:
        print("{} sayısı ortalamadan küçüktür".format(x))
    else:
        print("{} sayısı ortalamadan büyüktür".format(x))
    return round(sonuc2,3)
    
ortalama(5,10,14,x=25)

def araba(**kwargs):
    for key,value in kwargs.items():
        if value > 250000:
            print("{} marka araba biraz pahalı".format(key))
        else:
            print("{} marka araba biraz daha ucuz".format(key))

araba(Bmw=500000,Audi=350000,Ford=150000)