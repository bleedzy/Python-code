def penjumlahan(a, b):
    return a + b

def perkalian(a, b):
    return a * b

def keliling_persegi_panjang(p, l):
    return 2 * (p + l)

def luas_persegi_panjang(p, l):
    return p * l

while True:
    print("\n=== Program Kalkulator ===")
    print("1. Penjumlahan")
    print("2. Perkalian")
    print("3. Keliling Persegi Panjang")
    print("4. Luas Persegi Panjang")

    choice = input("Pilih operasi (1/2/3/4): ")

    if choice == '1':
        print("\n--- Penjumlahan ---")
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print(f"Hasil penjumlahan: {penjumlahan(a, b)}")
    elif choice == '2':
        print("\n--- Perkalian ---")
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print(f"Hasil perkalian: {perkalian(a, b)}")
    elif choice == '3':
        print("\n--- Keliling Persegi Panjang ---")
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        print(f"Keliling persegi panjang: {keliling_persegi_panjang(p, l)}")
    elif choice == '4':
        print("\n--- Luas Persegi Panjang ---")
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        print(f"Luas persegi panjang: {luas_persegi_panjang(p, l)}")
    else:
        print("Pilihan tidak valid!")

    repeat = input("\nApakah ingin menggunakan kalkulator lagi? (y/n): ").lower()
    if repeat == 'n':
        print("Terima kasih telah menggunakan program!")
        break
    elif repeat == 'y':
        continue
    else:
        print("Input tidak valid, program dihentikan.")
        break