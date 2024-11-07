a = ["apel","jeruk","ceri","durian","apel"]
#Melihat Jumlah
print(len(a))
#Mengambil satu item
print(a[3])

b = ["aple","jeruk","ceri","durian","apel"]
#data yang ingin di pilih
print(b[1:4])
#nambah item di akhir
a.append("manggis")
print(b)

#mengganti
a = ["hp","laptop","pc","ip"]
a[3]="android"
print(a)
#menambah di tengah tengah
d=["burung","sapi","ayam","ulat"]
d.insert(2,"ular")
print(d)

#menghapus item
c1=["apel","pisang","popaya","jeruk"]
c1.pop(2)
print(c1)

#bisa banyak tipe data dalam 1 list
x=["piring","sesndok",20,True,10.5,"gelas"]
print(x)

#nambah list ke list lain
c1.extend(x)
print(c1)

#mengurut(tipe data harus sama)
z=["piring","sesndok","garpu","gelas"]
z.sort()

#menghapus item (nama item)
print(z)
z.remove("garpu")

#tuple menggunakan 
g=("meja","lampu","kursi","meja","bangku")
print(g)

g=("meja","lampu","kursi","meja","bangku")
x=list(g)
x[2]="bola"
g=tuple(x)
print(g)

#manipulasi data tupel
g1=("meja","lampu","kursi","meja","bangku")
x1=list(g1)
x1.insert(2,"lemari")
x1.append("kasur")
x1.pop(4)
g1=tuple(x1)
print(g1)