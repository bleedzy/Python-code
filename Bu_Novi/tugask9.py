from collections import deque
antrian = deque(["Andi", "Budi", "Citra", "Dewi"])
print("Antrian awal ", list(antrian))

antrian.append("Eko")
print("Setelah menambahkan Eko ", list(antrian))

keluar = antrian.popleft()
print("Keluar dari antrian ", keluar)
print("Antrian setelah popleft ", list(antrian))