""" 
50 soruluk, 4 yanlışın 1 doğruyu götürdüğü sınavda öğrencinin inputlarla girilen doğru yanlış sayısına göre aldığı
puanı hesaplayan programı yazınız. Ogrenci sınıfı diye bir sınıf tanımlanacak.
Bu sınıfın içinde ogrenciAdı, ogrenciSoyadı, ogrenciSınıf’ı değişkenleri bulunacak.
Bu sınıftan nesne oluşturulurken bu bilgiler parametre olarak verilecek.
Soru diye bir sınıfınız olacak. Bu sınıfın NetSayısı(...) ve Hesapla(...) diye iki fonksiyon olacak.
NetSayısı fonksiyonu doğru ve yanlış sayısını parametre olarak alıp öğrencinin kaç neti olduğunu bulur.
Hesapla fonksiyonu net sayısını parametre olarak alıp öğrencinin puanını hesaplayacak.
Her net 2 puan.
En sonunda öğrenci bilgileri ve puanı console gösterilecek.
"""


class Ogrenci:

    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinifi):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinifi = ogrenciSinifi

    def ogrenci_bilgileri(self):
        print(f'{self.ogrenciAdi} {self.ogrenciSoyadi} {self.ogrenciSinifi}')


class Soru:
    toplamSoru = 50

    def NetSayisi(self, dogruSayisi, yanlisSayisi):
        toplamNet = dogruSayisi - (yanlisSayisi / 4)
        return toplamNet

    def Hesapla(self, toplamNet):
        toplamPuan = toplamNet * 2
        return toplamPuan


ogrenci_1 = Ogrenci('Corey', 'Schafer', 5)
ogrenci_1.ogrenci_bilgileri()

sinav_bilgileri = Soru()
print("toplam net sayisi: ", sinav_bilgileri.NetSayisi(40, 10))
print("toplam puan : ", sinav_bilgileri.Hesapla(sinav_bilgileri.NetSayisi(40, 10)))
