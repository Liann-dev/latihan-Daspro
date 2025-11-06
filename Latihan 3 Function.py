# Latihan Berlianda

# Latihan 3
# Program menghitung selisih waktu (jam - menit - detik)

print("=== Hitung Selisih Waktu ===")

# Input waktu mulai
jam_mulai = int(input("Masukkan jam mulai (0-23): "))
menit_mulai = int(input("Masukkan menit mulai (0-59): "))
detik_mulai = int(input("Masukkan detik mulai (0-59): "))

# Validasi jam, menit, dan detik
while not (0 <= jam_mulai <= 23 and 0 <= menit_mulai <= 59 and 0 <= detik_mulai <= 59):
    print("Input waktu mulai tidak valid!")
    jam_mulai = int(input("Masukkan jam mulai (0-23): "))
    menit_mulai = int(input("Masukkan menit mulai (0-59): "))
    detik_mulai = int(input("Masukkan detik mulai (0-59): "))

# Input waktu selesai
jam_selesai = int(input("Masukkan jam selesai (0-23): "))
menit_selesai = int(input("Masukkan menit selesai (0-59): "))
detik_selesai = int(input("Masukkan detik selesai (0-59): "))

# Validasi jam, menit, dan detik
while not (0 <= jam_selesai <= 23 and 0 <= menit_selesai <= 59 and 0 <= detik_selesai <= 59):
    print("Input waktu selesai tidak valid!")
    jam_selesai = int(input("Masukkan jam selesai (0-23): "))
    menit_selesai = int(input("Masukkan menit selesai (0-59): "))
    detik_selesai = int(input("Masukkan detik selesai (0-59): "))

# Validasi Urutan Waktu
while (jam_mulai > jam_selesai) or \
      (jam_mulai == jam_selesai and menit_mulai > menit_selesai) or \
      (jam_mulai == jam_selesai and menit_mulai == menit_selesai and detik_mulai > detik_selesai):
    print("Nguwaor, Jam mulai tidak boleh lebih besar dari jam selesai!")
    print("Silakan input ulang waktu mulai yaa:")
    jam_mulai = int(input("Masukkan jam mulai (0-23): "))
    menit_mulai = int(input("Masukkan menit mulai (0-59): "))
    detik_mulai = int(input("Masukkan detik mulai (0-59): "))

# Konversi waktu ke detik
total_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
total_selesai = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai

# Hitung selisih
selisih = total_selesai - total_mulai

# Konversi kembali ke jam, menit, detik
jam = selisih // 3600
selisih %= 3600
menit = selisih // 60
detik = selisih % 60

# Output hasil
print(f"\n===Hasil selisih waktu===")
print(f"{jam} jam, {menit} menit, {detik} detik")
