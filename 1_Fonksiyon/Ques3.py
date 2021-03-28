"""
3.
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.
vize1 toplam notun %30'una etki edecek.
vize2 toplam notun %30'una etki edecek.
final toplam notun %40'ına etki edecek. (Bu değerler 0-100 arası kabul edilmeli.)
Toplam Not >=  90 -----> AA
Toplam Not >=  85 -----> BA
Toplam Not >=  80 -----> BB
Toplam Not >=  75 -----> CB
Toplam Not >=  70 -----> CC
Toplam Not >=  65 -----> DC
Toplam Not >=  60 -----> DD
Toplam Not >=  55 -----> FD
Toplam Not <  55 -----> FF

"""

vize1 = float(input('vize1 notunuz: '))
vize2 = float(input('vize2 notunuz: '))
final_notu = float(input('final notunuz: '))

GecmeNotu = (vize1 * 0.3) + (vize2 * 0.3) + (final_notu * 0.4)
print(GecmeNotu)

if GecmeNotu >= 90:
    print('AA')

elif GecmeNotu >= 85:
    print('AB')

elif GecmeNotu >= 80:
    print('BB')

elif GecmeNotu >= 75:
    print('CB')

elif GecmeNotu >= 70:
    print('CC')

elif GecmeNotu >= 65:
    print('DC')

elif GecmeNotu >= 60:
    print('DD')

elif GecmeNotu >= 55:
    print('FD')

elif GecmeNotu < 55:
    print('FF')
