#Nama: Muhammad Rizal Nurfuadi
#Nim: 2400625
#Kelas: 1B RPL

#manipulasi data tupel
a=("meja","lampu","gelas","sendok","piring")
x=list(a)
x.insert(2,"lemari")
a=tuple(x)
print(a)

a1=("meja","lampu","gelas","sendok","piring")
x1=list(a1)
x1.append("kasur")
a1=tuple(x1)
print(a1)

a2=("meja","lampu","gelas","sendok","piring")
x2=list(a2)
x2.pop(3)
a2=tuple(x2)
print(a2)