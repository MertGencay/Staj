#Sözlük Veri Tipi

kimlik = {
    "İsim" : "Mert",
    "Soyisim" : "Gençay",
    "Yaş" : 21,
}

print(kimlik)
print(kimlik["İsim"])
print(kimlik["Soyisim"])
print(kimlik["Yaş"])

kimlik["İsim"] = "Ahmet" #Değiştirilebilir
print(kimlik)

kimlik["TC_no"] = 40506070901 #Eklenilebilir
print(kimlik)


kullanıcılar = {"Ahmetcan":{
    "TC_no":21435784591,
    "D_Yeri":"Ankara",
    "Yas":35                        
}, "Arzu":{
    "TC_no":21766884591,
    "D_Yeri":"İstanbul",
    "Yas":28
}                 
                }

print(kullanıcılar["Ahmetcan"])
print(kullanıcılar["Arzu"])