import streamlit as st

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
# FUNGSI-FUNGSI UTAMA KRIPTOGRAFI
# ==========================================

# 1. Caesar Cipher (Placeholder / To-Do)
def caesar_encrypt(text, shift):
    return f"[Caesar Encrypted: {text}]"

def caesar_decrypt(text, shift):
    return f"[Caesar Decrypted: {text}]"

# 2. Rail Fence Cipher (Placeholder / To-Do)
def rail_fence_encrypt(text, rails):
    return f"[RailFence Encrypted: {text}]"

def rail_fence_decrypt(ciphertext, rails):
    return f"[RailFence Decrypted: {ciphertext}]"

# 3. Cipher Aliran / Stream Cipher (Placeholder / To-Do)
def stream_cipher_process(text, key):
    return f"[StreamCipher Processed: {text}]"

# 4. Cipher Blok / Block Cipher (Oleh: Biyan)
def padding_teks(teks, ukuran_blok):
    sisa = len(teks) % ukuran_blok
    if sisa != 0:
        teks = teks + (' ' * (ukuran_blok - sisa))
    return teks

def block_cipher_encrypt(text, key, ukuran_blok):
    text_padded = padding_teks(text, ukuran_blok)
    hasil_ciphertext = ""
    shift = len(key) % 10 if key else 3

    for i in range(0, len(text_padded), ukuran_blok):
        blok = text_padded[i:i+ukuran_blok]
        blok_encrypted = "".join([chr(ord(c) + shift) for c in blok])
        hasil_ciphertext += blok_encrypted
        
    return hasil_ciphertext, shift

def block_cipher_decrypt(ciphertext, key, ukuran_blok):
    shift = len(key) % 10 if key else 3
    hasil_plaintext = ""

    for i in range(0, len(ciphertext), ukuran_blok):
        blok = ciphertext[i:i+ukuran_blok]
        blok_decrypted = "".join([chr(ord(c) - shift) for c in blok])
        hasil_plaintext += blok_decrypted
        
    return hasil_plaintext.rstrip(), shift


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
            <p><b>Cara Proses:</b> Setiap karakter dicari indeks abjadnya, lalu digeser ke kanan (enkripsi) atau ke kiri (dekripsi) sejumlah nilai shift.</p>
        </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.markdown("### 📝 Masukan Pengguna")
        teks_input = st.text_area("Teks Input:", placeholder="Masukkan teks di sini...", key="caesar_in")
        geseran = st.number_input("Jumlah Geseran (Shift):", min_value=1, max_value=25, value=3, key="caesar_shift")
        pilihan_aksi = st.radio("Pilih Aksi:", ["Enkripsi", "Dekripsi"], key="caesar_action")
        proses_btn = st.button("Proses Caesar Cipher", type="primary", use_container_width=True)

    with col2:
        st.markdown("### 📊 Hasil & Visualisasi")
        if proses_btn:
            # TODO: [ANIN] Masukkan logika enkripsi/dekripsi Caesar Cipher di sini
            st.info("Logika Caesar Cipher oleh Anin belum diimplementasikan.")


# ==========================================
# 2. MENU RAIL FENCE (To-Do: Andini)
# ==========================================
elif menu == "2. Rail Fence":
    
    # 1. Import khusus untuk modul Andini
    import time
    import pandas as pd

    # ==========================================
    # HELPER LOGIC RAIL FENCE 
    # ==========================================
    def encrypt_rail_fence(text, rails):
        if rails <= 1 or not text:
            return text, []
        matrix = [["." for _ in range(len(text))] for _ in range(rails)]
        row, direction = 0, 1
        for col, char in enumerate(text):
            matrix[row][col] = char
            if row == 0:
                direction = 1
            elif row == rails - 1:
                direction = -1
            row += direction
        ciphertext = "".join(
            ["".join([cell for cell in row if cell != "."]) for row in matrix]
        )
        return ciphertext, matrix

    def decrypt_rail_fence(ciphertext, rails):
        if rails <= 1 or not ciphertext:
            return ciphertext, []
        matrix = [["." for _ in range(len(ciphertext))] for _ in range(rails)]
        row, direction = 0, 1
        for col in range(len(ciphertext)):
            matrix[row][col] = "*"
            if row == 0:
                direction = 1
            elif row == rails - 1:
                direction = -1
            row += direction

        index = 0
        for r in range(rails):
            for c in range(len(ciphertext)):
                if matrix[r][c] == "*" and index < len(ciphertext):
                    matrix[r][c] = ciphertext[index]
                    index += 1

        plaintext = []
        row, direction = 0, 1
        for col in range(len(ciphertext)):
            plaintext.append(matrix[row][col])
            if row == 0:
                direction = 1
            elif row == rails - 1:
                direction = -1
            row += direction
        return "".join(plaintext), matrix

    # Kustomisasi warna matriks menggunakan CSS inline statis murni
    def highlight_zigzag(val):
        if val != ".":
            return "background-color: #2980b9; color: #ffffff; font-weight: bold; text-align: center; border: 1px solid #3498db;"
        return "color: #bdc3c7; text-align: center; border: 1px dashed #ecf0f1; background-color: #fafbfc;"

    # 2. Kustomisasi UI dengan CSS Murni & Statis
    st.markdown('''
    <style>
    .header-box {
        background-color: #2c3e50;
        padding: 20px;
        border-radius: 8px;
        color: #ffffff;
        text-align: center;
        margin-bottom: 25px;
        border-bottom: 5px solid #e74c3c;
    }
    .header-title {
        margin: 0;
        font-size: 32px;
        font-weight: 800;
        letter-spacing: 1px;
    }
    .header-subtitle {
        margin: 5px 0 0 0;
        font-size: 16px;
        color: #1abc9c;
    }
    .result-container {
        background-color: #ecf0f1;
        border-left: 6px solid #e74c3c;
        padding: 15px 20px;
        margin-top: 10px;
        margin-bottom: 20px;
        border-radius: 0px 8px 8px 0px;
    }
    .result-text {
        font-family: "Courier New", Courier, monospace;
        font-size: 24px;
        font-weight: bold;
        color: #2c3e50;
        letter-spacing: 3px;
        margin: 0;
    }
    </style>
    ''', unsafe_allow_html=True)

    # 3. Header Spektakuler
    st.markdown('''
    <div class="header-box">
        <h1 class="header-title">🎢 Algoritma Rail Fence</h1>
        <p class="header-subtitle">Modul Kriptografi Transposisi | Enginer: Andini</p>
    </div>
    ''', unsafe_allow_html=True)

    # 4. Interaksi Layout & Input
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        teks_input = st.text_input("Teks Pesan:", value="TEKNIK INFORMATIKA", help="Masukkan teks yang ingin diproses tanpa karakter spesial")
    with col2:
        jumlah_rail = st.number_input("Kedalaman Rail:", min_value=2, max_value=20, value=3)
    with col3:
        pilihan_aksi = st.selectbox("Operasi:", ["Enkripsi", "Dekripsi"])

    btn_proses = st.button("⚡ Eksekusi Algoritma", use_container_width=True)
    st.markdown("---")

    # 5. Logika Proses dengan Efek Animasi
    if btn_proses:
        teks_input = teks_input.upper().replace(" ", "")
        
        if not teks_input:
            st.error("⚠️ Input tidak valid! Masukkan huruf/angka.")
        else:
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
                status_text.text(f"Mengkalkulasi rute zigzag... {i+1}%")
            
            status_text.empty()
            progress_bar.empty()

            if pilihan_aksi == "Enkripsi":
                hasil, matriks = encrypt_rail_fence(teks_input, jumlah_rail)
                label_hasil = "Cipherteks (Teks Tersandi)"
            else:
                hasil, matriks = decrypt_rail_fence(teks_input, jumlah_rail)
                label_hasil = "Plainteks (Teks Asli)"

            # 6. Output Hasil Kustom
            st.success("✅ Operasi Kriptografi Berhasil Diselesaikan!")
            st.markdown(f"**{label_hasil}:**")
            st.markdown(f'''
            <div class="result-container">
                <p class="result-text">{hasil}</p>
            </div>
            ''', unsafe_allow_html=True)

            st.download_button(
                label="📥 Unduh Hasil txt",
                data=hasil,
                file_name=f"hasil_{pilihan_aksi.lower()}_railfence.txt",
                mime="text/plain"
            )

            # 7. Visualisasi Data Rapi dalam Expander
            with st.expander("👁️‍🗨️ Analisis Visual Matriks Transposisi", expanded=True):
                st.write(f"Distribusi **{len(teks_input)} karakter** pada matriks **{jumlah_rail} baris**:")
                
                df = pd.DataFrame(
                    matriks,
                    index=[f"Rail {i+1}" for i in range(jumlah_rail)],
                    columns=[f"P-{c+1}" for c in range(len(teks_input))]
                )
                
                st.dataframe(
                    df.style.map(highlight_zigzag),
                    use_container_width=True
                )
                
                if pilihan_aksi == "Enkripsi":
                    st.caption("🔍 **Insight Enkripsi:** Teks ditulis meliuk dari atas ke bawah, lalu dibaca mendatar dari Rail 1 hingga rail terakhir untuk membentuk Cipherteks.")
                else:
                    st.caption("🔍 **Insight Dekripsi:** Pola pagar kosong dibuat terlebih dahulu, lalu diisi oleh Cipherteks secara horizontal. Plainteks dikembalikan dengan membaca jalurnya secara meliuk.")

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
            <p><b>Cara Proses:</b> Dilakukan operasi transformasi byte/karakter (seperti XOR) antara teks dan kunci yang berulang mengikuti aliran data.</p>
        </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.markdown("### 📝 Masukan Pengguna")
        teks_input = st.text_area("Teks Input:", placeholder="Masukkan teks di sini...", key="stream_in")
        kunci = st.text_input("Masukkan Kunci (Key):", placeholder="Kata kunci rahasia...", key="stream_key")
        pilihan_aksi = st.radio("Pilih Aksi:", ["Enkripsi", "Dekripsi"], key="stream_action")
        proses_btn = st.button("Proses Cipher Aliran", type="primary", use_container_width=True)

    with col2:
        st.markdown("### 📊 Hasil & Visualisasi")
        if proses_btn:
            # TODO: [ALYA] Masukkan logika enkripsi/dekripsi Stream Cipher di sini
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
            <p><b>Kunci yang Dibutuhkan:</b> Kata Kunci (menentukan nilai geser *shift*) dan Ukuran Blok fleksibel (karakter per blok).</p>
            <p><b>Cara Proses:</b> Teks dipadded jika kurang, dipotong per blok, ditransformasikan karakternya berdasarkan kunci, lalu digabungkan kembali.</p>
        </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.markdown("### 📝 Masukan Pengguna")
        teks_input = st.text_area("Teks Input:", placeholder="Masukkan teks di sini...", key="teks_blok")
        kunci = st.text_input("Kunci Blok (Kata/Angka):", placeholder="Kunci rahasia...", key="kunci_blok")
        ukuran_blok = st.number_input("Pilih Ukuran Blok (Karakter):", min_value=2, max_value=10, value=4, key="ukuran_blok_input")
        pilihan_aksi = st.radio("Pilih Aksi:", ["Enkripsi", "Dekripsi"], key="aksi_blok")
        proses_btn = st.button("Jalankan Cipher Blok", type="primary", use_container_width=True)

    with col2:
        st.markdown("### 📊 Hasil & Visualisasi")
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
                        st.write(f"2. **Nilai Geser (Shift dari Kunci):** {shift_val}")
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
                        st.write(f"2. **Nilai Geser (Shift dari Kunci):** {shift_val}")
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
            <p><b>Fungsi:</b> Menggabungkan beberapa metode enkripsi secara berurutan (chained encryption) untuk meningkatkan keamanan.</p>
            <p><b>Konfigurasi:</b> Tentukan jumlah rantai kombinasi (2 s.d. 4 metode), urutan metodenya, serta parameter kunci pendukung di panel sebelah kiri.</p>
            <p><b>Cara Proses:</b> Output dari algoritma pertama akan langsung menjadi input untuk algoritma berikutnya sampai tahap akhir.</p>
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
