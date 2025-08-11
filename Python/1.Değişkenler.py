#Number
a = 10 # int: pozitif tam sayı
b = -5 # int: negatif tam sayı
pi = 3.14 # float: ondalıklı sayı

z = 3 + 4j # complex: karmaşık sayı
print(z.real)  # 3.0
print(z.imag)  # 4.0

#String
x = "Galatasaray"
print(len(x)) #String'in uzunluğunu verir.
print(type(x)) #Değişkenin tipini verir.

#İndeksleme
print(x[0])
print(x[2])
print(x[-1])
print(x[-2])

#Parçalama
print(x[0:11:2]) # ilk parametre dahil : ikinci parametre dahil değil : üçüncü parametre kaçar kaçar gideceğini belirtir.
print(x[::-1]) # String'i tersine çevirir.

y = "Cimbom"

print(x + y) # İki string'i birleştirir (boşluksuz).
print(x + " " + y) # İki string'i birleştirir (boşluklu).
print(y * 3) # Bir string'i birden fazla kez yazmak için * kullanılır.
print(x + " " + "\n" + y) # Bir alt satıra geçmek için \n kullanılır.

#Boolean 
print(1905>1903) # True
print(1905<1903) # False

x = True
print(type(x))