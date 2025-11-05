# Latihan 1
# No 1
def fibonacci(angka):
    a, b = 0, 1
    hasil = []
    for x in range(angka):
        hasil.append(a)
        a, b = b, a + b
    return hasil


angka = int(input("Masukkan jumlah deret Fibonacci: "))
print("Deret Fibonacci:", fibonacci(angka))

# No 2 
def volume_tabung(r, t):
    return 3.14 * r * r * t

print(volume_tabung(5, 10))

# No 3
def hitung_total_rata(*angka):
    total = sum(angka)
    rata = total / len(angka)
    return total, rata

angka_input = input("Masukkan beberapa angka (pisahkan dengan koma tanpa spasi): ")

angka_list = [float(x) for x in angka_input.split(",")]

total, rata = hitung_total_rata(*angka_list)
print(f"Total: {total}")
print(f"Rata-rata: {rata}")
