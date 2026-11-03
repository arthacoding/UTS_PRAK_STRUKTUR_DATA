class Node:
    def __init__(self, judul_lagu, penyanyi, durasi):
        self.judul_lagu = judul_lagu
        self.penyanyi = penyanyi
        self.durasi = durasi
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def tambah_lagu_diakhir(self, judul_lagu, penyanyi, durasi):
        new_node = Node(judul_lagu, penyanyi, durasi)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        print(f"Lagu '{judul_lagu}' berhasil ditambahkan.")

    def hapus_lagu_diawal(self):
        if not self.head:
            print("Playlist kosong!")
            return
        if self.head == self.current:
            self.current = self.head.next
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.current = None
        else:
            self.head = self.head.next
            self.head.prev = None
        print("Lagu di awal berhasil dihapus.")

    def tampilkan_daftar(self):
        if not self.head:
            print("Playlist kosong!")
            return
        curr = self.head
        print("\n=== DAFTAR PLAYLIST ===")
        while curr:
            status = " (Sedang Diputar)" if curr == self.current else ""
            print(f"- {curr.judul_lagu} oleh {curr.penyanyi} ({curr.durasi} menit){status}")
            curr = curr.next
        print("=======================\n")

    def navigasi_maju(self):
        if not self.current:
            print("Tidak ada lagu yang sedang diputar.")
            return
        if self.current.next:
            self.current = self.current.next
            print(f"Memutar: {self.current.judul_lagu} - {self.current.penyanyi}")
        else:
            print("Sudah berada di lagu terakhir.")

    def navigasi_mundur(self):
        if not self.current:
            print("Tidak ada lagu yang sedang diputar.")
            return
        if self.current.prev:
            self.current = self.current.prev
            print(f"Memutar: {self.current.judul_lagu} - {self.current.penyanyi}")
        else:
            print("Sudah berada di lagu pertama.")

playlist = Playlist()

playlist.tambah_lagu_diakhir("Fix You", "Coldplay", "4.5")
playlist.tambah_lagu_diakhir("Yellow", "Coldplay", "4.3")
playlist.tambah_lagu_diakhir("Perfect", "Ed Sheeran", "4.2")
playlist.tambah_lagu_diakhir("The Scientist", "Coldplay", "5.1")
playlist.tambah_lagu_diakhir("Shape of You", "Ed Sheeran", "3.5")

while True:
    print("\n=== MENU PLAYLIST MUSIK ===")
    print("1. Tambah Lagu di Akhir")
    print("2. Hapus Lagu di Awal")
    print("3. Navigasi Maju (Next)")
    print("4. Navigasi Mundur (Prev)")
    print("5. Tampilkan Seluruh Daftar Lagu")
    print("6. Keluar")
    
    pilihan = input("Pilih menu (1-6): ")
    
    if pilihan == "1":
        judul = input("Masukkan judul lagu: ")
        penyanyi = input("Masukkan penyanyi: ")
        durasi = input("Masukkan durasi (menit): ")
        playlist.tambah_lagu_diakhir(judul, penyanyi, durasi)
    elif pilihan == "2":
        playlist.hapus_lagu_diawal()
    elif pilihan == "3":
        playlist.navigasi_maju()
    elif pilihan == "4":
        playlist.navigasi_mundur()
    elif pilihan == "5":
      playlist.tampilkan_daftar()
    elif pilihan == "6":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")