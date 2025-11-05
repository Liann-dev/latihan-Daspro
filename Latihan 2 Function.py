# Latihan 2
# Program login dengan 3 kesempatan Admin dengan fungsi
# Fungsi untuk mengecek password saja
def cek_password(password, password_benar):
    return password == password_benar

# Prosedur utama untuk proses login
def proses_login():
    password_benar = "Latihan"
    username_benar = "Daspro123"
    maks_percobaan = 3
    percobaan = 0

    while percobaan < maks_percobaan:
        password_input = input("Haloo Budi, Silahkan Masukkan password: ")

        if cek_password(password_input, password_benar):
            print(f"Login berhasil! Selamat datang, {username_benar}.")
            break
        else:
            percobaan += 1
            sisa = maks_percobaan - percobaan
            if sisa > 0:
                print(f"Password salah. Kesempatan tersisa: {sisa}")
            else:
                print("Kesempatan habis. Login gagal.")
                break
proses_login()
