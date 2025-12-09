def cari_kode_buku():
    daftar = [101, 205, 330, 412, 578, 689, 710]
    try:
        kode = int(input("Masukkan kode buku yang dicari: "))
    except ValueError:
        print("Input tidak valid.")
        return

    ditemukan = False
    for k in daftar:
        if k == kode:
            print(f"Kode buku {kode} berhasil ditemukan")
            ditemukan = True
            break

    if not ditemukan:
        print(f"Kode buku {kode} tidak tersedia dalam daftar")

if __name__ == "__main__":
    cari_kode_buku()