def yazitura():
    import random
    sayi=random.random()

    if sayi>0.5:
        return "Tura"
    else:
        return "Yazı"
    

sonuc=yazitura()
print(sonuc)