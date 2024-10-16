# Mencetak angka ganjil hingga n
n = int(input("Masukkan nilai n: "))

print("Angka ganjil hingga", n, ":")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")

        #Program ini mencetak semua angka ganjil dari 1 hingga n. Angka-angka dicek dengan kondisi modulus (i % 2 != 0) untuk menentukan apakah ganjil.