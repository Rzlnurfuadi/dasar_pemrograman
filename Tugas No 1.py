#nama: Muhammad Rizal Nurfuadi
#NIM: 4200625

#daftar nilai mahasiswa
nilaimahasiswa = [88, 75, 63, 97, 82, 74, 91, 80, 81, 63]

#data nilai maksimum, minimum, dan nilai rata rata
nilaimaksimum = max(nilaimahasiswa)
nilaiminimum = min(nilaimahasiswa)
nilairatarata = sum(nilaimahasiswa) / len(nilaimahasiswa)

print ("nilai maksimum:", nilaimaksimum)
print ("nilai minimum:", nilaiminimum)
print ("nilai rata rata:", nilairatarata)

#angka terbesar kedua dalam daftar nilai
nilaiunik = list(set(nilaimahasiswa))
nilaiunik.sort()

nilaiterbesarkedua = nilaiunik[-2]
print("Nilai terbesar kedua:", nilaiterbesarkedua)