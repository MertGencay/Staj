#Nesne Yönelimli Programlama (OOP) - Kapsülleme (Encapsulation)

class Memur():
    def __init__(self,Ad,Soyad,Maas):
        self.Ad = Ad
        self.Soyad = Soyad
        self.__Maas = Maas
        self.__Zam = 0.2
    
    def zamoranı(self):
        self.__Maas = self.__Maas + self.__Maas*self.__Zam

    def getMaas(self):
        return self.__Maas

    def getZam(self):
        return self.__Zam

    def setZam(self,Yenioran):
        self.__Zam = Yenioran

memur1 = Memur("Mert","Gençay",6000)

print(memur1.Ad)
print(memur1.Soyad)
print(memur1.getMaas())
print(memur1.getZam())

memur1.setZam(0.5)
memur1.zamoranı()
print(memur1.getMaas())