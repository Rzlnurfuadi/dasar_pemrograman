#nama: Muhammad Rizal Nurfuadi
#NIM: 4200625
#Kelas: RPL 1B

student_info = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Mathematics"},
    "Charlie": {"age": 19, "major": "Physics"}
}

userinput = input("Masukan nama pelajar: ")
print(f"umur {userinput} adalah {student_info[userinput]['age']} dan prodi nya adalah {student_info[userinput]['major']} ")