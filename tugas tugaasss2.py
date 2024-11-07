#Nama : Muhammad Rizal Nurfuadi
#NIM : 2400625
#Kelas : RPL 1B 

students = {
    "Alice": "Computer Science",
    "Bob" : "Mathematics",
    "Charlie" : "Physics",
    "David" : "Computer Science",
    "Eva" : "Mathematics"
 }
jumlahjurusan = {}

for students in students.values():
    if students in jumlahjurusan:
        jumlahjurusan[students] += 1
    else:
        jumlahjurusan[students] = 1

for students, jumlah in jumlahjurusan.items():
    print(f"jurusan {students}, jumlah mahasiswa: {jumlah}")
