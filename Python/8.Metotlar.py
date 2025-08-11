#Metotlar

#Sayısal Metotlar
x = 1905
print(abs(x)) # abs: Mutlak değerini döndürür.
print(pow(x,2)) # pow: Üssünü alır.
print(x.__divmod__(2))  #Kalanı ve bölümü verir.
print(x.as_integer_ratio())  #Hangi iki sayının bölümü sonucu oluşacağını bulur.
print(x.is_integer())  #Tam sayı kontrolu yapar True False döndürür.

# Karakter Dizileri Metotları
y = "Galatasaray"
print(y.lower()) #Bütün harfleri küçültür.
print(y.upper()) #Bütün harfleri büyütür.
print(y.isnumeric()) #Sayı mı kontrolü yapar.
print(y.isalnum()) #Sadece sayı ve harflerden oluşursa True döner.
print(y.capitalize()) #Sadece ilk harfi büyük yapar.
print(y.title()) #Bütün kelimelerin baş harflerini büyük yapar.
print(y.swapcase()) #Büyük harfleri küçük, küçük harfleri büyük yapar.
print(y.count("a")) #Aldığı parametreye göre metnin içinde arama yapar ve kaç adet olduğunu döndürür.
print(y.strip(" ")) #Boşlukları kaldırır.
print(y.lstrip(" ")) #Soldan boşlukları kaldırır.
print(y.rstrip(" ")) #Sağdan boşlukları kaldırır.
print(y.split()) #Parçalama yapar.

z = y.split(" ")
print(" ".join(z)) #Parçalananları birleştirir.
print(y.find("Galatasaray")) #Arama yapar ve bulunca index döndürür, bulamazsa -1 döndürür.
print(y.replace("Galatasaray","Cimbom")) #Kelimeyi değiştirir.

#Format Metodu
ad = "Mert"
soyad = "Gençay"
yas = "21"
Bilgiler = [ad,soyad,yas]
print("Kişinin Adı: {} ,Kişinin Soyadı: {} ,Kişinin Yaşı: {}".format(Bilgiler[0],Bilgiler[1],Bilgiler[2]))

#Liste Metotları
liste = [1,2,5,"Cimbom",2.5]
liste.append("Galatasaray") #Listenin sonuna ekleme yapar.
print(liste)
liste.insert(3,"Mert") #İndexe göre listeye ekleme yapar.
liste.remove(2) #Parametreye göre soldan başlayarak ilk gördüğü değeri siler.
liste.pop() #Sondan silme yapar index girilmezse.
liste2 = liste.copy() #Listeyi kopyalar.
print(liste2) 

liste3 = [1,3,5,7]
liste4 = ["a","b","c","d"]
liste3.extend(liste4) #İki listeyi birleştirir liste3 += liste4 de yapılabilir.
print(liste3)
print(liste3.count(3)) #Liste içinde arama yapar verilen parametreden kaç adet olduğunu bulur.
#print(liste3.sort()) #Küçükten büyüğe sıralama yapar.
#print(liste3.sort(reverse=True)) #Büyükten küçüğe sıralama yapar.
print(liste3.reverse()) #Listeyi tersine çevirir.
liste3.clear() #Listeyi siler boş liste döndürür.
print(liste3)

#Demet Metotları
x = (1,1,"Cimbom",2.5)
print(x.index(2.5)) #Verilen parametrenin bulunduğu indexi döndürür.
print(x.count(1)) #Verilen parametreden kaç adet olduğunu döndürür.

#Sözlük Metotları
bilgi = {
    "Ad":"Mert",
    "Soyad":"Gençay",
    "DYer":"Ankara"
}

print(bilgi.keys())  #Anahtar değerlerini döndürür.
print(bilgi.values()) #Değerleri döndürür.
print(bilgi.items()) #Hem anahtarları hem de değerleri döndürür.
print(bilgi.get("Ad")) #Verilen parametreye göre değeri döndürür.
bilgi.update({"Cinsiyet":"Erkek"}) #Sözlüğe ekleme yapar.
print(bilgi) 
bilgi2 = bilgi.copy() #Sözlüğü kopyalar.
print(bilgi2)
print(bilgi.__len__()) #Sözlüğün uzunluğunu hesaplar.
bilgi.pop("DYer") #Verilen Parametreyi siler.
print(bilgi)
bilgi.clear() #Sözlüğü temizler boş sözlük döndürür.
print(bilgi)

#Küme Metotları
küme = {1,"Anlaşılır Ekonomi",2.5,}
küme.add("Merhaba")
print(küme)
küme.discard("Merhaba") #Eleman yoksa hata döndürmez.
print(küme)
#küme.remove("Merhaba") #Eleman yoksa keyerror hatası verir.
print(küme)