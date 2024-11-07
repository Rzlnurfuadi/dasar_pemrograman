#Nama: Muhammad Rizal Nurfuadi
#Kelas: RPL 1B
#NIM: 2400625

total = 0
print("Masukkan angka berturut-turut dan masukkan angka negatif untuk menghentikan:")
while True:
    angka = int(input())
    
    if angka < 0: 
        break
    
    total += angka
print("Total =", total)