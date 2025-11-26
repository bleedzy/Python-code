print('Daftar mahasiswa')

students = [
    {"No": 1, "Nama": "Ani",    "Nilai": 80},
    {"No": 2, "Nama": "Budi",   "Nilai": 95},
    {"No": 3, "Nama": "Candra", "Nilai": 85},
    {"No": 4, "Nama": "Dodi",   "Nilai": 70},
]

print("No\tNama\tNilai")
for s in students:
    print(f"{s['No']}\t{s['Nama']}\t{s['Nilai']}")

print("\n--- Deskripsi ---")
for s in students:
    print(f"no {s['No']}, nama {s['Nama'].lower()}, nilai {s['Nilai']}")