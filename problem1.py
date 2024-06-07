def sum_of_multiples_of_3_and_5(limit):
    # Belirli bir sınıra kadar olan 3 ve 5'in katlarının toplamını hesaplayan bir fonksiyon.
    total = 0
    # 1'den başlayarak limit - 1'e kadar olan tüm sayıları kontrol ederiz.
    for i in range(limit):
        # Eğer sayı 3 veya 5'e tam bölünebiliyorsa, total değişkenine ekleriz.
        if i % 3 == 0 or i % 5 == 0:
            total += i
    # Toplamı döndürürüz.
    return total

# 1000'e kadar olan 3 ve 5'in katlarının toplamını hesaplarız.
result = sum_of_multiples_of_3_and_5(1000)

print(result)
