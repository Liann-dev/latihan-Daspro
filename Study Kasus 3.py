import numpy as np

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