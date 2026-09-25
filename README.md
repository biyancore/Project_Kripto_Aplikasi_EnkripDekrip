# 🔐 Aplikasi Kriptografi Interaktif

Aplikasi berbasis web interaktif ini dibangun menggunakan **Python** dan **Streamlit**. Aplikasi ini dirancang untuk mendemonstrasikan berbagai algoritma kriptografi, baik klasik maupun modern, lengkap dengan visualisasi proses enkripsi/dekripsinya secara detail langkah demi langkah.

## ✨ Fitur Utama

Aplikasi ini mencakup 4 algoritma kriptografi utama dan 1 fitur kombinasi:

1. **Caesar Cipher** (Kriptografi Klasik - Substitusi)
   * Menggeser huruf pada teks berdasarkan nilai *shift* (1-25).
   * Menampilkan tabel visual *mapping* pergeseran alfabet.
2. **Rail Fence Cipher** (Kriptografi Klasik - Transposisi)
   * Mengubah posisi karakter menggunakan pola zig-zag (*rail*).
   * Dilengkapi tabel matriks visual untuk melihat alur penempatan teks.
3. **Stream Cipher** (Operasi XOR Bit-level)
   * Melakukan enkripsi/dekripsi dengan operasi logika XOR antara plainteks dan *keystream* (angka acak semu/pseudo-random).
   * Menampilkan jejak proses konversi biner dan operasi XOR per karakter.
4. **Block Cipher** (Enkripsi Berbasis Blok)
   * Memproses data dalam bentuk blok *bytes* dengan standar **PKCS#7 Padding**.
   * Menghasilkan teks rahasia dalam format **Heksadesimal (Hex)** agar rapi.
   * Menampilkan rincian transformasi teks ke biner/heksadesimal di setiap blok.
5. **Super Enkripsi Fleksibel** (Rantai Algoritma)
   * Fitur khusus untuk merantai 2 hingga 4 algoritma yang dipilih pengguna.
   * Output dari satu algoritma akan otomatis menjadi input untuk algoritma selanjutnya.

## 🛠️ Prasyarat & Instalasi

Pastikan komputer Anda sudah terinstal Python (versi 3.8 ke atas direkomendasikan).

1. Buka terminal atau *command prompt*.
2. *Clone* atau unduh repositori proyek ini.
3. Instal pustaka yang dibutuhkan menggunakan *pip*:
   ```bash
   pip install streamlit pandas
   ```

## 🚀 Cara Menjalankan Aplikasi

1. Buka terminal dan arahkan ke direktori tempat proyek ini disimpan.
2. Jalankan perintah Streamlit berikut (sesuaikan dengan nama file utama Anda, misalnya `app_2.py` atau `app.py`):
   ```bash
   streamlit run app_2.py
   ```
3. Aplikasi akan otomatis terbuka di *browser* default Anda pada `http://localhost:8501`.

## 📁 Struktur Direktori

```text
📁 Proyek-Kriptografi/
├── 📄 app_2.py                 # File utama antarmuka Streamlit
├── 📄 README.md                # Dokumentasi proyek
└── 📁 Metode/                  # Modul berisi logika algoritma inti
    ├── 📄 caesar.py            # Modul Caesar Cipher
    ├── 📄 rail_fence.py        # Modul Rail Fence Cipher
    ├── 📄 stream_chiper.py     # Modul Stream Cipher
    └── 📄 blok_chiper.py       # Modul Block Cipher
```

## 👥 Tim Pengembang

Proyek ini dikerjakan secara kolaboratif oleh tim kami:

* **Anindya Bintarti** (123240197) — *Pengembang Modul Caesar Cipher*
* **Andini Papa Sulima** (123240118) — *Pengembang Modul Rail Fence Cipher*
* **Alya Choirunnisa** (123240213) — *Pengembang Modul Stream Cipher*
* **Briliant Priscilla** (123240068) — *Pengembang Modul Block Cipher & Sistem Hex*
* **Integrasi Kelompok** — *Pengembangan UI Streamlit dan Logika Super Enkripsi*

---