# Meminta input nama pasangan dari pengguna
suami1 = input("Masukkan nama Suami 1: ")
istri1 = input("Masukkan nama Istri 1: ")
suami2 = input("Masukkan nama Suami 2: ")
istri2 = input("Masukkan nama Istri 2: ")
suami3 = input("Masukkan nama Suami 3: ")
istri3 = input("Masukkan nama Istri 3: ")

# Menyusun pasangan suami-istri
pasangan = {
    suami1: istri1,
    suami2: istri2,
    suami3: istri3
}

# Status awal
start_side = {suami1, istri1, suami2, istri2, suami3, istri3}
end_side = set()
boat = set()

# Fungsi untuk memeriksa apakah aturan dilanggar
def is_valid_state(side):
    for suami in pasangan:
        istri = pasangan[suami]
        # Jika istri ada di sisi yang sama dengan pria lain tanpa suaminya, aturan dilanggar
        if istri in side and suami not in side:
            # Cek jika ada pria lain di sisi yang sama
            if any(p in side for p in pasangan if p != suami):
                return False
    return True

# Fungsi untuk mencetak kondisi terkini dari setiap sisi sungai
def print_state():
    print("Di sisi awal:", start_side)
    print("Di sisi akhir:", end_side)
    print("Di perahu:", boat)
    print("-" * 30)

# Proses penyeberangan
def menyeberang():
    global start_side, end_side, boat
    
    # Langkah-langkah untuk menyeberangkan pasangan tanpa melanggar aturan
    steps = [
        # Langkah manual
        ({suami1, suami2}, "Langkah 1"),
        ({suami1}, "Langkah 2"),
        ({istri1, istri2}, "Langkah 3"),
        ({suami2}, "Langkah 4"),
        ({suami1, suami3}, "Langkah 5"),
        ({suami1}, "Langkah 6"),
        ({istri1, istri3}, "Langkah 7"),
        ({suami3}, "Langkah 8"),
        ({suami1, suami2}, "Langkah 9"),
        ({suami1}, "Langkah 10"),
        ({istri1, istri2}, "Langkah 11"),
        ({suami2}, "Langkah 12"),
    ]
    
    # Menjalankan setiap langkah
    for step, description in steps:
        print(description)
        # Menyeberang dari start_side ke end_side
        if step.issubset(start_side):
            start_side -= step
            boat = step
        # Kembali dari end_side ke start_side
        else:
            end_side -= step
            boat = step
        
        # Memindahkan boat ke sisi tujuan
        if boat.issubset(start_side):
            end_side.update(boat)
        else:
            start_side.update(boat)
        
        boat = set()  # Kosongkan perahu di setiap langkah
        print_state()
        
        # Periksa apakah aturan dilanggar di setiap sisi
        if not is_valid_state(start_side) or not is_valid_state(end_side):
            print("Aturan dilanggar! Ulangi proses.")
            return

# Menjalankan proses menyeberang
menyeberang()

# Cek apakah semua orang berhasil menyeberang
if not start_side:
    print("Semua orang berhasil menyeberang dengan aman!")
else:
    print("Masih ada yang tertinggal di sisi awal.")