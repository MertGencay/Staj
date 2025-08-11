# Random Modülü

import random

x = random.random() # 0-1 arasında rastgele sayı üretir
print(x)

y = random.uniform(10,1000) # İstenilen aralıkta float sayı üretir
print(y)

z = random.randint(10,1000) # İstenilen aralıkta tam sayı üretir
print(z)

a = ["Ali","Mehmet","Ahmet","Yusuf"]
b = random.choice(a) # Rastgele bir ismi döndürür
print(b)

liste = range(0,100)
c = random.sample(liste,20) # İstenilen sayıda rastgele sayı (0,100) üretir
print(c)