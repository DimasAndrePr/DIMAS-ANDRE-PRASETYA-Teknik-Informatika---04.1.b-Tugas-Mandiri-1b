from collections import deque


class QueueMahasiswa:
    def __init__(self):
        self.data = deque()

    # Enqueue: menambahkan data ke belakang antrean
    def tambah(self, mahasiswa):
        self.data.append(mahasiswa)

    # Dequeue: mengambil data dari depan antrean
    def layani(self):
        if self.kosong():
            return None

        return self.data.popleft()

    # Front / Peek: melihat data paling depan
    def lihat_terdepan(self):
        if self.kosong():
            return None

        return self.data[0]

    # IsEmpty: mengecek apakah antrean kosong
    def kosong(self):
        return len(self.data) == 0

    # Mengembalikan data ke depan antrean
    # Digunakan saat Undo Dequeue
    def kembalikan_ke_depan(self, mahasiswa):
        self.data.appendleft(mahasiswa)

    # Menghapus data paling belakang
    # Digunakan saat Undo Enqueue
    def hapus_terakhir(self):
        if self.kosong():
            return None

        return self.data.pop()

    # Menampilkan seluruh antrean
    def tampilkan(self):
        if self.kosong():
            print("Antrean kosong.")
            return

        print("\n=== ISI ANTREAN ===")

        for mahasiswa in self.data:
            print(
                mahasiswa["nomor"],
                "-",
                mahasiswa["nama"]
            )