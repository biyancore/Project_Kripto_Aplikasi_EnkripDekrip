import streamlit as st

# Import fungsi dari folder Metode (pastikan nama folder dan file sesuai)
from Metode.blok_chiper import block_cipher_encrypt, block_cipher_decrypt, padding_teks

# Placeholder untuk fungsi teman kelompok (akan diisi nanti oleh Anin, Andini, Alya)
def caesar_encrypt(text, shift):
    return f"[Caesar Encrypted: {text}]"

def rail_fence_encrypt(text, rails):
    return f"[RailFence Encrypted: {text}]"

def stream_cipher_process(text, key):
    return f"[StreamCipher Processed: {text}]"


# Konfigurasi Halaman Utama
st.set_page_config(
    page_title="Aplikasi Kriptografi Kelompok",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling CSS untuk Mempercantik Tampilan UI
st.markdown("""
    <style>
    .main-header {
        font-size: 2.3rem;
        color: #1f77b4;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #666666;
        margin-bottom: 1.5rem;
    }
    .info-box {
        background-color: #f0f8ff;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #1f77b4;
        margin-bottom: 20px;
    }
    .stAlert {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR NAVIGATION & IDENTITAS
# ==========================================
st.sidebar.markdown("## 🧭 Navigasi Menu")
menu = st.sidebar.selectbox(
    "Pilih Menu Algoritma",
    [
        "1. Caesar Cipher",
        "2. Rail Fence",
        "3. Cipher Aliran",
        "4. Cipher Blok",
        "5. Super Enkripsi Fleksibel",
    ],
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 👥 Tim Pengembang:")
st.sidebar.markdown("""
- **Anin** (Caesar Cipher)
- **Andini** (Rail Fence)
- **Alya** (Cipher Aliran)
- **Biyan** (Briliant Priscilla - 123240068) (Cipher Blok & Integrasi)
""")


# ==========================================
# 1. MENU CAESAR CIPHER (To-Do: Anin)
# ==========================================
if menu == "1. Caesar Cipher":
    st.markdown('<p class="main-header">🔐 Menu 1: Caesar Cipher</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Algoritma Kriptografi Klasik - Substitusi Karakter</p>', unsafe_allow_html=True)
    st.markdown("*Dikerjakan oleh: Anin*")

    with st.container():
        st.markdown("""
        <div class="info-box">
            <h4>📖 Panduan & Konsep</h4>
            <p><b>Fungsi:</b> Menggeser setiap huruf dalam teks plaintext sejauh nilai tertentu dalam alfabet.</p>
            <p><b>Kunci yang Dibutuhkan:</b> Nilai pergeseran (<i>Shift</i> berupa angka).</p>
        </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")
    with col1:
        teks_input = st.text_input("Teks Input:", key="caesar_in")
        geseran = st.number_input("Jumlah Geseran (Shift):", min_value=1, max_value=25, value=3, key="caesar_shift")
        pilihan_aksi = st.radio("Pilih Aksi:", ["Enkripsi", "Dekripsi"], key="caesar_action")
        proses_btn = st.button("Proses Caesar Cipher", type="primary", use_container_width=True)

    with col2:
        if proses_btn:
            st.info("Logika Caesar Cipher oleh Anin belum diimplementasikan.")


# ==========================================
# 2. MENU RAIL FENCE (To-Do: Andini)
# ==========================================
elif menu == "2. Rail Fence":
    st.markdown('<p class="main-header">🚧 Menu 2: Rail Fence Cipher</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Algoritma Kriptografi Klasik - Transposisi Zig-Zag</p>', unsafe_allow_html=True)
    st.markdown("*Dikerjakan oleh: Andini*")

    with st.container():
        st.markdown("""
        <div class="info-box">
            <h4>📖 Panduan & Konsep</h4>
            <p><b>Fungsi:</b> Mengubah urutan karakter teks dengan menulisnya secara diagonal/zig-zag.</p>
            <p><b>Kunci yang Dibutuhkan:</b> Jumlah rail (baris).</p>
        </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")
    with col1:
        teks_input = st.text_input("Teks Input:", key="rail_in")
        jumlah_rail = st.number_input("Jumlah Rail (Baris):", min_value=2, max_value=5, value=3, key="rail_num")
        pilihan_aksi = st.radio("Pilih Aksi:", ["Enkripsi", "Dekripsi"], key="rail_action")
        proses_btn = st.button("Proses Rail Fence", type="primary", use_container_width=True)

    with col2:
        if proses_btn:
            st.info("Logika Rail Fence oleh Andini belum diimplementasikan.")


# ==========================================
# 3. MENU CIPHER ALIRAN (To-Do: Alya)
# ==========================================
elif menu == "3. Cipher Aliran":
    st.markdown('<p class="main-header">🌊 Menu 3: Cipher Aliran (Stream Cipher)</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Algoritma Kriptografi Modern - Enkripsi Bit/Karakter Berbasis Kunci</p>', unsafe_allow_html=True)
    st.markdown("*Dikerjakan oleh: Alya*")

    with st.container():
        st.markdown("""
        <div class="info-box">
            <h4>📖 Panduan & Konsep</h4>
            <p><b>Fungsi:</b> Mengenkripsi plaintext dengan menggabungkan karakter teks dan kunci secara berurutan.</p>
            <p><b>Kunci yang Dibutuhkan:</b> Kata kunci (*Key*).</p>
        </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")
    with col1:
        teks_input = st.text_input("Teks Input:", key="stream_in")
        kunci = st.text_input("Masukkan Kunci (Key):", key="stream_key")
        pilihan_aksi = st.radio("Pilih Aksi:", ["Enkripsi", "Dekripsi"], key="stream_action")
        proses_btn = st.button("Proses Cipher Aliran", type="primary", use_container_width=True)

    with col2:
        if proses_btn:
            st.info("Logika Cipher Aliran oleh Alya belum diimplementasikan.")


# ==========================================
# 4. MENU CIPHER BLOK (Biyan)
# ==========================================
elif menu == "4. Cipher Blok":
    st.markdown('<p class="main-header">📦 Menu 4: Cipher Blok (Block Cipher)</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Algoritma Kriptografi Modern - Transformasi Blok dengan Padding Fleksibel</p>', unsafe_allow_html=True)
    st.markdown("*Dikerjakan oleh: Briliant Priscilla - 123240068*")

    with st.container():
        st.markdown("""
        <div class="info-box">
            <h4>📖 Panduan & Konsep</h4>
            <p><b>Fungsi:</b> Memecah teks menjadi beberapa blok ukuran tetap, lalu mengenkripsi setiap blok secara bersamaan.</p>
            <p><b>Kunci yang Dibutuhkan:</b> Kata Kunci dan Ukuran Blok fleksibel.</p>
        </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")
    with col1:
        teks_input = st.text_area("Teks Input:", placeholder="Masukkan teks di sini...", key="teks_blok")
        kunci = st.text_input("Kunci Blok (Kata/Angka):", placeholder="Kunci rahasia...", key="kunci_blok")
        ukuran_blok = st.number_input("Pilih Ukuran Blok (Karakter):", min_value=2, max_value=10, value=4, key="ukuran_blok_input")
        pilihan_aksi = st.radio("Pilih Aksi:", ["Enkripsi", "Dekripsi"], key="aksi_blok")
        proses_btn = st.button("Jalankan Cipher Blok", type="primary", use_container_width=True)

    with col2:
        if proses_btn:
            if not teks_input or not kunci:
                st.warning("Mohon masukkan teks dan kunci terlebih dahulu!")
            else:
                if pilihan_aksi == "Enkripsi":
                    hasil_akhir, shift_val = block_cipher_encrypt(teks_input, kunci, int(ukuran_blok))
                    st.success("Enkripsi Blok Berhasil!")
                    st.markdown(f"**Hasil Ciphertext:**")
                    st.code(hasil_akhir)
                    
                    with st.expander("🔍 Lihat Proses Langkah demi Langkah (Enkripsi)"):
                        text_padded = padding_teks(teks_input, int(ukuran_blok))
                        st.write(f"1. **Ukuran Blok:** {ukuran_blok} karakter")
                        st.write(f"2. **Nilai Geser (Shift):** {shift_val}")
                        st.write("3. **Transformasi per Blok:**")
                        for i in range(0, len(text_padded), int(ukuran_blok)):
                            b = text_padded[i:i+int(ukuran_blok)]
                            encrypted_b = "".join([chr(ord(c) + shift_val) for c in b])
                            st.code(f"Blok '{b}'  -->  '{encrypted_b}'")
                else:
                    hasil_akhir, shift_val = block_cipher_decrypt(teks_input, kunci, int(ukuran_blok))
                    st.success("Dekripsi Blok Berhasil!")
                    st.markdown(f"**Hasil Plaintext:**")
                    st.code(hasil_akhir)
                    
                    with st.expander("🔍 Lihat Proses Langkah demi Langkah (Dekripsi)"):
                        st.write(f"1. **Ukuran Blok:** {ukuran_blok} karakter")
                        st.write(f"2. **Nilai Geser (Shift):** {shift_val}")
                        st.write("3. **Pemulihan per Blok:**")
                        for i in range(0, len(teks_input), int(ukuran_blok)):
                            b = teks_input[i:i+int(ukuran_blok)]
                            decrypted_b = "".join([chr(ord(c) - shift_val) for c in b])
                            st.code(f"Blok '{b}'  -->  '{decrypted_b}'")


# ==========================================
# 5. MENU SUPER ENKRIPSI FLEKSIBEL (Integrasi)
# ==========================================
elif menu == "5. Super Enkripsi Fleksibel":
    st.markdown('<p class="main-header">⚡ Menu 5: Super Enkripsi Fleksibel</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Rantai Kombinasi Berurutan dari Berbagai Metode Kriptografi</p>', unsafe_allow_html=True)
    st.markdown("*Dikerjakan bersama (Integrasi Kelompok)*")

    with st.container():
        st.markdown("""
        <div class="info-box">
            <h4>📖 Panduan & Konsep Super Enkripsi</h4>
            <p><b>Fungsi:</b> Menggabungkan beberapa metode enkripsi secara berurutan (chained encryption).</p>
        </div>
        """, unsafe_allow_html=True)

    jumlah_kombinasi = st.slider("Pilih jumlah metode yang dikombinasikan dalam rantai:", min_value=2, max_value=4, value=3)
    
    pilihan_metode = []
    opsi_tersedia = ["Caesar Cipher", "Rail Fence", "Cipher Aliran", "Cipher Blok"]
    
    col_config, col_main = st.columns([1, 1], gap="medium")
    
    with col_config:
        st.markdown("### ⚙️ Pengaturan Rantai Metode")
        for i in range(jumlah_kombinasi):
            pilih = st.selectbox(f"Urutan Algoritma ke-{i+1}:", opsi_tersedia, key=f"super_{i}")
            pilihan_metode.append(pilih)
            
        st.markdown("---")
        st.markdown("### 🔑 Parameter Pendukung")
        teks_super = st.text_area("Teks Awal (Plaintext):", placeholder="Teks yang akan di-super enkripsi...", key="text_super_in")
        kunci_super = st.text_input("Kunci Universal (Stream/Blok):", value="kunci123", key="key_super_in")
        geser_super = st.number_input("Nilai Caesar Shift:", value=3, key="shift_super_in")
        rail_super = st.number_input("Jumlah Rail Fence:", value=3, key="rail_super_in")
        blok_super = st.number_input("Ukuran Blok:", value=4, key="blok_super_in")
        
        jalankan_btn = st.button("Jalankan Super Enkripsi Berantai", type="primary", use_container_width=True)

    with col_main:
        st.markdown("### 🔄 Alur & Hasil Rantai Enkripsi")
        if jalankan_btn:
            if not teks_super:
                st.warning("Mohon masukkan teks awal terlebih dahulu!")
            else:
                current_text = teks_super
                
                for idx, metode in enumerate(pilihan_metode):
                    if metode == "Caesar Cipher":
                        current_text = caesar_encrypt(current_text, int(geser_super))
                    elif metode == "Rail Fence":
                        current_text = rail_fence_encrypt(current_text, int(rail_super))
                    elif metode == "Cipher Aliran":
                        current_text = stream_cipher_process(current_text, kunci_super)
                    elif metode == "Cipher Blok":
                        current_text, _ = block_cipher_encrypt(current_text, kunci_super, int(blok_super))
                        
                    with st.expander(f"Tahap {idx+1}: {metode}", expanded=True):
                        st.write(f"Hasil sementara setelah melalui **{metode}**:")
                        st.code(current_text)
                        
                st.success("Super Enkripsi Selesai Dilakukan!")
                st.markdown(f"**Ciphertext Akhir (Super Enkripsi):**")
                st.code(current_text)