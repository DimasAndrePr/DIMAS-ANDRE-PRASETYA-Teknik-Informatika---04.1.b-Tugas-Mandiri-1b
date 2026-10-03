from queue import QueueMahasiswa
from undo import StackUndo


antrean = QueueMahasiswa()
undo_stack = StackUndo()


# ==========================================
# TAMBAH MAHASISWA
# ==========================================

def tambah_mahasiswa():
    print("\n=== PENAMBAHAN DATA ===")

    nomor = input("Nomor urut     : ")
    nama = input("Nama mahasiswa : ")

    mahasiswa = {
        "nomor": nomor,
        "nama": nama
    }

    # Enqueue
    antrean.tambah(mahasiswa)

    # Simpan aktivitas untuk Undo
    undo_stack.tambah({
        "jenis": "enqueue",
        "data": mahasiswa,
        "deskripsi": f"Menambahkan {nama} ke antrean"
    })

    print("Data berhasil ditambahkan.")


# ==========================================
# MELAYANI MAHASISWA
# ==========================================

def layani_mahasiswa():
    print("\n=== PENGHAPUSAN / PENGAMBILAN DATA ===")

    # Dequeue
    mahasiswa = antrean.layani()

    if mahasiswa is None:
        print("Antrean kosong.")
        return

    print(
        "Mahasiswa yang dilayani:",
        mahasiswa["nomor"],
        "-",
        mahasiswa["nama"]
    )

    # Simpan aktivitas untuk Undo
    undo_stack.tambah({
        "jenis": "dequeue",
        "data": mahasiswa,
        "deskripsi": f"Melayani {mahasiswa['nama']} dari antrean"
    })


# ==========================================
# MELIHAT DATA TERDEPAN
# ==========================================

def lihat_terdepan():
    print("\n=== DATA TERDEPAN ===")

    # Front / Peek
    mahasiswa = antrean.lihat_terdepan()

    if mahasiswa is None:
        print("Antrean kosong.")
        return

    print("Nomor :", mahasiswa["nomor"])
    print("Nama  :", mahasiswa["nama"])


# ==========================================
# CEK ANTREAN
# ==========================================

def cek_antrean():
    print("\n=== KONDISI ANTREAN ===")

    # IsEmpty
    if antrean.kosong():
        print("Antrean dalam kondisi kosong.")
    else:
        print("Antrean masih memiliki data.")


# ==========================================
# UNDO AKTIVITAS
# ==========================================

def undo_aktivitas():
    print("\n=== UNDO AKTIVITAS ===")

    # Pop
    aktivitas = undo_stack.ambil()

    if aktivitas is None:
        print("Tidak ada aktivitas yang dapat di-Undo.")
        return

    # Undo Enqueue
    if aktivitas["jenis"] == "enqueue":
        mahasiswa = antrean.hapus_terakhir()

        if mahasiswa is not None:
            print(
                "Undo berhasil:",
                mahasiswa["nama"],
                "dikeluarkan dari antrean."
            )

    # Undo Dequeue
    elif aktivitas["jenis"] == "dequeue":
        mahasiswa = aktivitas["data"]

        antrean.kembalikan_ke_depan(mahasiswa)

        print(
            "Undo berhasil:",
            mahasiswa["nama"],
            "dikembalikan ke bagian depan antrean."
        )


# ==========================================
# MELIHAT AKTIVITAS TERAKHIR
# ==========================================

def lihat_aktivitas_terakhir():
    print("\n=== AKTIVITAS TERAKHIR ===")

    # Peek / Top
    aktivitas = undo_stack.lihat_terakhir()

    if aktivitas is None:
        print("Belum ada aktivitas.")
        return

    print(aktivitas["deskripsi"])


# ==========================================
# CEK STACK UNDO
# ==========================================

def cek_undo():
    print("\n=== KONDISI STACK UNDO ===")

    # IsEmpty
    if undo_stack.kosong():
        print("Stack Undo dalam kondisi kosong.")
    else:
        print("Stack Undo masih memiliki aktivitas.")


# ==========================================
# TAMPILKAN ANTREAN
# ==========================================

def tampilkan_antrean():
    antrean.tampilkan()


# ==========================================
# TAMPILKAN RIWAYAT UNDO
# ==========================================

def tampilkan_riwayat():
    undo_stack.tampilkan()


# ==========================================
# MENU ANTREAN
# ==========================================

def menu_antrean():

    while True:
        print("\n==============================")
        print("        MENU ANTREAN")
        print("==============================")
        print("1. Penambahan data")
        print("2. Penghapusan / pengambilan data")
        print("3. Melihat data terdepan")
        print("4. Memeriksa kondisi kosong")
        print("5. Melihat seluruh antrean")
        print("6. Kembali")
        print("==============================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_mahasiswa()

        elif pilihan == "2":
            layani_mahasiswa()

        elif pilihan == "3":
            lihat_terdepan()

        elif pilihan == "4":
            cek_antrean()

        elif pilihan == "5":
            tampilkan_antrean()

        elif pilihan == "6":
            break

        else:
            print("Pilihan tidak tersedia.")


# ==========================================
# MENU UNDO
# ==========================================

def menu_undo():

    while True:
        print("\n==============================")
        print("          MENU UNDO")
        print("==============================")
        print("1. Undo aktivitas")
        print("2. Melihat aktivitas terakhir")
        print("3. Memeriksa kondisi kosong")
        print("4. Melihat riwayat aktivitas")
        print("5. Kembali")
        print("==============================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            undo_aktivitas()

        elif pilihan == "2":
            lihat_aktivitas_terakhir()

        elif pilihan == "3":
            cek_undo()

        elif pilihan == "4":
            tampilkan_riwayat()

        elif pilihan == "5":
            break

        else:
            print("Pilihan tidak tersedia.")


# ==========================================
# PROGRAM UTAMA
# ==========================================

while True:

    print("\n====================================")
    print("      SISTEM LAYANAN MAHASISWA")
    print("====================================")
    print("1. Fitur Antrean")
    print("2. Fitur Undo")
    print("3. Keluar")
    print("====================================")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        menu_antrean()

    elif pilihan == "2":
        menu_undo()

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")