#Aritmetik Operatörleri
print(5+3) #Toplama
print(5-3) #Çıkarma
print(5*3) #Çarpma
print(5/3) #Bölme
print(5//3) #Tam Bölme (integer)
print(5**3) #Üs alma
print(5%3) #Bölümünden kalan

#Atama Operatörleri
x,y = 10,20
x += 5
x -= 5
x *= 5
x /= 5
x //= 5
x **= 5
x %= 5

#Karşılaştırma Operatörleri
x,y = 12,9
print(x<y)
print(x>y)
print(x==y) #Eşit mi
print(x!=y) #Eşit değil mi
print(x<=y)
print(x>=y)

x=[1,3,5]
print(3 in x) #Listenin içinde var mı yok mu kontrolü yapar

y=[2]
z=[2]
print(id(y),id(z))
print(y is z) #İdlerin eşit olup olmamasını kontrol eder
print(y is not z)

#Mantıksal Operatörleri
x,y = 2,5
print(x<10 or y<10) #Veya
print(x<10 and y<10) #Ve
print(not(x<5)) #Değili