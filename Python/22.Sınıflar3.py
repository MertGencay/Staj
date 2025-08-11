#Nesne Yönelimli Programlama (OOP) - Miraslama/Kalıtım (Inheritance)

class Insan():
    def __init__(self,Ad,Soyad,Sacrengi,Boy,Kilo):
        self.Ad = Ad
        self.Soyad = Soyad
        self.Sacrengi = Sacrengi        
        self.Boy = Boy        
        self.Kilo = Kilo

class Ogrenci(Insan):
    def __init__(self, Ad, Soyad, Sacrengi, Boy, Kilo,Bolum,Yas):
        super().__init__(Ad, Soyad, Sacrengi, Boy, Kilo) #Miraslama
        self.Bolum = Bolum
        self.Yas = Yas

Insan1 = Insan("Mert","Gençay","Siyah",175,85)
Ogrenci1 = Ogrenci("Ali","Can","Kumral",180,90,"Fen",19)

print(Insan1.Kilo)
print(Ogrenci1.Bolum)