import numpy as np

# Latihan No 2
nilaiujian30siswa = np.array([80, 75, 90, 85, 70, 95, 60, 88, 92, 78, 84, 76, 
                              89, 91, 73, 87, 82, 94, 77, 81,79, 83, 
                              86, 74, 96, 68, 69, 72, 71, 65])

print("5 Nilai Tersesar:", np.sort(nilaiujian30siswa)[-5:][::-1]) # menampilkan 5 nilai terbesar