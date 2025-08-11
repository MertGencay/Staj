# İnput Fonksiyonu
# Kullanıcıdan girdi alır.

x = input("İlk Sayıyı Giriniz: ")   
y = input("İkinci Sayıyı Giriniz: ")
z = int(x) + int(y)
print("Sonuç:"+" "+str(z))

çap = input("Lütfen dairenin çapını giriniz: ")
yarıçap = float(çap)/2
pi = 3.14159
alan = pi*(yarıçap*yarıçap)
print("Dairenin Alanı: "+" "+str(alan))