#Demet (Tuple) Veri Tipi

demet = ("Mert")
print(demet)
print(type(demet)) #String

demet2 = ("Mert",21)
print(demet2)
print(type(demet2)) #Tuple

print(demet2[0])
print(demet2[1])

#demet2[0] = "Mehmet" Demetler(tuples) değiştirilemezler! => TypeError: 'tuple' object does not support item assignment bu hatayı alırız.
#print(demet2)


# Küme(set) Veri Tipi
küme = {"Mert",25,"Mert"}
print(type(küme))
print(küme)  #Ahmeti iki kez yazmaz.