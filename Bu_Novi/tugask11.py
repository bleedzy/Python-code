def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

if __name__ == "__main__":
    harga = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]
    print("Daftar harga (terurut):", harga)

    try:
        target = int(input("Masukkan harga yang dicari: ").strip())
    except ValueError:
        print("Input tidak valid.")
        raise SystemExit(1)

    idx = binary_search(harga, target)
    if idx != -1:
        print(f"Harga {target} ditemukan pada indeks {idx}.")
    else:
        print(f"Harga {target} tidak tersedia dalam daftar.")