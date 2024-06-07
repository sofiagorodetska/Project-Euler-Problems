def gcd(a, b):
    # En büyük ortak böleni (GCD) hesaplayan bir fonksiyon.
    # Bu fonksiyon, iki sayının en büyük ortak bölenini bulmak için Euclid'in Algoritması'nı kullanır.
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    # En küçük ortak katı (LCM) hesaplayan bir fonksiyon.
    # İki sayının LCM'i, bu sayıların çarpımının GCD'sine bölünmesiyle bulunur.
    return (a * b) // gcd(a, b)

def smallest_multiple(n):
    # Belirli bir sayının tüm bölenlerinin en küçük ortak katını hesaplayan bir fonksiyon.
    # Başlangıçta en küçük ortak katı 1 olarak tanımlarız.
    result = 1
    # 1'den n'ye kadar olan tüm sayıları kontrol ederiz.
    for i in range(2, n + 1):
        # Her adımda, en küçük ortak katı güncelleriz.
        result = lcm(result, i)
    # Sonunda, en küçük ortak katı döndürürüz.
    return result

# 1'den 20'ye kadar olan tüm sayıların en küçük ortak katını hesaplarız.
result = smallest_multiple(20)

print(result)
