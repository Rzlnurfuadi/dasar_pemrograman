#Nama: Muhammad Rizal Nurfuadi
#NIM: 2400625
#Kelas: RPL 1B

barang = int(input("masukan jumlah barang: "))

if barang<100:
    c = barang*5000
    print(f"harga barang Rp. {c}")
elif barang>=100 and barang<=150:
    b = barang*4000
    print(f"harga barang Rp. {b}")
elif barang>150:
    a = barang*2500
    print(f"harga barang Rp. {a}")
    