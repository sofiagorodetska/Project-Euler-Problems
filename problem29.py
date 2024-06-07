def distinct_powers(a_min, a_max, b_min, b_max):
    # farklı terimleri saklamak için bir küme oluştur
    distinct_terms = set()
    
    # a_min'den a_max'a ve b_min'den b_max'a kadar tüm a ve b değerlerini döngüyle gez
    for a in range(a_min, a_max + 1):
        for b in range(b_min, b_max + 1):
            # a^b'nin sonucunu hesapla ve kümeye ekle
            distinct_terms.add(a ** b)
    
    # farklı terimlerin sayısını döndür
    return len(distinct_terms)

# 2^2'den 100^100'e kadar olan tüm farklı terimlerin sayısını hesapla
result = distinct_powers(2, 100, 2, 100)
print(result)
