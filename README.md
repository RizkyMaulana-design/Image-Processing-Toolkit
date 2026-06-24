# Aplikasi Pengolahan Citra Digital (GUI)

> **UAS Mata Kuliah Pengolahan Citra Digital**
> Dosen Pengampu: Dr. Muhamad Fatchan, S.Kom., M.Kom.

Aplikasi desktop berbasis antarmuka grafis (GUI) untuk melakukan pemrosesan dan analisis citra digital secara interaktif. Dikembangkan menggunakan Python, OpenCV, dan Tkinter dengan mengusung antarmuka *Dark Mode* yang modern dan elegan.

## Identitas Pengembang
* **Nama**: Rizky Maulana
* **NIM**: 312410430
* **Kelas**: I241C
* **Program Studi**: Teknik Informatika

---

## Fitur Utama

Aplikasi ini mencakup implementasi 5 algoritma pemrosesan citra dasar beserta fitur manajemen berkas pendukung:

1. **RGB to Grayscale**: Konversi citra berwarna menjadi saluran tunggal derajat keabuan untuk mereduksi dimensi komputasi.
2. **Histogram Equalization**: Perbaikan kualitas citra spasial untuk meratakan distribusi intensitas piksel dan meningkatkan kontras.
3. **Gaussian Filter**: Teknik *smoothing* (low-pass filter) menggunakan matriks kernel (15, 15) untuk mereduksi *noise* berfrekuensi tinggi.
4. **Canny Edge Detection**: Deteksi tepi objek secara presisi dengan penekanan *noise* menggunakan metode kalkulus multi-tahap (threshold: 100-200).
5. **Thresholding**: Segmentasi citra biner (nilai ambang 127) untuk memisahkan objek utama (*foreground*) dari latar belakang (*background*).
6. **Save Image**: Fitur otomatisasi penyimpanan citra hasil pemrosesan dengan rekomendasi penamaan *file* yang terstruktur.

## Teknologi yang Digunakan
* **Bahasa Pemrograman**: Python 3.x
* **Computer Vision**: OpenCV (`cv2`)
* **Komputasi Matriks**: NumPy
* **GUI Framework**: Tkinter
* **Image Handling**: Pillow (PIL)

---

## Struktur Direktori

```text
📁 UAS-PengolahanCitra
│
├── 📁 dataset                  # Kumpulan 20 citra digital asli (.jpg)
├── 📁 hasil_proses             # Direktori penyimpanan hasil pemrosesan
│   ├── 📁 1_Grayscale
│   ├── 📁 2_Histogram_Eq
│   ├── 📁 3_Gaussian
│   ├── 📁 4_Canny_Edge
│   └── 📁 5_Thresholding
│
├── 📄 main.py                  # Source code utama aplikasi
├── 📄 README.md                # Dokumentasi repository
├── 📄 Laporan_UAS_Rizky.pdf    # Dokumen Laporan Project
└── 📄 Presentasi_UAS_Rizky.pdf # Dokumen Slide Presentasi

```

---

## Cara Instalasi dan Penggunaan

**1. Clone Repository**

```bash
git clone [https://github.com/RizkyMaulana-design/UAS-PengolahanCitra.git](https://github.com/RizkyMaulana-design/UAS-PengolahanCitra.git)
cd UAS-PengolahanCitra

```

**2. Instalasi Dependencies**
Pastikan Python sudah terinstal di sistem Anda. Jalankan perintah berikut di terminal untuk memasang pustaka yang dibutuhkan:

```bash
pip install opencv-python numpy pillow

```

**3. Menjalankan Aplikasi**
Eksekusi *file* utama untuk membuka antarmuka aplikasi:

```bash
python main.py

```

**4. Panduan Penggunaan**

* Klik tombol **1. Load Image** dan pilih salah satu gambar dari folder `dataset`.
* Klik salah satu dari 5 tombol proses yang tersedia (misal: *Gaussian Filter*). Area gambar di sebelah kanan akan menampilkan pratinjau hasil secara *real-time*.
* Klik **Simpan Gambar Hasil** untuk menyimpan citra ke dalam folder `hasil_proses` yang sesuai.
* Klik **Reset to Original** untuk mengembalikan citra ke kondisi awal sebelum diberi *filter*.

---

### Hak Cipta & Lisensi

Proyek ini dikembangkan secara spesifik untuk memenuhi persyaratan Ujian Akhir Semester Mata Kuliah Pengolahan Citra Digital Tahun Ajaran 2025/2026.

```

```
