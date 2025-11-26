print('Program Mencari Angka Terbesar')
print('--------------------------')
n = int(input('Masukkan jumlah angka : '))

if n <= 0:
    print('Tidak ada angka untuk diproses.')
else:
    print('Masukkan', n, 'angka : ')

    x = []
    for i in range(n):
        print('Angka ke -', i + 1, ': ', sep='', end='')
        x.append(int(input()))
    print()

    max_num = x[0]
    for i in range(1, n):
        if x[i] > max_num:
            max_num = x[i]

    print('Pilih metode penjumlahan:')
    print('1. Menggunakan perulangan')
    print('2. Menggunakan fungsi sum()')
    metode = input('Masukkan pilihan (1/2): ').strip()

    if metode == '1':
        total = 0
        for val in x:
            total += val
        metode_used = 'Perulangan'
    elif metode == '2':
        total = sum(x)
        metode_used = 'Fungsi sum()'

    print('Angka terbesar adalah :', max_num)
    print(f'Total / Jumlah seluruh angka ({metode_used}):', total)