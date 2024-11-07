# Daftar nilai mahasiswa
nilaimahasiswa = [88, 75, 63, 97, 82, 74, 91, 80, 81, 63]

# a. Tampilkan data nilai maksimum, minimum, dan nilai rata-rata
nilaimaksimum = max(nilaimahasiswa)
nilaiminimum = min(nilaimahasiswa)
nilairatarata = sum(nilaimahasiswa) / len(nilaimahasiswa)

print("Nilai maksimum:", nilaimaksimum)
print("Nilai minimum:", nilaiminimum)
print("Nilai rata-rata:", nilairatarata)

# b. Tampilkan angka terbesar kedua dalam daftar nilai
# Menggunakan set untuk menghilangkan duplikat, kemudian mengurutkan
nilaiunique = list(set(nilaimahasiswa))
nilaiunique.sort()

if len(nilaiunique) > 1:
    nilaiterbesarkedua = nilaiunique[-2]  # Mengambil nilai terbesar kedua
    print("Angka terbesar kedua:", nilaiterbesarkedua)
else:
    print("Tidak ada angka terbesar kedua.")


#sama saja
def cari_terbesar_kedua(daftar):
    # Menghapus duplikat dan mengurutkan daftar
    daftar_unik = list(set(daftar))
    daftar_unik.sort()
    
    # Mengembalikan angka terbesar kedua
    if len(daftar_unik) < 2:
        return None  # Jika tidak ada angka kedua terbesar
    else:
        return daftar_unik[-2]

# Contoh penggunaan
daftar_angka = [10, 20, 4, 45, 99, 99, 45]
hasil = cari_terbesar_kedua(daftar_angka)
print("Angka terbesar kedua adalah:", hasil)
















# Mendefinisikan tuple dengan pasangan (latitude, longitude) untuk beberapa kota
jakarta = (-6.2008, 106.8456)
bandung = (-6.9175, 107.6191)
surabaya = (-7.2575, 112.7521)

# Mengumpulkan semua lokasi dalam sebuah dictionary untuk kemudahan akses
lokasi = {
    "Jakarta": jakarta,
    "Bandung": bandung,
    "Surabaya": surabaya
}

# a. Menampilkan data koordinat untuk kota Bandung
koordinat_bandung = lokasi["Bandung"]
print("Koordinat Bandung:", koordinat_bandung)

# b. Menampilkan jumlah lokasi yang tersimpan
jumlah_lokasi = len(lokasi)
print("Jumlah lokasi yang tersimpan:", jumlah_lokasi)