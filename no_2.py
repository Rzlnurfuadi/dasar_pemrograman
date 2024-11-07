#Nama : Muhammad Rizal Nurfuadi
#NIM : 2400625
#Kelas : Rpl 1B

nilai = [87.7, 56.5, 93.2, 67.8, 65.0, 38.5, 42.8, 74.5, 89.0, 93.2]

nourut = int(input("Masukkan nomor urut siswa: "))

if 1 <= nourut <= 10:
    print(f"Nilai siswa nomor urut {nourut} adalah: {nilai[nourut - 1]}")
else:
    print("Eror. Silakan masukkan nomor antara 1 hingga 10.")