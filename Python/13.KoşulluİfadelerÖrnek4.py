#If-Elif-Else Yapısı Örnek-4 Basit Bir Hesap Makinesi

print("""Hesap Makinesi
[1] Toplama
[2] Çıkarma   
[3] Çarpma   
[4] Bölme   
[5] Üs Alma   
[Q] Çıkış         
""")

islem = input("Lütfen yapmak istediğiniz işlemi seçiniz:")

if islem == "1":
    sayı1 = float(input("Lütfen ilk sayıyı giriniz:"))
    sayı2 = float(input("Lütfen ikinci sayıyı giriniz:"))
    print("Toplama işleminizin sonucu {}".format(sayı1+sayı2))
elif islem == "2":
    sayı1 = float(input("Lütfen ilk sayıyı giriniz:"))
    sayı2 = float(input("Lütfen ikinci sayıyı giriniz:"))
    print("Çıkarma işleminizin sonucu {}".format(sayı1-sayı2))
elif islem == "3":
    sayı1 = float(input("Lütfen ilk sayıyı giriniz:"))
    sayı2 = float(input("Lütfen ikinci sayıyı giriniz:"))
    print("Çarpma işleminizin sonucu {}".format(sayı1*sayı2))
elif islem == "4":
    sayı1 = float(input("Lütfen ilk sayıyı giriniz:"))
    sayı2 = float(input("Lütfen ikinci sayıyı giriniz:"))
    print("Bölme işleminizin sonucu {}".format(sayı1/sayı2))
elif islem == "5":
    sayı1 = float(input("Lütfen ilk sayıyı giriniz:"))
    sayı2 = float(input("Lütfen kuvvet derecesini giriniz:"))
    print("Üs alma işleminizin sonucu {}".format(sayı1**sayı2))
elif islem == "Q" or islem == "q":
    print("Hoşçakalın...")