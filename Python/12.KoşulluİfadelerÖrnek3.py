#If-Elif-Else Yapısı Örnek-3

isim = str(input("Lütfen Adınızı Giriniz:"))
yas = int(input("Lütfen Yaşınızı Giriniz:"))
egitim = str(input("Lütfen Eğitim Durumunuzu Giriniz:"))
egitim2 = ("İlkokul","Ortaokul","Lise","Üniversite")

if egitim not in egitim2:
    print("Lütfen Geçerli Bir Eğitim Durumu Giriniz!")
elif (yas >= 18) and (egitim == "Lise" or egitim == "Üniversite"):
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet alamazsınız.")
