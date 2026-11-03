class Lab_komputer_barang:
    def __init__(self, kode_barang, nama_barang, kategori, jumlah):
        self.kode_barang = kode_barang
        self.nama_barang = nama_barang
        self.kategori = kategori
        self.jumlah = jumlah

    def tampil_info(self):
        print(f"[{self.kode_barang}] {self.nama_barang} | Kategori: {self.kategori} | Jumlah: {self.jumlah}")
 

class Inventaris:
    def __init__(self):
        self.daftar_barang = {}

    def tambah_barang(self, barang):
        if barang.kode_barang in self.daftar_barang:
            print(f"Gagal: Kode '{barang.kode_barang}' sudah digunakan!")
            return False
        self.daftar_barang[barang.kode_barang] = barang
        print(f"Berhasil menambahkan '{barang.nama_barang}'")
        return True

    def tampilkan_semua(self):
        print("\n--- Daftar Seluruh Barang ---")
        if not self.daftar_barang:
            print("Inventaris kosong.")
        for b in self.daftar_barang.values():
            b.tampil_info()

    def cari_barang(self, kode):
        print(f"\n--- Hasil Pencarian Kode: {kode} ---")
        b = self.daftar_barang.get(kode)
        if b:
            b.tampil_info()
        else:
            print("Barang tidak ditemukan!")

    def total_unit(self):
        total = sum(b.jumlah for b in self.daftar_barang.values())
        print(f"\nTotal seluruh unit barang: {total}")

    def tampilkan_kategori_unik(self):
        kategori = {b.kategori for b in self.daftar_barang.values()}
        print("\n--- Kategori Unik ---")
        if not kategori:
            print("Belum ada kategori.")
        for k in kategori:
            print(f"- {k}")


inv = Inventaris()

while True:
    print("\n=== MENU INVENTARIS LAB ===")
    print("1. Tambah Barang Baru")
    print("2. Tampilkan Seluruh Barang")
    print("3. Cari Barang Berdasarkan Kode")
    print("4. Hitung Total Seluruh Unit")
    print("5. Tampilkan Kategori Unik")
    print("6. Keluar")
    
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        kode = input("Masukkan Kode Barang: ")
        nama = input("Masukkan Nama Barang: ")
        kategori = input("Masukkan Kategori: ")
        try:
            jumlah = int(input("Masukkan Jumlah Unit: "))
            inv.tambah_barang(Lab_komputer_barang(kode, nama, kategori, jumlah))
        except ValueError:
            print("Error: Jumlah harus berupa angka integer!")
    elif pilihan == "2":
        inv.tampilkan_semua()
    elif pilihan == "3":
        kode = input("Masukkan Kode Barang yang Dicari: ")
        inv.cari_barang(kode)
    elif pilihan == "4":
        inv.total_unit()
    elif pilihan == "5":
        inv.tampilkan_kategori_unik()
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan menu tidak valid!")