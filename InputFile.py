from datetime import datetime

biodata_list = []
close = False

while True:
    x = datetime.now()

    name = input("Masukan nama: ")
    place = input("Masukan tempat lahir: ")
    idate = input("Masukan tanggal lahir (YYYY-MM-DD): ")
    hobby = input("Masukan hobi: ")

    y = datetime.strptime(idate, "%Y-%m-%d")

    age = x.year - y.year - ((x.month, x.day) < (y.month, y.day))

    biodata_list.append({
        "name": name,
        "place": place,
        "dob": y.strftime('%Y-%m-%d'),
        "age": age,
        "hobby": hobby
    })

    repeat = input("Masukan biodata lagi? (y/n): ").lower()

    if repeat == 'n' or repeat == 'N':
        break
    elif repeat == 'y' or repeat == 'Y':
        continue
    else:
        close = True
        break

if close == False:
    print("\n--- Biodata ---")
    for i, biodata in enumerate(biodata_list, start=1):
        print(f"\nData ke-{i}:")
        print(f"Nama: {biodata['name']}")
        print(f"Tempat tanggal lahir: {biodata['place']}, {biodata['dob']}")
        print(f"Umur: {biodata['age']} tahun")
        print(f"Hobi: {biodata['hobby']}")
else:
    print("Program dihentikan.")