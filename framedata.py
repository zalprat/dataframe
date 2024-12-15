import pandas as pd

# Membaca file CSV
file_path = "disperkim-od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_data.csv"
df = pd.read_csv(file_path)

# Menampilkan data dari csv
print("Data yang dibaca:")
print(df.head())

tahun_tertentu = 2015
total_produksi = 0

for index, row in df.iterrows():
    if row["tahun"] == tahun_tertentu:
        total_produksi += row["jumlah_produksi_sampah"]

print(f"\nTotal produksi sampah untuk tahun {tahun_tertentu}: {total_produksi} ton")

total_per_tahun = {}
for index, row in df.iterrows():
    tahun = row["tahun"]
    if tahun not in total_per_tahun:
        total_per_tahun[tahun] = row["jumlah_produksi_sampah"]
    else:
        total_per_tahun[tahun] += row["jumlah_produksi_sampah"]

print("\nTotal produksi sampah per tahun:")
for tahun, total in total_per_tahun.items():
    print(f"Tahun {tahun}: {total} ton")

total_per_kota_per_tahun = {}
for index, row in df.iterrows():
    tahun = row["tahun"]
    kota = row["nama_kabupaten_kota"]
    produksi_sampah = row["jumlah_produksi_sampah"]

    key = (tahun, kota)

    if key not in total_per_kota_per_tahun:
        total_per_kota_per_tahun[key] = produksi_sampah
    else:
        total_per_kota_per_tahun[key] += produksi_sampah

print("\nTotal produksi sampah per Kota/Kabupaten per tahun:")
for (tahun, kota), total in total_per_kota_per_tahun.items():
    print(f"Tahun {tahun}, {kota}: {total} ton")
