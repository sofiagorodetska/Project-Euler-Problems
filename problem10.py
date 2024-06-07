def is_prime(n):
    # Bir sayının asal olup olmadığını kontrol eden bir fonksiyon.
    # 2'den başlayarak sayının kareköküne kadar olan sayıları kontrol ederiz.
    # Eğer sayı bir böleni varsa, asal değildir.
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes_below_n(n):
    # Belirli bir sınırın altındaki tüm asal sayıların toplamını hesaplayan bir fonksiyon.
    total = 0
    for number in range(2, n):
        if is_prime(number):
            total += number
    return total

# 2 milyonun altındaki tüm asal sayıların toplamını hesaplarız.
limit = 2000000
result = sum_of_primes_below_n(limit)

print(result)
