l = 41
# Variabel jumlah dan harga buah
a = ['30','5000']
j = ['20','4000']
m = ['15','7500']

#1. Total buah
tbuah = int(a[0]) + int(j[0]) + int(m[0])
print('Total buah'.ljust(l),':' , tbuah)

#2. Total harga buah
tharga = (int(a[0]) * int(a[1])) + (int(j[0]) * int(j[1])) + (int(m[0]) * int(m[1]))
print('Total harga buah'.ljust(l),':' , f'Rp. {tharga:,.2f}')

#3. Rata-rata harga per buah
print('Rata-rata harga per buah'.ljust(l),':' , f'Rp. {tharga//tbuah:,.2f}')

#4. Pendapatan bersih setelah diskon 10%
diskon = 0.10
ub = tharga * (1 - diskon)
print('Pendapatan bersih setelah diskon 10%'.ljust(l),':' , f'Rp. {ub:,.2f}')

#5. Uang yang diterima masing-masing karyawan dan sisa uang setelah dibagi rata
jk = 4
upk = ub // jk  
sisa = ub % jk
print('Jumlah karyawan'.ljust(l),':' , jk)
print('Uang yang diterima masing-masing karyawan'.ljust(l),':' , f'Rp. {upk:,.2f}')
print('Sisa uang setelah dibagi rata'.ljust(l),':' , f'Rp. {sisa:,.2f}')



