"""2.
sayiAtama ve sayiOkusu isimli 2 tane fonksiyon tanımlayın bu fonksiyonlardan sayiAtama fonksiyonu 2 basamaklı
bi sayıyı parametre olarak alabilecek ve fonksiyon içinde bu değer bir değişkene atanacak. Daha sonra sayiAtama
fonksiyonu içinde sayiOkunusu isimli fonksiyon çağırılarak değişkene atanan sayının okunuşu string olarak verilecek.
sayiAtama fonksiyonu 2 basamaktan az yada daha fazla sayıyı kabul etmeyecek.
"""

birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def sayiAtama(sayi):
    if (10 > sayi) or (sayi < 100):
        sayi1 = sayi
        return sayiOkusu(sayi1)
    else:
        pass


def sayiOkusu(sayi1):
    birinci = sayi1 % 10
    ikinci = sayi1 // 10

    return onlar[ikinci] + " " + birler[birinci]


print(sayiOkusu(99))
