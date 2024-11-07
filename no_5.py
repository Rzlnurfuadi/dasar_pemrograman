#Nama : Muhammad Rizal Nurfuadi
#NIM : 2400625
#Kelas : RPL 1B

mobil={
    'Merek' : 'Honda',
    'Tipe' : 'HRV',
    'Tahun' : 2018,
    'Warna' : 'Hitam',
    'No. Polisi' : 'D 1234 ABC',
    'Bensin' : 'Pertalite',
    'Tranmisi' : 'Manual',
    }

print("Mobil Lama:", mobil)

mobil['merek'] = input("Masukkan merek mobil baru: ")
mobil['tipe'] = input("Masukkan tipe mobil baru: ")
mobil['tahun'] = int(input("Masukkan tahun mobil baru: "))
mobil['warna'] = input("Masukkan warna mobil baru: ")
mobil['No. polisi'] = input("Masukan No. Polisi:")
mobil['Bensin'] = input("Masukan bensin yang di pakai:")
mobil['Tranmisi'] = input("Masukan tranmisi yang digunakan mobiknya:")

print("Mobil Baru:", mobil)