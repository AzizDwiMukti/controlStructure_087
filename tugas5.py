# Mencetak pola angka hingga n
n = int(input("Masukkan nilai n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()

    #Program ini mencetak pola angka dengan bentuk segitiga. Setiap baris ke-i mencetak angka i sebanyak i kali