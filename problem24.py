from itertools import permutations

# Dijital rakamları içeren bir dizi oluştur
digits = '0123456789'

# Tüm permütasyonları üret ve leksikografik sıraya göre sırala
perms = sorted([''.join(perm) for perm in permutations(digits)])

# Milyonuncu leksikografik permütasyonu bul
millionth_perm = perms[999999]

print(millionth_perm)
