#Nama : Muhammad Rizal Nurfuadi
#Kelas : 1B RPL
#NIM : 2400625

def rata_rata(*angka):
    total = sum(angka)
    ratarata = total / len(angka)
    return total, ratarata

angka = []
while True:
    input_angka = int(input(f"Masukkan angka: "))
    if input_angka == 0:
        break
    angka.append(input_angka)

total, ratarata = rata_rata(*angka)
print(f"Total: {total}")
print(f"Rata-rata: {ratarata}")