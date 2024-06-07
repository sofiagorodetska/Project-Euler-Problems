def prime_factors(n):
    # Bir sayının asal çarpanlarını bulan bir fonksiyon.
    factors = []
    # 2, 3 ve sonraki tek sayılar için bölenleri kontrol ederiz.
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 3 == 0:
        factors.append(3)
        n //= 3
    # Geriye kalan bölenleri kontrol ederiz.
    # İlk asal sayıdan (5) başlayarak bir sonraki sayıya (6) 2 ekleriz.
    # Bu, sayıların sadece tek sayılar olması ve 6'nın 2 ve 3'e tam bölünmemesi anlamına gelir.
    # Bu sayede 6'nın katları olan sayıları (12, 18, 24, vb.) zaten 2 ve 3'e bölündüğü için kontrol etmemiz gerekmez.
    i = 5
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        while n % (i + 2) == 0:
            factors.append(i + 2)
            n //= (i + 2)
        i += 6
    # Eğer n, kendisinden küçük bir asal sayıya bölünmezse, n kendisi asal olur.
    if n > 2:
        factors.append(n)
    return factors

def distinct_prime_factors_count(n):
    # Bir sayının farklı asal çarpanlarının sayısını döndüren bir fonksiyon.
    # Her bir çarpanın bir kere sayılmasını sağlamak için bir küme kullanırız.
    return len(set(prime_factors(n)))

def find_consecutive_numbers_with_distinct_prime_factors(num_count, distinct_count):
    # Ardışık num_count sayıyı kontrol eder ve her biri distinct_count farklı asal çarpana sahip olanları bulur.
    count = 0
    number = 2 * 3 * 5 * 7  # İlk num_count sayının çarpanlarının çarpımıyla başlarız.
    while True:
        if distinct_prime_factors_count(number) == distinct_count:
            count += 1
            if count == num_count:
                return number - num_count + 1
        else:
            count = 0
        number += 1

# Ardışık 4 sayı buluruz, her birinin farklı asal çarpanları olacak.
result = find_consecutive_numbers_with_distinct_prime_factors(4, 4)

print(result)
