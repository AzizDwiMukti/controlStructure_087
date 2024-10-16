# Mencari Angka Terbesar dari Tiga Angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
angka3 = float(input("Masukkan angka ketiga: "))

if angka1 >= angka2 and angka1 >= angka3:
    print(f"Angka terbesar adalah: {angka1}")
elif angka2 >= angka1 and angka2 >= angka3:
    print(f"Angka terbesar adalah: {angka2}")
else:
    print(f"Angka terbesar adalah: {angka3}")

    #Program ini mencari angka terbesar dari tiga angka yang diinput. Angka terbesar dibandingkan menggunakan struktur if-elif-else, kemudian dicetak.

