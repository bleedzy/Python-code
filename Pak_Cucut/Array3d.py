biodata_kelompok = [
    {
    "Nama": "Adi",
    "Usia": 20,
    "Hobi": "Coding",
    "Tinggi": 144,
    "Berat": 20,
    "Alamat": "Jl. Merdeka No. 1"
    },
    {
    "Nama": "Algojali",
    "Usia": 21,
    "Hobi": "Mancing",
    "Tinggi": 245,
    "Berat": 110,
    "Alamat": "Jl. Merdeka No. 2"
    },
    {
    "Nama": "Kia",
    "Usia": 20,
    "Hobi": "Jajan",
    "Tinggi": 160,
    "Berat": 50,
    "Alamat": "Jl. Merdeka No. 3"
    }
    ]

print("\n--- Biodata Kelompok ---")
for i, biodata in enumerate(biodata_kelompok, start=1):
    print(f"\nAnggota {i}:")
    print(f"Nama   : {biodata['Nama']}")
    print(f"Usia   : {biodata['Usia']} tahun")
    print(f"Hobi   : {biodata['Hobi']}")
    print(f"Tinggi : {biodata['Tinggi']} cm")
    print(f"Berat  : {biodata['Berat']} kg")
    print(f"Alamat : {biodata['Alamat']}")



