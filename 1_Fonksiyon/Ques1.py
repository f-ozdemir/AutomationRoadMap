"""
1.
3 tane parametre alan bolunenSayiBulma isimli bir fonksiyon tanımlayın.
Bu fonsiyon;min_sayi,max_sayibolunecek_sayi isimli parametreleri alacak.
Fonksiyon dışardan aldığı bu parametre değerlerini kullanarak,
min_sayi ve max_sayi aralığındaki bolunecek_sayi değerine bölünen sayıları bir diziye atayıp,
listeleyecek ve toplam_sayi ile bu aralık arasındaki değerlerin sayısını return ile döndürücek.

"""


def bolunenSayiBulma(min_sayi, max_sayi, bolunecek_sayi):
    bolunen_sayilar = []
    toplam_sayi = 0
    for i in range(min_sayi, max_sayi + 1):
        if i % bolunecek_sayi == 0:
            bolunen_sayilar.append(i)
            toplam_sayi = sum(bolunen_sayilar)
    print('bölünen Sayilar:', bolunen_sayilar)
    print("bölünen Sayilar Toplamı:", toplam_sayi)


bolunenSayiBulma(2, 20, 2)
