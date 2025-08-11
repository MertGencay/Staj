# Datetime Kütüphanesi

from datetime import*

# Zamanı Tarihi döndürür
x = datetime.now() 
print(x)
x = datetime.today() 
print(x)
print(x.strftime("%d-%m-%Y")) # Gün-Ay-Yıl
print(x.day)
print(x.month)
print(x.year)
print(x.hour)
print(x.minute)
print(x.second)

y = date(2025,6,30)
print(y)

z = datetime(2025,6,25,16,4,30)
print(z)

a = time(12,15,36)
print(a)

b = datetime.now()
c = datetime.ctime(b)
print(b)
print(c)

dogumgünü = datetime(1976,9,16)
bugün = datetime.today()
fark = bugün - dogumgünü
print(fark)
print(fark.days)

bugün = datetime.today()
fark = timedelta(days=3251)
gelecek = bugün + fark
gecmis = bugün - fark
print(gelecek)
print(gecmis)

import time 

# while True:
#     zaman = time.strftime("%H:%M:%S")
#     print(zaman)
#     time.sleep(3)