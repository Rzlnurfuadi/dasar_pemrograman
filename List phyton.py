#Nama: Muhammad Rizal Nurfuadi
#Nim: 2400625
#Kelas: 1B RPL

#manipulasi data list
a=["apel","jeruk","ceri","durian","apel","mangga"]
a[2]="cherry"
print(a)

namaitem=input("masukkan nama item:")
indexitem=int(input("pada index ke:"))
a.insert(indexitem,namaitem)
print("data buah",a)

a.sort()
print(a)