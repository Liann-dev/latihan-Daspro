import numpy as np
# Latihan No 1
celcius = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90,])
farenheit = (celcius * 9/5) + 32
print("Suhu dalam Farenheit:", farenheit)
print("Suhu dalam Celcius:", celcius)

# Latihan No 2
nilaiujian30siswa = np.array([80, 75, 90, 85, 70, 95, 60, 88, 92, 78, 84, 76, 
                              89, 91, 73, 87, 82, 94, 77, 81,79, 83, 
                              86, 74, 96, 68, 69, 72, 71, 65])

print("5 Nilai Tersesar:", np.sort(nilaiujian30siswa)[-5:][::-1]) # menampilkan 5 nilai terbesar

# Latihan No 3
keuntunganharian = np.array([5000, 7000, 8000, 6000, 9000, 7500, 8500, 9500, 10000, 11000, 12000, 13000, 14000, 15000,])

ratarata = np.mean(keuntunganharian)
print(f"Rata-rata Keuntungan Harian:" "Rp", ratarata)

keuntungantertinggidenganhari = np.max(keuntunganharian)
print(f"Keuntungan Tertinggi pada hari :", keuntungantertinggidenganhari)
keuntunganterendahdenganhari = np.min(keuntunganharian) 
print("Keuntungan Terendah dalam Sehari:", keuntunganterendahdenganhari)

harikeuntungantertinggi = np.argmax(keuntunganharian) + 1
print("Hari dengan Keuntungan Tertinggi adalah hari ke-", harikeuntungantertinggi)
harikeuntunganterendah = np.argmin(keuntunganharian) + 1
print("Hari dengan Keuntungan Terendah adalah hari ke-", harikeuntunganterendah)
