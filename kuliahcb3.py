# Data jumlah dan harga per buah
jumlah_apel = 30
harga_apel = 5000

jumlah_jeruk = 20
harga_jeruk = 4000

jumlah_mangga = 15
harga_mangga = 7500

# 1. Total buah
total_buah = jumlah_apel + jumlah_jeruk + jumlah_mangga
print("Total buah:", total_buah)

# 2. Total harga buah
total_harga = (jumlah_apel * harga_apel) + (jumlah_jeruk * harga_jeruk) + (jumlah_mangga * harga_mangga)
print("Total harga buah:", total_harga)

# 3. Rata-rata harga per buah
rata_rata_harga = total_harga / total_buah
print("Rata-rata harga per buah:", rata_rata_harga)

# 4. Pendapatan bersih setelah diskon 10%
diskon = 0.10
pendapatan_bersih = total_harga * (1 - diskon)
print("Pendapatan bersih setelah diskon 10%:", pendapatan_bersih)

# 5. Uang yang diterima masing-masing karyawan dan sisa uang setelah dibagi rata
jumlah_karyawan = 4
uang_per_karyawan = pendapatan_bersih // jumlah_karyawan
sisa_uang = pendapatan_bersih % jumlah_karyawan
print("Uang yang diterima masing-masing karyawan:", uang_per_karyawan)
print("Sisa uang setelah dibagi rata:", sisa_uang)