buku = ['Matematika', 'Fisika', 'Kimia', 'Biologi']
print('Data awal:', buku)

buku.append('Sejarah')
print('Data masuk Sejarah:', buku)

buku.append('Geografi')
print("Data masuk Geografi:", buku)

dataKeluar = buku.pop()
print('Data yang keluar adalah:', dataKeluar)
print("Data terakhir adalah:", buku)