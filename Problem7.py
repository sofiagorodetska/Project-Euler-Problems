def is_prime(n):
    # Bir sayının asal olup olmadığını kontrol eden bir fonksiyon.
    # Bu fonksiyon, 2'den n'in kareköküne kadar olan sayıları kontrol eder.
    # Eğer sayı bir böleni varsa, asal değildir.
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    # Belirli bir sıradaki asal sayıyı bulan bir fonksiyon.
    # Başlangıçta, asal sayı sayacını ve bulunan asal sayıyı sıfıra eşitleriz.
    prime_count = 0
    prime = 0
    # 2'den başlayarak sonsuz bir döngü başlatırız.
    number = 2
    while True:
        # Eğer sayı asalsa, asal sayacı artırırız.
        if is_prime(number):
            prime_count += 1
            # Eğer asal sayacı hedef sıraya ulaştıysa, bu sayıyı bulunan asal sayı olarak atarız.
            if prime_count == n:
                prime = number
                break
        # Sayıyı bir artırırız.
        number += 1
    # Bulunan asal sayıyı döndürürüz.
    return prime

# 10001. asal sayıyı buluruz.
result = nth_prime(10001)

print(result)
