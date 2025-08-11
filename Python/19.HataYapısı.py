# Hata Yapıları

def toplam(x,y): # iki noktayı koymazsak SyntaxError: expected ':'
    sonuc = x + y   # Girinti hatası yaparsak IndentationError: expected an indented block after function definition on line 4
    return sonuc

#print(x) # Tanımlanmamış bir değeri yazdırmaya çalışırsak NameError: name 'x' is not defined
#print(10/0) # ZeroDivisionError: division by zero

# Try-Except Yapısı

while True:
    try:
        x = int(input("Lütfen İlk Sayıyı Giriniz:"))
        y = int(input("Lütfen İkinci Sayıyı Giriniz:"))
        print(x/y)
    # except ZeroDivisionError:
    #     print("Sıfıra Bölmeye Çalışıyorsunuz!!!")
    # except ValueError:
    #     print("Sayı Dışında Bir Değer Girdiniz!!!")
    except Exception as hata:
        print("Yolunda Gitmeyen Birşeyler Var!!!",hata) # Hem kullanıcı bilgilendirilir hemde kodu yazan kişinin hatayı anlaması sağlanır
    else:
        #print("Sorun Yok")
        break
    # except (ZeroDivisionError,ValueError):
    #     print("Hatali Bir Değer Girdiniz!!!")
    # except:
    #     print("Hatali Bir Değer Girdiniz!!!")


# Raise Yapısı

# x = int(input("Lütfen sıfırdan farklı bir sayı giriniz:"))

# if x == 0:
#     raise Exception("Girdiğiniz değer sıfırdan farklı olmalıdır")
# else:
#     print(x)

def kontrol(y):
    if len(y)<5:
        raise Exception("Şifreniz en az 5 karakterden oluşmalıdır!!!")
    else:
        print("Şifreniz başarılı bir şekilde oluşturulmuştur.")

y = input("Lütfen Şifre Belirleyiniz:")

try:
    kontrol(y)
except Exception as hata:
    print(hata)