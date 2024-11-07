#Nama: Muhammad Rizal Nurfuadi
#NIM: 2400625
#Kelas: RPL 1B

umur = int(input("Masukan umur: "))
kelamin = input("masukan jenis kelamin wanita/pria: ").lower()
tinggibadan = int(input("masukan tinggi bandan: "))
iq = int(input("masukan iq: "))

if umur>=18 and umur<=25:
    if(kelamin == "wanita" and tinggibadan >=170 and iq >= 130):
        print("dapat menjadi catwalk")
    elif(kelamin == "pria" and tinggibadan >=175 and iq >= 130):
        print("dapat menjadi catwalk")
    else:
        print("tidak memenuhi persyaratan")
else:
    print("umur tidak sesuai")