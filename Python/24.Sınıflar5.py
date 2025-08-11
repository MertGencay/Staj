#Nesne Yönelimli Programlama (OOP) - Çok Biçimlilik/Polymorphism

class Employee:
    def maas(self):
        zam = 0.1
        return 100 + 100 * zam
    
class CompEng(Employee):
    def maas(self):
        zam = 0.2
        return 100 + 100 * zam
    
class EEE(Employee):
    def maas(self):
        zam = 0.3
        return 100 + 100 * zam
    
e1 = Employee()
c1 = CompEng()
eee = EEE()

print(e1.maas())
print(c1.maas())
print(eee.maas())
