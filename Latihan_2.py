#Nama: Muhammad Rizal Nurfuadi
#NIM: 2400625
#Kelas: RPL 1B

bilangan = int(input("masukan bilangan: "))
if bilangan > 0:
    if bilangan %2==0:
        print("angka positif genap")
    else:
        print("angka positif ganjil")

elif bilangan < 0:
    if bilangan %2==0:
        print("angka negatif genap")
    else:
        print("angka neegatif ganjil")

else:
    print("angka yang di masukan 0")