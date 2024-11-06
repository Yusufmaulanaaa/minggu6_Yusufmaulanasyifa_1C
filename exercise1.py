# Program untuk menghitung rata-rata nilai ujian siswa

# Meminta jumlah siswa
jumlah_siswa = int(input("Masukkan jumlah siswa: "))

# Variabel untuk menyimpan total nilai
total_nilai = 0

# Meminta input nilai untuk setiap siswa
for i in range(jumlah_siswa):
    nilai = float(input(f"Masukkan nilai ujian siswa ke-{i+1}: "))
    total_nilai += nilai  # Menambahkan nilai siswa ke total

# Menghitung rata-rata nilai
rata_rata = total_nilai / jumlah_siswa

# Menampilkan hasil
print(f"Rata-rata nilai ujian seluruh siswa adalah: {rata_rata:.2f}")
