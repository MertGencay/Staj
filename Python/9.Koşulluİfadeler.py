#If-Else Yapısı

x = 3
if x==5:
    print("Evet x 5'e eşittir.")
else:
    print("Hayır x 5'e eşit değildir.")

kullanici_adi = "Mert Gençay"
kullanici_sifre = "1905"
if kullanici_adi == "Mert Gençay" and kullanici_sifre == "1905":
    print("Giriş Başarılı")
else:
    print("Kullanıcı adı veya şifre hatalıdır!")

#If-Elif-Else Yapısı

ad = "Mert Gençay"
sifre = "1905"
if ad == "Mert Gençay" and sifre == "1905":
    print("Giriş Başarılı Hoşgeldiniz...")
elif ad != "Mert Gençay" and sifre != "1905":
    print("Kullanıcı Adı ve Şifre Hatalı!")
elif ad != "Mert Gençay":
    print("Kullanıcı Adı Hatalı!")
else: 
    print("Şifre Hatalı!")
