# Tugas 1 \- Algoritma dan Pemrograman

Repository ini berisi implementasi program Python 3 (`soal1.py` dan `soal2.py`) serta dokumentasi rancangan fungsi dan analisis perhitungan untuk **Tugas 1 Algoritma dan Pemrograman**.

## Soal 1: Rekapitulasi Nilai Mata Kuliah (`soal1.py`)

### 1\. Deskripsi Program dan Keluaran (Bagian a)

Program `soal1.py` digunakan untuk mengolah daftar nilai lima mahasiswa yang terdiri dari komponen **Tugas (**$30\%$**)**, **UTS (**$30\%$**)**, dan **UAS (**$40\%$**)**, mengonversinya menjadi nilai huruf dan status kelulusan, serta menampilkan rekapitulasi nilai dalam bentuk tabel beserta rata-rata nilai akhir kelas dan jumlah mahasiswa yang lulus.

**Contoh Keluaran Program:**

```
Nama       | Nilai Akhir | Huruf | Status
------------------------------------------
Andi       |       81.00 | B     | Lulus     
Bunga      |       87.70 | A     | Lulus     
Citra      |       51.50 | D     | Tidak Lulus
Dimas      |       72.50 | B     | Lulus     
Eka        |       35.00 | E     | Tidak Lulus
------------------------------------------
Rata-rata Nilai Akhir Kelas: 65.54
Banyaknya Mahasiswa Lulus  : 3

```

### 2\. Tabel Rancangan Fungsi (Bagian b)

Program disusun secara modular dengan memisahkan logika perhitungan tiap mahasiswa dan pencetakan rekapitulasi ke dalam **empat fungsi utama** di luar fungsi `main()`:

| Nama Fungsi | Parameter | Mengembalikan Nilai atau Tidak | Tugas yang Dikerjakan |
| :---- | :---- | :---- | :---- |
| `hitung_nilai_akhir` | `tugas`, `uts`, `uas` | **Ya** (*non-void*, mengembalikan `float`) | Menghitung nilai akhir satu mahasiswa dengan rumus $(0.3 \times \text{tugas}) + (0.3 \times \text{uts}) + (0.4 \times \text{uas})$. |
| `tentukan_huruf` | `nilai` | **Ya** (*non-void*, mengembalikan `str`) | Mengonversi nilai akhir angka menjadi nilai huruf (`A`, `B`, `C`, `D`, atau `E`) sesuai batas rentang nilai pada soal. |
| `cek_status` | `huruf` | **Ya** (*non-void*, mengembalikan `str`) | Menentukan keterangan kelulusan (`"Lulus"` jika nilai huruf `A`, `B`, atau `C`, dan `"Tidak Lulus"` jika selain itu). |
| `cetak_tabel` | `daftar_mhs` | **Tidak** (*void*) | Melakukan iterasi pada seluruh data mahasiswa, memanggil fungsi perhitungan dan penentuan status, mencetak baris tabel rekapitulasi, serta menghitung dan menampilkan rata-rata nilai akhir kelas dan banyaknya mahasiswa yang lulus. |
| `main` *(fungsi utama)* | Tidak ada | **Tidak** (*void*) | Menyimpan daftar data nilai mahasiswa dan memanggil fungsi `cetak_tabel` untuk menjalankan alur utama program. |

### 3\. Perhitungan Manual dan Perbandingan Keluaran (Bagian c)

Berikut adalah perhitungan manual nilai akhir dan nilai huruf untuk **Andi** dan **Dimas**:

#### A. Perhitungan Manual Andi

* **Data Nilai:** $\text{Tugas} = 80$, $\text{UTS} = 70$, $\text{UAS} = 90$

* **Nilai Akhir:**

  $$
  \text{Nilai Akhir} = (80 \times 0.3) + (70 \times 0.3) + (90 \times 0.4) = 24 + 21 + 36 = 81.00
  $$

* **Nilai Huruf:** Karena nilai akhir $81.00$ berada pada rentang $70 \le \text{nilai} < 85$, maka nilai hurufnya adalah **B** (Status: **Lulus**).

#### B. Perhitungan Manual Dimas

* **Data Nilai:** $\text{Tugas} = 75$, $\text{UTS} = 80$, $\text{UAS} = 65$

* **Nilai Akhir:**

  $$
  \text{Nilai Akhir} = (75 \times 0.3) + (80 \times 0.3) + (65 \times 0.4) = 22.5 + 24 + 26 = 72.50
  $$

* **Nilai Huruf:** Karena nilai akhir $72.50$ berada pada rentang $70 \le \text{nilai} < 85$, maka nilai hurufnya adalah **B** (Status: **Lulus**).

#### C. Perbandingan dengan Keluaran Program

| Nama Mahasiswa | Hasil Hitung Manual (Angka / Huruf) | Keluaran Program `soal1.py` (Angka / Huruf) | Keterangan |
| :---- | :---- | :---- | :---- |
| **Andi** | `81.00` / `B` | `81.00` / `B` | Sesuai |
| **Dimas** | `72.50` / `B` | `72.50` / `B` | Sesuai |

### 4\. Analisis Penambahan Fitur Nilai Akhir Tertinggi (Bagian d)

Apabila dosen meminta tambahan fitur untuk **menampilkan nama mahasiswa dengan nilai akhir tertinggi**, berikut adalah rincian dampak perubahan pada kode yang dikaitkan dengan cara pengelompokan fungsi pada bagian (b):

1. **Fungsi yang Tidak Perlu Disentuh Sama Sekali:**

   * `hitung_nilai_akhir(tugas, uts, uas)`

   * `tentukan_huruf(nilai)`

   * `cek_status(huruf)`

   * `main()` *(apabila pemanggilan fitur dan pencetakan hasil dilakukan di dalam `cetak_tabel`)*

   * **Alasan:** Pada rancangan bagian (b), ketiga fungsi bantu (`hitung_nilai_akhir`, `tentukan_huruf`, dan `cek_status`) telah dikelompokkan berdasarkan prinsip *single responsibility*—masing-masing hanya memproses aturan penilaian untuk **satu mahasiswa**. Karena rumus bobot nilai, aturan konversi huruf, dan syarat kelulusan tidak mengalami perubahan, ketiga fungsi ini dapat langsung digunakan kembali tanpa perlu diubah sedikit pun.

2. **Fungsi yang Perlu Ditambah:**

   * **Menambah fungsi `cari_nilai_tertinggi(daftar_mhs)` (*non-void*):** Agar tetap sesuai dengan aturan bahwa satu fungsi sebaiknya mengerjakan satu tugas yang jelas, kita perlu menambahkan satu fungsi baru yang menerima parameter `daftar_mhs`. Di dalamnya, fungsi ini melakukan perulangan untuk memanggil kembali `hitung_nilai_akhir(tugas, uts, uas)`, membandingkan nilai akhir setiap mahasiswa, lalu mengembalikan nama mahasiswa dengan nilai akhir tertinggi.  
3. **Fungsi yang Perlu Diubah:**

   * **Mengubah fungsi `cetak_tabel(daftar_mhs)` (*void*):** Pada pengelompokan kode di bagian (b), fungsi `cetak_tabel` bertanggung jawab menampilkan seluruh rekapitulasi akhir kelas (tabel nilai, rata-rata kelas, dan jumlah mahasiswa lulus). Oleh karena itu, perubahan cukup dilakukan pada bagian akhir fungsi `cetak_tabel` dengan memanggil fungsi baru `cari_nilai_tertinggi(daftar_mhs)` dan mencetak nama mahasiswa peraih nilai tertinggi tersebut.

## Soal 2: Struk Pengiriman Toko Daring (`soal2.py`)

### 1\. Deskripsi Program dan Keluaran (Bagian a)

Program `soal2.py` digunakan untuk menghitung ongkos kirim lima pesanan pelanggan toko daring berdasarkan berat paket, jarak pengiriman, dan status keanggotaan, lalu menampilkannya dalam bentuk tabel rincian struk beserta total pendapatan ongkos kirim hari ini.

**Contoh Keluaran Program:**

```
Pelanggan  | Biaya Berat | Biaya Jarak | Potongan | Ongkir Akhir
----------------------------------------------------------------
Rina       | Rp    10000 | Rp        0 | Rp     0 | Rp     10000
Sari       | Rp    22000 | Rp     5000 | Rp     0 | Rp     27000
Tono       | Rp    22000 | Rp     5000 | Rp  2700 | Rp     24300
Umar       | Rp    10000 | Rp     5000 | Rp  1500 | Rp     13500
Vina       | Rp    34000 | Rp        0 | Rp     0 | Rp     34000
----------------------------------------------------------------
Total Pendapatan Ongkos Kirim Hari Ini: Rp 108800

```

### 2\. Tabel Rancangan Fungsi (Bagian b)

Program dikelompokkan menjadi **empat fungsi utama** di luar fungsi `main()` agar setiap aturan perhitungan tarif terpisah dengan jelas:

| Nama Fungsi | Parameter | Mengembalikan Nilai atau Tidak | Tugas yang Dikerjakan |
| :---- | :---- | :---- | :---- |
| `hitung_biaya_berat` | `berat` | **Ya** (*non-void*, mengembalikan `int`) | Menghitung biaya pengiriman berdasarkan berat paket ($\text{Rp}10.000$ untuk berat $\le 2\text{ kg}$, ditambah $\text{Rp}4.000$ untuk setiap kelebihan kg). |
| `hitung_biaya_jarak` | `jarak` | **Ya** (*non-void*, mengembalikan `int`) | Menghitung biaya tambahan pengiriman berdasarkan jarak ($\text{Rp}0$ jika jarak $\le 20\text{ km}$, dan $\text{Rp}5.000$ jika jarak $> 20\text{ km}$). |
| `hitung_potongan` | `ongkos_kotor`, `status_anggota` | **Ya** (*non-void*, mengembalikan `float` atau `int`) | Menghitung potongan diskon sebesar $10\%$ dari ongkos kirim kotor apabila pelanggan berstatus anggota (`"Ya"`), atau $0$ jika bukan anggota. |
| `cetak_struk` | `daftar_pesanan` | **Tidak** (*void*) | Melakukan iterasi pada daftar pesanan, memanggil fungsi perhitungan biaya dan potongan, mencetak baris rekap struk tiap pelanggan dalam bentuk tabel, serta menghitung dan menampilkan total pendapatan ongkos kirim hari ini. |
| `main` *(fungsi utama)* | Tidak ada | **Tidak** (*void*) | Menyimpan daftar data pesanan pelanggan hari ini dan memanggil fungsi `cetak_struk` untuk menjalankan alur utama program. |

### 3\. Perhitungan Manual dan Pembuktian Keluaran (Bagian c)

Berikut adalah perhitungan manual ongkos kirim akhir untuk pesanan **Sari**, **Tono**, dan **Umar**:

#### A. Perhitungan Manual Sari

* **Data Pesanan:** $\text{Berat} = 5\text{ kg}$, $\text{Jarak} = 25\text{ km}$, $\text{Anggota} = \text{Bukan}$

* **Biaya Berat:** Karena berat $5\text{ kg} > 2\text{ kg}$ (kelebihan $3\text{ kg}$):

  $$
  \text{Biaya Berat} = 10.000 + ((5 - 2) \times 4.000) = 10.000 + 12.000 = \text{Rp}22.000
  $$

* **Biaya Jarak:** Karena jarak $25\text{ km} > 20\text{ km}$, maka $\text{Biaya Jarak} = \text{Rp}5.000$.

* **Ongkos Kirim Kotor:** $22.000 + 5.000 = \text{Rp}27.000$.

* **Potongan:** Karena status `"Bukan"` anggota, maka $\text{Potongan} = \text{Rp}0$.

* **Ongkos Kirim Akhir:** $27.000 - 0 = \mathbf{\text{Rp}27.000}$.

#### B. Perhitungan Manual Tono

* **Data Pesanan:** $\text{Berat} = 5\text{ kg}$, $\text{Jarak} = 25\text{ km}$, $\text{Anggota} = \text{Ya}$

* **Biaya Berat:** $10.000 + ((5 - 2) \times 4.000) = \text{Rp}22.000$.

* **Biaya Jarak:** Karena jarak $25\text{ km} > 20\text{ km}$, maka $\text{Biaya Jarak} = \text{Rp}5.000$.

* **Ongkos Kirim Kotor:** $22.000 + 5.000 = \text{Rp}27.000$.

* **Potongan:** Karena status `"Ya"` (anggota), mendapat potongan $10\%$:

  $$
  \text{Potongan} = 10\% \times 27.000 = \text{Rp}2.700
  $$

* **Ongkos Kirim Akhir:** $27.000 - 2.700 = \mathbf{\text{Rp}24.300}$.

#### C. Perhitungan Manual Umar

* **Data Pesanan:** $\text{Berat} = 2\text{ kg}$, $\text{Jarak} = 30\text{ km}$, $\text{Anggota} = \text{Ya}$

* **Biaya Berat:** Karena berat $2\text{ kg} \le 2\text{ kg}$, maka $\text{Biaya Berat} = \text{Rp}10.000$.

* **Biaya Jarak:** Karena jarak $30\text{ km} > 20\text{ km}$, maka $\text{Biaya Jarak} = \text{Rp}5.000$.

* **Ongkos Kirim Kotor:** $10.000 + 5.000 = \text{Rp}15.000$.

* **Potongan:** Karena status `"Ya"` (anggota), mendapat potongan $10\%$:

  $$
  \text{Potongan} = 10\% \times 15.000 = \text{Rp}1.500
  $$

* **Ongkos Kirim Akhir:** $15.000 - 1.500 = \mathbf{\text{Rp}13.500}$.

#### D. Pembuktian dengan Keluaran Program

| Nama Pelanggan | Ongkir Akhir (Hitung Manual) | Ongkir Akhir (Keluaran `soal2.py`) | Keterangan |
| :---- | :---- | :---- | :---- |
| **Sari** | `Rp 27000` | `Rp 27000` | Sesuai |
| **Tono** | `Rp 24300` | `Rp 24300` | Sesuai |
| **Umar** | `Rp 13500` | `Rp 13500` | Sesuai |

### 4\. Analisis Perubahan Kebijakan Tarif Jarak (Bagian d)

Apabila toko mengubah kebijakan menjadi **batas jarak** $15\text{ km}$ dan **biaya tambahan jarak menjadi** $\text{Rp}7.000$, berikut adalah bagian kode yang terdampak serta evaluasi pengelompokannya:

1. **Bagian Kode yang Harus Diubah:** Perubahan **hanya perlu dilakukan pada satu tempat**, yaitu di dalam fungsi `hitung_biaya_jarak(jarak)`:

   * Mengubah kondisi batas jarak dari `if jarak <= 20:` menjadi `if jarak <= 15:`.

   * Mengubah nilai pengembalian biaya tambahan dari `return 5000` menjadi `return 7000`.

```
def hitung_biaya_jarak(jarak):
    """Fungsi untuk menghitung biaya tambahan berdasarkan jarak pengiriman."""
    if jarak <= 15:
        return 0
    else:
        return 7000

```

2. **Evaluasi Pengelompokan Kode:**

   * Pada program ini, satu perubahan aturan kebijakan jarak **tidak memerlukan perubahan di lebih dari satu tempat**. Hal ini disebabkan aturan perhitungan biaya jarak sudah diisolasi ke dalam satu fungsi khusus (`hitung_biaya_jarak`) dan tidak ditulis berulang di dalam fungsi `cetak_struk` maupun `main`.

   * Fungsi-fungsi lain (`hitung_biaya_berat`, `hitung_potongan`, `cetak_struk`, dan `main`) tetap dapat berjalan normal tanpa perlu dimodifikasi. Sebagai perbaikan tambahan agar nilai aturan lebih mudah dibaca dan dikelola di masa depan, angka kebijakan seperti batas jarak dan tarif jarak juga dapat didefinisikan sebagai konstanta di bagian atas program (misalnya `BATAS_JARAK = 15` dan `TARIF_JARAK = 7000`).