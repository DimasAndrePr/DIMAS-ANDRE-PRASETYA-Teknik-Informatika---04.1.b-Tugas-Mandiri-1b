import unittest
from undo import StackUndo


class TestStackUndo(unittest.TestCase):

    def setUp(self):
        self.undo = StackUndo()

    # 1. Pengujian penambahan data
    def test_penambahan_data(self):
        aktivitas = {
            "jenis": "enqueue",
            "data": {
                "nomor": "001",
                "nama": "Andi"
            },
            "deskripsi": "Menambahkan Andi ke antrean"
        }

        self.undo.tambah(aktivitas)

        self.assertFalse(self.undo.kosong())
        self.assertEqual(
            self.undo.lihat_terakhir(),
            aktivitas
        )

    # 2. Pengujian penghapusan data
    def test_penghapusan_data(self):
        aktivitas1 = {
            "jenis": "enqueue",
            "data": {
                "nomor": "002",
                "nama": "Budi"
            },
            "deskripsi": "Menambahkan Budi ke antrean"
        }

        aktivitas2 = {
            "jenis": "enqueue",
            "data": {
                "nomor": "003",
                "nama": "Citra"
            },
            "deskripsi": "Menambahkan Citra ke antrean"
        }

        self.undo.tambah(aktivitas1)
        self.undo.tambah(aktivitas2)

        hasil = self.undo.ambil()

        # Citra masuk terakhir, jadi Citra keluar lebih dulu
        self.assertEqual(hasil, aktivitas2)

        # Budi masih berada di Stack
        self.assertEqual(
            self.undo.lihat_terakhir(),
            aktivitas1
        )

    # 3. Pengujian melihat data terdepan / Top
    def test_melihat_data_terakhir(self):
        aktivitas1 = {
            "jenis": "enqueue",
            "data": {
                "nomor": "004",
                "nama": "Dimas"
            },
            "deskripsi": "Menambahkan Dimas ke antrean"
        }

        aktivitas2 = {
            "jenis": "enqueue",
            "data": {
                "nomor": "005",
                "nama": "Eka"
            },
            "deskripsi": "Menambahkan Eka ke antrean"
        }

        self.undo.tambah(aktivitas1)
        self.undo.tambah(aktivitas2)

        hasil = self.undo.lihat_terakhir()

        # Eka berada di posisi paling atas
        self.assertEqual(hasil, aktivitas2)

        # Peek tidak menghapus data
        self.assertFalse(self.undo.kosong())

    # 4. Pengujian kondisi kosong
    def test_memeriksa_kondisi_kosong(self):
        # Kondisi awal Stack harus kosong
        self.assertTrue(self.undo.kosong())

        aktivitas = {
            "jenis": "enqueue",
            "data": {
                "nomor": "005",
                "nama": "Eka"
            },
            "deskripsi": "Menambahkan Eka ke antrean"
        }

        self.undo.tambah(aktivitas)

        # Setelah ditambah, Stack tidak kosong
        self.assertFalse(self.undo.kosong())


if __name__ == "__main__":
    unittest.main()