def factorial(n):
    # İlk olarak, 0 ve 1'in faktöriyelini 1 olarak tanımlarız.
    if n == 0 or n == 1:
        return 1
    else:
        # Faktöriyeli hesaplamak için bir döngü kullanırız.
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def sum_of_digits(n):
    # Bir sayının basamaklarının toplamını hesaplamak için bu fonksiyonu kullanırız.
    # İlk olarak, sayıyı string olarak dönüştürürüz.
    num_str = str(n)
    total = 0
    for digit in num_str:
        # String olarak dönüştürülen sayının her bir basamağını alırız ve integer'a dönüştürerek toplama ekleriz.
        total += int(digit)
    return total

# 100! (100 faktöriyel) hesaplanır.
factorial_100 = factorial(100)

# 100! 'in basamakları toplanır.
result = sum_of_digits(factorial_100)

print(result)
