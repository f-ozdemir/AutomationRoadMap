"""
Insan isimli bir sınıf tanımlayınız. Bütün constructor parametreleri default değerlere sahip olacak, 
default contructor (__init__) içinde belirlenecek. Bu değerler; ad,soyad,yas,ulke,sehir olacak.
Ek olarak yetenekler isimli bir boş dizi init fonksiyonu içinde tanımlanacak.
kisi_bilgileri isimli fonksiyon ile init fonksiyonu içinde belirlenen kisi bilgileri return’le dönülecek.
yetenek_ekle isimli fonksiyon ile init fonksiyonu içinde belirlenen yetenekler dizisine yetenekler eklenecek.
Bu classtan belirtilen bilgileri içeren bir nesne tanımlayın.
Tanımlanan nesneye yetenek ekleyin. (Bisiklete binmek, Python vs.)
kisi_bilgileri fonksiyonu ile bu bilgileri gösterin.
"""


class Insan:
    def __init__(self, ad, soyad, yas, ulke, sehir):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def yetenek_ekle(self, yetenek):
        self.yetenekler.append(yetenek)

    def kisi_bilgileri(self):
        print(f'{self.ad} {self.soyad} {self.yas} {self.ulke} {self.sehir} {self.yetenekler[0]} ')


kisi1 = Insan("Shima", "Baha", 22, "India", "Mumbai")
kisi1.yetenek_ekle("Coding\n ")
kisi1.kisi_bilgileri()
