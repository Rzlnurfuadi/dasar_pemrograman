#Nama: Muhammad Rizal Nurfuadi
#NIM: 2400625
#Kelas: RPL 1B

nilai = int(input("masukan nilai: "))

if nilai>=90:
    print(f"nilai {nilai} bernilai A")
elif nilai<90 and nilai>=80:
    print(f"nilai {nilai} bernilai B")
elif nilai<80 and nilai>=70:
    print(f"nilai {nilai} bernilai C")
elif nilai<70:
    print(f"nilai {nilai} Bernilai D")