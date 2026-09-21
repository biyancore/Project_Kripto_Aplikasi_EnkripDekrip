import streamlit as st

st.set_page_config(page_title="Aplikasi Kriptografi Kelompok", layout="wide")

# Sidebar untuk Navigasi Menu
menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "1. Caesar Cipher",
        "2. Rail Fence",
        "3. Cipher Aliran",
        "4. Cipher Blok",
        "5. Super Enkripsi Fleksibel",
    ],
)


# ==========================================
# MENU 1: CAESAR CIPHER (Tugas: Anin)
# ==========================================
if menu == "1. Caesar Cipher":
    st.header("Menu 1: Caesar Cipher")
    st.markdown("*Dikerjakan oleh: Anin*")

    teks_input = st.text_input("Masukkan teks:")
    geseran = st.number_input("Jumlah Geseran (Shift):", min_value=1, max_value=25, value=3)
    pilihan_aksi = st.radio("Aksi:", ["Enkripsi", "Dekripsi"])

    if st.button("Proses Caesar"):
        # TODO: [ANIN] Masukkan logika enkripsi/dekripsi Caesar Cipher di sini
        # TODO: [ANIN] Tampilkan visualisasi proses langkah demi langkah (gunakan st.expander)
        st.info("Logika Caesar Cipher oleh Anin belum diimplementasikan.")


# ==========================================
# MENU 2: RAIL FENCE (Tugas: Andini)
# ==========================================
elif menu == "2. Rail Fence":
    st.header("Menu 2: Rail Fence Cipher")
    st.markdown("*Dikerjakan oleh: Andini*")

    teks_input = st.text_input("Masukkan teks:")
    jumlah_rail = st.number_input("Jumlah Rail:", min_value=2, max_value=5, value=3)
    pilihan_aksi = st.radio("Aksi:", ["Enkripsi", "Dekripsi"])

    if st.button("Proses Rail Fence"):
        # TODO: [ANDINI] Masukkan logika enkripsi/dekripsi Rail Fence di sini
        # TODO: [ANDINI] Tampilkan visualisasi bentuk zigzag/matriks prosesnya
        st.info("Logika Rail Fence oleh Andini belum diimplementasikan.")


# ==========================================
# MENU 3: CIPHER ALIRAN (Tugas: Alya)
# ==========================================
elif menu == "3. Cipher Aliran":
    st.header("Menu 3: Cipher Aliran (Stream Cipher)")
    st.markdown("*Dikerjakan oleh: Alya*")

    teks_input = st.text_input("Masukkan teks:")
    kunci = st.text_input("Masukkan Kunci:")
    pilihan_aksi = st.radio("Aksi:", ["Enkripsi", "Dekripsi"])

    if st.button("Proses Cipher Aliran"):
        # TODO: [ALYA] Masukkan logika enkripsi/dekripsi Stream Cipher di sini
        # TODO: [ALYA] Tampilkan tahapan perubahan biner atau proses XOR di st.expander
        st.info("Logika Cipher Aliran oleh Alya belum diimplementasikan.")


# ==========================================
# MENU 4: CIPHER BLOK (Tugas: Biyan)
# ==========================================
elif menu == "4. Cipher Blok":
    st.header("Menu 4: Cipher Blok (Block Cipher)")
    st.markdown("*Dikerjakan oleh: Biyan*")

    teks_input = st.text_input("Masukkan teks:")
    kunci = st.text_input("Masukkan Kunci Blok:")
    pilihan_aksi = st.radio("Aksi:", ["Enkripsi", "Dekripsi"])

    if st.button("Proses Cipher Blok"):
        # TODO: [BIYAN] Masukkan logika enkripsi/dekripsi Block Cipher di sini
        # TODO: [BIYAN] Tampilkan proses pembagian blok teksnya
        st.info("Logika Cipher Blok oleh Biyan belum diimplementasikan.")


# ==========================================
# MENU 5: SUPER ENKRIPSI FLEKSIBEL (Integrasi)
# ==========================================
elif menu == "5. Super Enkripsi Fleksibel":
    st.header("Menu 5: Super Enkripsi Fleksibel")
    st.markdown("*Dikerjakan bersama (Integrasi)*")

    jumlah_kombinasi = st.slider("Pilih jumlah metode yang dikombinasikan:", 2, 4, 3)
    
    pilihan_metode = []
    opsi_tersedia = ["Caesar", "Rail Fence", "Cipher Aliran", "Cipher Blok"]
    
    for i in range(jumlah_kombinasi):
        pilih = st.selectbox(f"Urutan ke-{i+1}:", opsi_tersedia, key=f"super_{i}")
        pilihan_metode.append(pilih)

    teks_super = st.text_area("Masukkan teks untuk Super Enkripsi:")

    if st.button("Jalankan Super Enkripsi"):
        # TODO: [BIYAN & TIM] Hubungkan fungsi dari Menu 1, 2, 3, dan 4 secara berurutan di sini!
        st.info("Logika Super Enkripsi berantai belum diimplementasikan.")