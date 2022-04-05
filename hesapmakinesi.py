def topla():
    sayi1=int(input("1.Sayıyı Giriniz:"))
    sayi2 = int(input("2.Sayıyı Giriniz:"))
    print(sayi1+sayi2)
def cikar():
    sayi1 = int(input("1.Sayıyı Giriniz:"))
    sayi2 = int(input("2.Sayıyı Giriniz:"))
    a=sayi1-sayi2
    if sayi1>sayi2:
        print(a)
    else:
        print("Sonuç Negatifdir:",a)

def bolme():
    sayi1 = int(input("1.Sayıyı Giriniz:"))
    sayi2 = int(input("2.Sayıyı Giriniz:"))
    if sayi1==0 and sayi2==0:
        print("Tanımsızdır")
    else:
        a = sayi1 / sayi2
        print (a)

def carpma():
    sayi1 = int(input("1.Sayıyı Giriniz:"))
    sayi2 = int(input("2.Sayıyı Giriniz:"))
    a=sayi1*sayi2
    if not sayi1==0 and sayi2==0:
        print("Çarpma İşlemi Sonucu:",a)
    else:
        print("sonuç:",a)

def modal():
    sayi1 = int(input("1.Sayıyı Giriniz:"))
    sayi2 = int(input("2.Sayıyı Giriniz:"))
    a=sayi1%sayi2
    print(float(a))




x=input("Adınızı girer misiniz?:")
if  x=="":
    print("Geçerli Bir İsim Giriniz!!")
else:
    print("Hesap Makinesi Uygulmasına Hoşgeldiniz Sayın :", x)
    print(
        "Hangi işlem yapılsın istiyorsanız numarasını giriniz:"
        " 1-Toplama "
        " 2-Çıkarma"
        " 3-Bölme"
        " 4-Çarpma"
        " 5-Mod Alma"
    )
    secim = int(input("Yapmak İstenen İşlem ?:"))

    if secim == 1:
        topla()
    if secim == 2:
        cikar()
    if secim == 3:
        bolme()
    if secim == 4:
        carpma()
    if secim == 5:
        modal()









