#Nama : Muhammad Rizal Nurfuadi
#Nim : 2400625
#Kelas : Rpl 1B

perm2 = 450000

panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
tinggi = float(input("Masukkan tinggi: "))

luasdinding = 2 * (panjang * tinggi) + 2 * (lebar * tinggi)

totalbiaya = luasdinding * perm2

print(f"Luas permukaan dinding: {luasdinding} m2")
print(f"Total biaya: Rp {totalbiaya}")
