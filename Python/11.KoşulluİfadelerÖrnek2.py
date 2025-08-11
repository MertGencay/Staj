#If-Elif-Else Yapısı Örnek-2

print("Merhaba, Vücut Kitle Endeksi Hesaplama Uygulamasına Hoşgeldiniz!")

boy = int(input("Lütfen Boyunuzu Cm Cinsiden Giriniz:"))
kilo = int(input("Lütfen Kilonuzu Giriniz:"))
endeks = round(((kilo)/(boy/100)**2),2) #round verilen parametreye göre virgülden sonraki rakamları göstermez

if endeks <= 18.5:
    print("Vücut kitle endeksiniz {}'dir.Düşük kilolu grubundasınız!".format(endeks))
elif endeks <= 24.9:
    print("Vücut kitle endeksiniz {}'dir.Normal kilolu grubundasınız!".format(endeks))
elif endeks <= 29.9:
    print("Vücut kitle endeksiniz {}'dir.Fazla kilolu grubundasınız!".format(endeks))
elif endeks <= 40:
    print("Vücut kitle endeksiniz {}'dir.Obez grubundasınız!".format(endeks))
elif endeks > 40:
    print("Vücut kitle endeksiniz {}'dir.Aşırı obez grubundasınız!".format(endeks))