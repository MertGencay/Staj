#Veri Tiplerinde Dönüşüm

a = 2
b = 2.2
c = "21"

print(type(a))
print(type(b))
print(type(c))

d = str(a) #String'e döner.
print(d+c)

e = float(a) #Float'a döner.
print(a+e)

f = int(b) #Integer'a döner.
print(f+a)

x = [1,3,5,7,9]
print(type(x))

y = tuple(x) #Tuple'a döner.
print(y)
print(type(y))

z = set(x) #Set'e döner.
print(z)
print(type(z))