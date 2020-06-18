import random

print("Merhaba, ben SayıBulucu. Aklından 1 ve 100 arası bir sayı tut ve ben onu bulacağım.")
sayiTuttumu = input("Aklından sayı tuttun mu? E/H ") #sadece E veya H harfi girilmeli
if (sayiTuttumu == "H"):
    print("Keşke bir sayı tutsaydın. Eğlenirdik :(")
    exit(0)
enBuyukSayi = 100
enKucukSayi = 1
tahmin = random.randint(enKucukSayi, enBuyukSayi)
while True:
    sayiDBK = input("Aklından tutuğun sayı {} mı değilse ipucu ver : D(Doğru)/B(Büyük)/K(Küçük) ".format(tahmin)) #sayı doğrusa D, büyük ise B, küçük ise K girlmeli
    if (sayiDBK == "D"):
        print("Bildim bak  :P")
        print("Demekki bu sayıyı {} tutmuşsun.".format(tahmin))
        break
    if (sayiDBK == "B"):
        enBuyukSayi = tahmin
        tahmin = random.randint(enKucukSayi, tahmin)

    if (sayiDBK == "K"):
        enKucukSayi = tahmin
        tahmin = random.randint(enKucukSayi, enBuyukSayi)
