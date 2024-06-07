def special_pythagorean_triplet(target_sum):
    # İki döngü kullanarak olası a ve b değerlerini taramaya başlarız.
    for a in range(1, target_sum // 3):
        for b in range(a + 1, target_sum // 2):
            # c'nin değeri, a ve b'nin bulunduğu durumda target_sum - (a+b) olacaktır.
            c = target_sum - a - b
            # Eğer a^2 + b^2 = c^2 koşulunu sağlıyorsa, bu bir özel pisagor üçlüsüdür.
            if a**2 + b**2 == c**2:
                # Eğer özel pisagor üçlüsünü bulduysak, bu değerleri döndürürüz.
                return a, b, c
    # Eğer hiçbir özel pisagor üçlüsü bulamazsak, None döndürürüz.
    return None

# Hedef toplamı (target_sum) 1000 olarak belirleriz.
target_sum = 1000
# Özel pisagor üçlüsünün (a, b, c) değerlerini buluruz.
triplet = special_pythagorean_triplet(target_sum)

# Eğer bir özel pisagor üçlüsü bulunduysa, a * b * c'yi hesaplarız.
if triplet:
    product = triplet[0] * triplet[1] * triplet[2]
    print(product)

