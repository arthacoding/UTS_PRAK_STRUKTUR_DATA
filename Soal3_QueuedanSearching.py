max_antrean = int(input("Masukkan jumlah maksimum antrian: "))
antrean = []

def cari_pasien(antrean, nama):
    for i in range(len(antrean)):
        if antrean[i].lower() == nama.lower():
            return i
    return -1

while True:
    print("1. Pendaftaran Pasien")
    print("2. Panggil Pasien")
    print("3. Tampilkan Antrean")
    print("4. Cari Pasien")
    print("5. Keluar")
    pilihan = int(input("Masukkan pilihan: "))
    
    if pilihan == 1:
        if len(antrean) < max_antrean:
            nama = input("Masukkan nama pasien: ")
            antrean.append(nama)
            print(f"--Memasukkan {nama} ke antrian--")
        else:
            print("**Antrian sudah penuh**")
    elif pilihan == 2:
        if len(antrean) == 0:
            print("**Maaf, Antrian sudah habis**")
        else:
            print(f"Pasien dipanggil: {antrean.pop(0)}")
    elif pilihan == 3:
        print(antrean)
    elif pilihan == 4:
        nama = input("Masukkan nama yang dicari: ")
        pos = cari_pasien(antrean, nama)
        if pos != -1:
            print(f"Pasien ditemukan di antrean ke-{pos + 1}")
        else:
            print("Pasien tidak ditemukan")
    else:
        print("Keluar... Sampai jumpa lagi..")
        break