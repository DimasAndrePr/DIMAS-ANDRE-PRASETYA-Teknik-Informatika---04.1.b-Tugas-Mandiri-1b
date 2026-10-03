# Tugas Mandiri 1B — Struktur Data Linear

## Sistem Antrean Layanan Mahasiswa dan Fitur Undo

Repository ini berisi implementasi **struktur data linear** menggunakan Python untuk menyelesaikan studi kasus sistem layanan administrasi mahasiswa.

Program memiliki dua fitur utama, yaitu:

- **Queue** untuk sistem antrean layanan mahasiswa.
- **Stack** untuk menyimpan aktivitas dan menjalankan fitur Undo.

---

## Identitas

**Nama:** Dimas Andre Prasetya  
**Program Studi:** Teknik Informatika  
**Mata Kuliah:** Struktur Data  
**Tugas:** Tugas Mandiri 1B  

---

## Studi Kasus

Sistem layanan administrasi mahasiswa membutuhkan struktur data untuk mengatur antrean mahasiswa berdasarkan urutan kedatangan.

Setiap mahasiswa yang datang akan dimasukkan ke dalam antrean dan dilayani mulai dari mahasiswa yang berada di posisi paling depan.

Selain itu, sistem memiliki fitur **Undo** untuk membatalkan aktivitas terakhir yang dilakukan oleh petugas.

Berdasarkan karakteristik tersebut, digunakan dua struktur data:

| Fitur | Struktur Data | Prinsip |
|---|---|---|
| Antrean layanan mahasiswa | Queue | FIFO (First In First Out) |
| Fitur Undo | Stack | LIFO (Last In First Out) |

---

## Struktur Data dan Operasi

### Queue

Queue digunakan untuk mengatur antrean mahasiswa sesuai urutan kedatangan.

Operasi yang digunakan:

- **Enqueue** — menambahkan mahasiswa ke bagian belakang antrean.
- **Dequeue** — mengambil atau melayani mahasiswa dari bagian depan antrean.
- **Front / Peek** — melihat mahasiswa yang berada di bagian depan tanpa menghapusnya.
- **IsEmpty** — memeriksa apakah antrean dalam keadaan kosong.

### Stack

Stack digunakan untuk menyimpan aktivitas petugas sehingga aktivitas terakhir dapat dibatalkan terlebih dahulu.

Operasi yang digunakan:

- **Push** — menambahkan aktivitas ke bagian atas Stack.
- **Pop** — mengambil aktivitas terakhir dari bagian atas Stack.
- **Peek / Top** — melihat aktivitas terakhir tanpa menghapusnya.
- **IsEmpty** — memeriksa apakah Stack dalam keadaan kosong.

---

## Implementasi Program

Program dibuat menggunakan bahasa **Python** dan dipisahkan menjadi beberapa file agar setiap bagian memiliki fungsi yang jelas.

```text
Tugas-Mandiri-1b/
│
├── tests/
│   ├── __init__.py
│   ├── test_queue.py
│   └── test_undo.py
│
├── README.md
├── main.py
├── queue.py
└── undo.py
