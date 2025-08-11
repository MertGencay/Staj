#Nesne Yönelimli Programlama (OOP) - Soyutlama/Abstract Classes

from abc import ABC, abstractmethod

class Hayvan(ABC):
    @abstractmethod
    def yurumek(self): pass

    @abstractmethod
    def kosmak(self): pass

class Köpek(Hayvan):
    def __init__(self):
        print("Köpek")
    
    def yurumek(self):
        print("yürümek")
    def kosmak(self):
        print("koşmak")

k1 = Köpek()