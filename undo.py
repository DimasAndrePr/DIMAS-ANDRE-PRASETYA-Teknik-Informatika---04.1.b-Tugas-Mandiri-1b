class StackUndo:
    def __init__(self):
        self.data = []

    # Push: menyimpan aktivitas baru
    def tambah(self, aktivitas):
        self.data.append(aktivitas)

    # Pop: mengambil aktivitas terakhir
    def ambil(self):
        if self.kosong():
            return None

        return self.data.pop()

    # Peek / Top: melihat aktivitas terakhir
    def lihat_terakhir(self):
        if self.kosong():
            return None

        return self.data[-1]

    # IsEmpty: mengecek apakah Stack kosong
    def kosong(self):
        return len(self.data) == 0

    # Menampilkan riwayat aktivitas
    def tampilkan(self):
        if self.kosong():
            print("Belum ada aktivitas.")
            return

        print("\n=== RIWAYAT AKTIVITAS ===")

        for i, aktivitas in enumerate(
            reversed(self.data),
            start=1
        ):
            print(i, "-", aktivitas["deskripsi"])