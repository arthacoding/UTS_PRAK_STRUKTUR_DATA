class Barang:
    def __init__(self, kode_barang, nama_barang, stok, harga):
        self.kode_barang = kode_barang
        self.nama_barang = nama_barang
        self.stok = stok
        self.harga = harga

    def tambah_stok(self, jml):
        self.stok += jml
        print(f"Stok {self.nama_barang} berhasil ditambahkan sebanyak {jml}. Stok sekarang: {self.stok}")

    def kurangi_stok(self, jml):
        if jml <= self.stok:
            self.stok -= jml
            print(f"Stok {self.nama_barang} berhasil dikurangi sebanyak {jml}. Stok sekarang: {self.stok}")
        else:
            print(f"Gagal mengurangi stok {self.nama_barang}. Stok tidak mencukupi (sisa: {self.stok})!")

    def total_harga(self, jumlah):
        return jumlah * self.harga

    def tampil_info(self):
        print(f"--- Informasi Barang ---")
        print(f"Kode Barang : {self.kode_barang}")
        print(f"Nama Barang : {self.nama_barang}")
        print(f"Stok        : {self.stok}")
        print(f"Harga       : Rp {self.harga:,.2f}")
        print("-" * 26)


# ==========================================
# STUDI KASUS
# ==========================================

print("=== 1. MEMBUAT 3 OBJEK BARANG ===")
barang1 = Barang("B001", "Buku Tulis", 50, 5000)
barang2 = Barang("B002", "Pulpen Gel", 100, 3000)
barang3 = Barang("B003", "Buku Gambar", 30, 7500)

barang1.tampil_info()
barang2.tampil_info()
barang3.tampil_info()

print("\n=== 2. MENAMBAH DAN MENGURANGI STOK ===")
barang1.tambah_stok(20)      
barang2.kurangi_stok(15)     
barang3.tambah_stok(10)      

print("\n=== 3. TOTAL NILAI MASING-MASING BARANG DI GUDANG ===")
nilai_b1 = barang1.total_harga(barang1.stok)
nilai_b2 = barang2.total_harga(barang2.stok)
nilai_b3 = barang3.total_harga(barang3.stok)

print(f"Total nilai {barang1.nama_barang}: Rp {nilai_b1:,.2f}")
print(f"Total nilai {barang2.nama_barang}: Rp {nilai_b2:,.2f}")
print(f"Total nilai {barang3.nama_barang}: Rp {nilai_b3:,.2f}")

total_seluruh_aset = nilai_b1 + nilai_b2 + nilai_b3
print(f"\n> **Total Keseluruhan Nilai Barang di Gudang: Rp {total_seluruh_aset:,.2f}**")