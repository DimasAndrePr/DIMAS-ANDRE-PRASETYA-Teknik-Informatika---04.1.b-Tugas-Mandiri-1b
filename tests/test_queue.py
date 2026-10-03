import unittest
from queue import QueueMahasiswa


class TestQueueMahasiswa(unittest.TestCase):

    def setUp(self):
        self.antrean = QueueMahasiswa()

    # 1. Pengujian penambahan data
    def test_penambahan_data(self):
        andi = {
            "nomor": "001",
            "nama": "Andi"
        }

        self.antrean.tambah(andi)

        self.assertFalse(self.antrean.kosong())
        self.assertEqual(
            self.antrean.lihat_terdepan(),
            andi
        )

    # 2. Pengujian penghapusan data
    def test_penghapusan_data(self):
        budi = {
            "nomor": "002",
            "nama": "Budi"
        }

        citra = {
            "nomor": "003",
            "nama": "Citra"
        }

        self.antrean.tambah(budi)
        self.antrean.tambah(citra)

        hasil = self.antrean.layani()

        # Budi harus keluar lebih dulu
        self.assertEqual(hasil, budi)

        # Setelah Budi diambil, Citra menjadi terdepan
        self.assertEqual(
            self.antrean.lihat_terdepan(),
            citra
        )

    # 3. Pengujian melihat data terdepan
    def test_melihat_data_terdepan(self):
        dimas = {
            "nomor": "004",
            "nama": "Dimas"
        }

        eka = {
            "nomor": "005",
            "nama": "Eka"
        }

        self.antrean.tambah(dimas)
        self.antrean.tambah(eka)

        hasil = self.antrean.lihat_terdepan()

        # Dimas harus menjadi data terdepan
        self.assertEqual(hasil, dimas)

        # Peek tidak menghapus data
        self.assertEqual(
            self.antrean.lihat_terdepan(),
            dimas
        )

    # 4. Pengujian kondisi kosong
    def test_memeriksa_kondisi_kosong(self):
        # Kondisi awal harus kosong
        self.assertTrue(self.antrean.kosong())

        eka = {
            "nomor": "005",
            "nama": "Eka"
        }

        self.antrean.tambah(eka)

        # Setelah ditambahkan, antrean tidak kosong
        self.assertFalse(self.antrean.kosong())


if __name__ == "__main__":
    unittest.main()