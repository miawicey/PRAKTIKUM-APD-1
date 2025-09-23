print("Supermarket Kasir Vita")
print("brum brum brum")
print("welcome to my supermarket")

# JENIS BARANG
barang1 = "Susu"
barang2 = "Nabati"
barang3 = "Indomie"

# HARGA BARANG
harga1 = 4000
harga2 = 3500
harga3 = 4000

# JUMLAH BARANG
jumlah1 = 5
jumlah2 = 6
jumlah3 = 10

# DISKON
diskon = 0.5  # 50%
ada_diskon = True

# HITUNG TOTAL PER BARANG
total1 = harga1 * jumlah1
total2 = harga2 * jumlah2
total3 = harga3 * jumlah3

# SUBTOTAL
subtotal = total1 + total2 + total3

# POTONGAN DISKON
if ada_diskon:
    potongan = subtotal * diskon
else:
    potongan = 0

# TOTAL BAYAR
total_bayar = subtotal - potongan

# CETAK STRUK
print("Barang:", barang1, "| Harga:", harga1, "| Jumlah:", jumlah1, "| Total:", total1)
print("Barang:", barang2, "| Harga:", harga2, "| Jumlah:", jumlah2, "| Total:", total2)
print("Barang:", barang3, "| Harga:", harga3, "| Jumlah:", jumlah3, "| Total:", total3)
print("Subtotal:", subtotal)
print("Diskon 50%, potongan:", potongan)
print("Total Bayar:", total_bayar)
print("Ada Diskon?", ada_diskon)
print("Terima Kasih")
print("Datang lagi yaaa ke supermarket vita")
print("brum brum brum")