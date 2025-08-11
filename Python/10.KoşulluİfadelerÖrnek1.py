#If-Elif-Else Yapısı Örnek-1

Kullanici_Adi = input("Lütfen Kullanıcı Adını Giriniz:")
Kullanici_Sifre = input("Lütfen Şifrenizi Giriniz:")

SistemKA = "Mert Gençay"
SistemSif = "1905"

if Kullanici_Adi == SistemKA and Kullanici_Sifre == SistemSif:
    print("Merhaba {},Hoşgeldiniz...".format(SistemKA))
elif Kullanici_Adi != SistemKA and Kullanici_Sifre != SistemSif:
    print("Merhaba,Kullanıcı Adı ve Şifre Hatalı!")
elif Kullanici_Adi != SistemKA:
    print("Merhaba,Kullanıcı Adını Hatalı Girdiniz!")
else:
    print("Merhaba {}, Hatalı Bir Şifre Girdiniz!".format(SistemKA))
