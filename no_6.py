#Nama : Muhammad Rizal Nurfuadi
#NIM : 2400625
#Kelas : RPL 1B

bulanjuli = [
    "T-Shirt",
    "Blouse",
    "Kemeja",
    "Celana Panjang",
    "Rok",
    "Baju renang",
    "Tas",
    "Topi",
    "Sepatu",
    "sandal"
]

bulanini = bulanjuli.copy()

bulanini.remove("Topi")
bulanini.append("Dompet")
bulanini.append("Jepit rambut")
bulanini.append("Kerudung")

print("Daftar barang bulan Juli:")
for barang in bulanjuli:
    print(f"{barang}")
print(f"jumlah jenis barang :{len(bulanjuli)}")

print("daftar barang jualan bulan ini:")
for barang in bulanini:
    print(f"{barang}")
print(f"julah jenis barang: {len(bulanini)}")