import lingkaran
import persegi
from lingkaran import luas_lingkaran

while True:
    print("=== Perhitungan Lingkaran ===")
    r = float(input("Masukkan jari-jari lingkaran: "))

    print("\n=== Perhitungan Persegi ===")
    s = float(input("Masukkan panjang sisi persegi: "))

    luas_lingkaran = lingkaran.luas_lingkaran(r)
    keliling_lingkaran = lingkaran.keliling_lingkaran(r)

    luas_persegi = persegi.luas_persegi(s)
    keliling_persegi = persegi.keliling_persegi(s)

    print("\n=== Hasil Perhitungan ===")
    print(f"Luas Lingkaran: {luas_lingkaran:.2f}")
    print(f"Keliling Lingkaran: {keliling_lingkaran:.2f}")
    print(f"Luas Persegi: {luas_persegi:.2f}")
    print(f"Keliling Persegi: {keliling_persegi:.2f}")

    repeat = input("\nApakah ingin menggunakan kalkulator lagi? (y/n): ").lower()
    if repeat == 'n':
        print("Terima kasih telah menggunakan program!")
        break
    elif repeat == 'y':
        continue
    else:
        print("Input tidak valid, program dihentikan.")
        break
