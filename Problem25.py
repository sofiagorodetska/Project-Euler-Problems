def fibonacci_digits(n):
    # Fibonacci dizisindeki bir sayının basamak sayısını hesaplayan bir fonksiyon.
    # İlk olarak, ilk iki Fibonacci sayısını 1 olarak tanımlarız.
    fib_1 = 1
    fib_2 = 1
    index = 2  # İlk iki sayıyı saymaya başlamak için 2'ye ayarlarız.

    # İlk iki sayı hariç, Fibonacci dizisindeki her sayıyı hesaplarız.
    while True:
        # Fibonacci dizisindeki bir sonraki sayıyı hesaplarız.
        fib_next = fib_1 + fib_2
        # İndeksi bir artırırız.
        index += 1
        # Eğer son sayının basamak sayısı n'i geçerse, bu sayının indeksini döndürürüz.
        if len(str(fib_next)) >= n:
            return index
        # Fibonacci dizisindeki sayıları güncelleriz.
        fib_1, fib_2 = fib_2, fib_next

# 1000 basamaklı bir Fibonacci sayısının indeksini hesaplarız.
result = fibonacci_digits(1000)

print(result)
