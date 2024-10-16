# Deret Fibonacci hingga n
n = int(input("Masukkan nilai n: "))

a, b = 0, 1
print("Deret Fibonacci:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

    #Program ini mencetak deret Fibonacci hingga n angka. Dimulai dari 0 dan 1, lalu setiap angka berikutnya adalah jumlah dari dua angka sebelumnya.