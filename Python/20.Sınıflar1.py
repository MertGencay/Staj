#Nesne Yönelimli Programlama (OOP) - Sınıf Yaratmak

class Insan:
    ad = "Mert"
    soyad = "Gençay"
    yaş = 21
    sacrengi = "Siyah"

print(Insan.ad)
print(Insan.sacrengi)

#x = Insan()
#print(type(x)) #<class '__main__.Insan'>

class insan:
    def __init__(self,ad,soyad,yaş,sacrengi):
        self.ad = ad
        self.soyad = soyad
        self.yaş = yaş
        self.sacrengi = sacrengi

insan1 = insan("Leroy","Sane",29,"Siyah")
insan2 = insan("Victor","Osimhen",26,"Sarı")

print(insan1.ad)
print(insan2 .ad)