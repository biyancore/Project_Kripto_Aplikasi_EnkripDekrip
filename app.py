import streamlit as st
import pandas as pd

# ============================================================
# IMPORT METODE DARI FOLDER Metode
# ============================================================
from Metode.caesar import (
    encrypt_caesar,
    decrypt_caesar,
    get_caesar_mapping,
)

from Metode.rail_fence import (
    encrypt_rail_fence,
    decrypt_rail_fence,
    highlight_zigzag,
)

from Metode.stream_chiper import (
    stream_cipher_process,
    stream_cipher_encrypt,
    stream_cipher_decrypt,
)

from Metode.blok_chiper import (
    block_cipher_encrypt,
    block_cipher_decrypt,
)


# ============================================================
# KONFIGURASI HALAMAN
# ============================================================
st.set_page_config(
    page_title="Aplikasi Kriptografi Kelompok",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CSS
# ============================================================
st.markdown(
    """
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

    .result-container {
        background-color: #ecf0f1;
        border-left: 6px solid #1f77b4;
        padding: 15px 20px;
        margin-top: 10px;
        margin-bottom: 20px;
        border-radius: 0 8px 8px 0;
    }

    .result-text {
        font-family: "Courier New", Courier, monospace;
        font-size: 20px;
        font-weight: bold;
        color: #2c3e50;
        letter-spacing: 1px;
        margin: 0;
        white-space: pre-wrap;
        word-break: break-word;
    }

    .stAlert {
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================
st.sidebar.markdown("## 🧭 Navigasi Menu")

menu = st.sidebar.selectbox(
    "Pilih Menu Algoritma",
    [
        "1. Caesar Cipher",
        "2. Rail Fence",
        "3. Stream Cipher",
        "4. Block Cipher",
        "5. Super Enkripsi Fleksibel",
    ],
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 👥 Tim Pengembang:")
st.sidebar.markdown(
    """
    - **Anindya Bintarti - 123240197** — Caesar Cipher
    - **Andini Papa Sulima - 123240118** — Rail Fence
    - **Alya Choirunnisa - 123240213** — Stream Cipher
    - **Briliant Priscilla - 123240068** — Block Cipher
    """
)


# ============================================================
# MENU 1 — CAESAR CIPHER
# ============================================================
if menu == "1. Caesar Cipher":
    st.markdown(
        '<p class="main-header">🔐 Menu 1: Caesar Cipher</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="sub-header">Algoritma Kriptografi Klasik - Substitusi Karakter</p>',
        unsafe_allow_html=True,
    )
    st.markdown("*Dikerjakan oleh: Anindya Bintarti - 123240197*")

    st.markdown(
        """
        <div class="info-box">
            <h4>📖 Panduan & Konsep</h4>
            <p><b>Fungsi:</b> Menggeser setiap huruf dalam teks berdasarkan nilai shift.</p>
            <p><b>Kunci:</b> Nilai pergeseran berupa angka 1-25.</p>
            <p>Huruf besar dan kecil dipertahankan. Spasi, angka, dan simbol tidak berubah.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        teks_input = st.text_area(
            "Teks Input:",
            placeholder="Masukkan plaintext atau ciphertext...",
            key="caesar_in",
        )
        geseran = st.number_input(
            "Jumlah Geseran (Shift):",
            min_value=1,
            max_value=25,
            value=3,
            key="caesar_shift",
        )
        pilihan_aksi = st.radio(
            "Pilih Aksi:",
            ["Enkripsi", "Dekripsi"],
            key="caesar_action",
            horizontal=True,
        )
        proses_btn = st.button(
            "🔐 Proses Caesar Cipher",
            type="primary",
            use_container_width=True,
        )

    with col2:
        if proses_btn:
            if not teks_input:
                st.warning("Mohon masukkan teks terlebih dahulu.")
            else:
                if pilihan_aksi == "Enkripsi":
                    hasil = encrypt_caesar(teks_input, int(geseran))
                else:
                    hasil = decrypt_caesar(teks_input, int(geseran))

                st.success(f"{pilihan_aksi} berhasil!")
                st.markdown("**Hasil:**")
                st.code(hasil)

                st.download_button(
                    "📥 Unduh Hasil",
                    data=hasil,
                    file_name=f"hasil_caesar_{pilihan_aksi.lower()}.txt",
                    mime="text/plain",
                    use_container_width=True,
                )

                with st.expander("🔍 Lihat Mapping Per Karakter"):
                    mapping = get_caesar_mapping(
                        teks_input,
                        int(geseran),
                        pilihan_aksi,
                    )
                    st.dataframe(
                        pd.DataFrame(mapping),
                        use_container_width=True,
                        hide_index=True,
                    )

                    st.markdown("### 📚 Penjelasan Alfabet Caesar")

                    st.markdown(
                        f"""
                        <div class="info-box">
                            <p>
                                <b>Karakter Hasil</b> adalah huruf yang diperoleh setelah
                                setiap huruf pada alfabet digeser sebanyak
                                <b>{int(geseran)} posisi</b>.
                            </p>
                            <p>
                                A = <b>{encrypt_caesar("A", int(geseran))}</b>.
                            </p>
                            <p>
                                Jika proses pergeseran melewati huruf Z, maka alfabet
                                akan kembali ke huruf A.
                            </p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    # Membuat alfabet asli
                    alfabet_asli = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

                    # Membuat alfabet hasil berdasarkan shift
                    if pilihan_aksi == "Enkripsi":
                        alfabet_hasil = encrypt_caesar(
                            alfabet_asli,
                            int(geseran)
                        )
                    else:
                        alfabet_hasil = decrypt_caesar(
                            alfabet_asli,
                            int(geseran)
                        )

                    st.markdown("#### 🔤 Blok Alfabet")
                    list_asli = list(alfabet_asli)
                    list_hasil = list(alfabet_hasil)

                    # Membuat DataFrame agar berbentuk tabel kotak-kotak yang rapi
                    df_alfabet = pd.DataFrame(
                        [list_asli, list_hasil],
                        index=["Alfabet Asli", "Alfabet Hasil"]
                    )

                    # Menampilkan tabel interaktif yang rapi di Streamlit
                    st.dataframe(df_alfabet, use_container_width=True)


# ============================================================
# MENU 2 — RAIL FENCE
# ============================================================
elif menu == "2. Rail Fence":
    st.markdown(
        '<p class="main-header">🎢 Menu 2: Rail Fence Cipher</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="sub-header">Algoritma Kriptografi Transposisi dengan pola zig-zag</p>',
        unsafe_allow_html=True,
    )
    st.markdown("*Dikerjakan oleh: Andini Papa Sulima - 123240118*")

    st.markdown(
        """
        <div class="info-box">
            <h4>📖 Panduan & Konsep</h4>
            <p>Teks ditulis mengikuti pola zig-zag pada sejumlah rail, kemudian dibaca per baris.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        teks_input = st.text_area(
            "Teks Pesan:",
            placeholder="Masukkan teks yang ingin diproses...",
            key="rail_in",
        )

    with col2:
        jumlah_rail = st.number_input(
            "Kedalaman Rail:",
            min_value=2,
            max_value=20,
            value=3,
            step=1,
            key="rail_count",
        )

    with col3:
        pilihan_aksi = st.selectbox(
            "Operasi:",
            ["Enkripsi", "Dekripsi"],
            key="rail_action",
        )

    btn_proses = st.button(
        "⚡ Eksekusi Algoritma",
        type="primary",
        use_container_width=True,
    )

    if btn_proses:
        if not teks_input:
            st.error("Masukkan teks terlebih dahulu.")
        elif jumlah_rail >= len(teks_input):
            st.warning(
                "Jumlah rail sebaiknya lebih kecil dari jumlah karakter teks."
            )
        else:
            if pilihan_aksi == "Enkripsi":
                hasil, matriks = encrypt_rail_fence(
                    teks_input,
                    int(jumlah_rail),
                )
                label_hasil = "Cipherteks"
            else:
                hasil, matriks = decrypt_rail_fence(
                    teks_input,
                    int(jumlah_rail),
                )
                label_hasil = "Plainteks"

            st.success("✅ Operasi berhasil!")
            st.markdown(f"**{label_hasil}:**")
            
            # Menggunakan st.code agar muncul ikon copy di pojok kanan atas
            st.code(hasil, language="plaintext")

            st.download_button(
                label="📥 Unduh Hasil TXT",
                data=hasil,
                file_name=f"hasil_{pilihan_aksi.lower()}_railfence.txt",
                mime="text/plain",
            )

            with st.expander(
                "👁️‍🗨️ Analisis Visual Matriks Transposisi",
                expanded=True,
            ):
                df = pd.DataFrame(
                    matriks,
                    index=[f"Rail {i + 1}" for i in range(int(jumlah_rail))],
                    columns=[
                        f"P-{i + 1}" for i in range(len(teks_input))
                    ],
                )

                styler = df.style
                style_func = (
                    styler.map
                    if hasattr(styler, "map")
                    else styler.applymap
                )

                st.dataframe(
                    style_func(highlight_zigzag),
                    use_container_width=True,
                )

                if pilihan_aksi == "Enkripsi":
                    st.caption(
                        "🔍 Teks ditulis meliuk dari atas ke bawah, "
                        "kemudian dibaca mendatar dari rail pertama hingga terakhir."
                    )
                else:
                    st.caption(
                        "🔍 Pola zig-zag dibuat terlebih dahulu, kemudian "
                        "cipherteks ditempatkan pada posisi yang sesuai."
                    )

# ============================================================
# MENU 3 — Stream Cipher
# ============================================================
elif menu == "3. Stream Cipher":
    st.markdown(
        '<p class="main-header">🌊 Menu 3: Stream Cipher (Stream Cipher)</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="sub-header">Enkripsi/dekripsi karakter menggunakan XOR dan keystream pseudo-random</p>',
        unsafe_allow_html=True,
    )
    st.markdown("*Dikerjakan oleh: Alya Choirunnisa - 123240213*")

    st.markdown(
        """
        <div class="info-box">
            <h4>📖 Panduan & Konsep</h4>
            <p>Modul menggunakan <b>random.seed(key)</b> untuk menghasilkan keystream
            yang sama ketika kunci yang sama digunakan.</p>
            <p>Enkripsi dan dekripsi menggunakan fungsi yang sama karena operasi XOR
            dapat dibalik menggunakan keystream yang sama.</p>
            <p><b>Kunci:</b> Angka.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        teks_input = st.text_area(
            "Teks Input:",
            placeholder="Masukkan plaintext atau ciphertext...",
            key="stream_in",
        )

        kunci_stream = st.number_input(
            "Masukkan Kunci (Key):",
            min_value=0,
            value=123,
            step=1,
            key="stream_key",
        )

        pilihan_aksi = st.radio(
            "Pilih Aksi:",
            ["Enkripsi", "Dekripsi"],
            key="stream_action",
            horizontal=True,
        )

        proses_btn = st.button(
            "🌊 Proses Stream Cipher",
            type="primary",
            use_container_width=True,
        )

    with col2:
        if proses_btn:
            if not teks_input:
                st.warning("Mohon masukkan teks terlebih dahulu.")
            else:
                if pilihan_aksi == "Enkripsi":
                    hasil, teks_langkah = stream_cipher_encrypt(teks_input, int(kunci_stream))
                else:
                    hasil, teks_langkah = stream_cipher_decrypt(teks_input, int(kunci_stream))

                st.success(f"{pilihan_aksi} berhasil!")
                st.markdown("**Hasil:**")
                st.code(hasil)

                with st.expander("🔍 Lihat Detail Proses XOR"):
                    st.code(teks_langkah)

                st.download_button(
                    "📥 Unduh Hasil",
                    data=hasil,
                    file_name=f"hasil_stream_{pilihan_aksi.lower()}.txt",
                    mime="text/plain",
                    use_container_width=True,
                )


# ============================================================
# MENU 4 — BLOCK CIPHER
# ============================================================
elif menu == "4. Block Cipher":
    st.markdown(
        '<p class="main-header">📦 Menu 4: Block Cipher (Block Cipher)</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="sub-header">Enkripsi level bit menggunakan operasi XOR dan standar padding PKCS#7</p>',
        unsafe_allow_html=True,
    )
    st.markdown("*Dikerjakan oleh: Briliant Priscilla - 123240068*")

    st.markdown(
        """
        <div class="info-box">
            <h4>📖 Panduan & Konsep</h4>
            <p>Teks diubah ke dalam bentuk bit (bytes). Jika kurang dari ukuran blok, sistem menambahkan PKCS#7 Padding.</p>
            <p>Panjang kunci <b>enkripsi = panjang blok. Kunci dipotong atau diulang agar ukurannya pas.</p>
            <p>Hasil output ditampilkan dalam <b>Heksadesimal (Hex)</b> agar bebas dari karakter yang tidak terbaca.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        teks_input = st.text_area(
            "Teks Input:",
            placeholder="Masukkan plaintext teks biasa, atau ciphertext heksadesimal...",
            key="teks_blok",
        )

        kunci = st.text_input(
            "Kunci Blok (Kata):",
            placeholder="Kunci rahasia...",
            key="kunci_blok",
        )

        ukuran_blok = st.number_input(
            "Pilih Ukuran Blok (Bytes):",
            min_value=2,
            max_value=16,
            value=4,
            step=1,
            key="ukuran_blok_input",
        )

        pilihan_aksi = st.radio(
            "Pilih Aksi:",
            ["Enkripsi", "Dekripsi"],
            key="aksi_blok",
            horizontal=True,
        )

        proses_btn = st.button(
            "📦 Jalankan Block Cipher",
            type="primary",
            use_container_width=True,
        )

    with col2:
        if proses_btn:
            if not teks_input:
                st.warning("Mohon masukkan teks terlebih dahulu.")
            elif not kunci:
                st.warning("Mohon masukkan kunci terlebih dahulu.")
            else:
                ukuran = int(ukuran_blok)

                if pilihan_aksi == "Enkripsi":
                    hasil_akhir, kunci_bytes = block_cipher_encrypt(
                        teks_input,
                        kunci,
                        ukuran,
                    )

                    st.success("Enkripsi Blok Berhasil!")
                    st.markdown("**Hasil Ciphertext (Hexadesimal):**")
                    st.code(hasil_akhir)

                    with st.expander("🔍 Lihat Detail Transformasi per Blok"):
                        st.write(f"**Ukuran per Blok:** {ukuran} bytes (karakter)")
                        st.write(f"**Kunci Blok (Teks):** `{kunci_bytes.decode('utf-8', errors='ignore')}`")
                        
                        st.markdown("---")
                        st.markdown("**Proses Enkripsi (Teks → Hex/Bin → XOR):**")

                        text_bytes = teks_input.encode('utf-8')
                        pad_len = ukuran - (len(text_bytes) % ukuran)
                        padded_data = text_bytes + bytes([pad_len] * pad_len)

                        for i in range(0, len(padded_data), ukuran):
                            blok = padded_data[i:i + ukuran]
                            encrypted_b = bytearray(b ^ k for b, k in zip(blok, kunci_bytes))
                            
                            # Definisikan teks_asli agar tidak error
                            try:
                                teks_asli = blok.decode('utf-8')
                            except:
                                teks_asli = "[Mengandung Padding PKCS#7]"
                                
                            # Mengubah bytes menjadi string biner
                            bin_teks = " ".join(f"{b:08b}" for b in blok)
                            bin_kunci = " ".join(f"{k:08b}" for k in kunci_bytes)
                            bin_hasil = " ".join(f"{e:08b}" for e in encrypted_b)

                            st.code(
                                f"📝 Teks Asli : {teks_asli!r}\n"
                                f"--------------------------------------------------\n"
                                f"1. Teks  (Hex) : {blok.hex().upper()}\n"
                                f"   Teks  (Bin) : {bin_teks}\n"
                                f"2. Kunci (Hex) : {kunci_bytes.hex().upper()}\n"
                                f"   Kunci (Bin) : {bin_kunci}\n"
                                f"-------------------------------------------------- (Di-XOR)\n"
                                f"✅ Hasil (Bin) : {bin_hasil}\n"
                                f"✅ Hasil (Hex) : {encrypted_b.hex().upper()}"
                            )

                else:
                    try:
                        hasil_akhir, kunci_bytes = block_cipher_decrypt(
                            teks_input,
                            kunci,
                            ukuran,
                        )

                        st.success("Dekripsi Blok Berhasil!")
                        st.markdown("**Hasil Plaintext:**")
                        st.code(hasil_akhir)

                        with st.expander("🔍 Lihat Detail Pemulihan per Blok"):
                            st.write(f"**Ukuran per Blok:** {ukuran} bytes")
                            st.write(f"**Kunci Blok (Teks):** `{kunci_bytes.decode('utf-8', errors='ignore')}`")
                            
                            st.markdown("---")
                            st.markdown("**Proses Dekripsi (Hex/Bin → XOR → Teks):**")

                            ciphertext_bytes = bytes.fromhex(teks_input)
                            
                            for i in range(0, len(ciphertext_bytes), ukuran):
                                blok = ciphertext_bytes[i:i + ukuran]
                                decrypted_b = bytearray(b ^ k for b, k in zip(blok, kunci_bytes))
                                
                                # Mengubah kembali hasil XOR menjadi teks
                                teks_pulih = decrypted_b.decode('utf-8', errors='replace')
                                
                                # Mengubah bytes menjadi string biner
                                bin_cipher = " ".join(f"{b:08b}" for b in blok)
                                bin_kunci = " ".join(f"{k:08b}" for k in kunci_bytes)
                                bin_hasil = " ".join(f"{e:08b}" for e in decrypted_b)

                                st.code(
                                    f"🔒 Cipher(Hex) : {blok.hex().upper()}\n"
                                    f"   Cipher(Bin) : {bin_cipher}\n"
                                    f"🔑 Kunci (Hex) : {kunci_bytes.hex().upper()}\n"
                                    f"   Kunci (Bin) : {bin_kunci}\n"
                                    f"-------------------------------------------------- (Di-XOR)\n"
                                    f"🔓 Hasil (Bin) : {bin_hasil}\n"
                                    f"🔓 Hasil (Hex) : {decrypted_b.hex().upper()}\n"
                                    f"📝 Teks Pulih  : {teks_pulih!r}"
                                )
                    except ValueError:
                        st.error("Format input salah! Untuk dekripsi, input harus berupa kode Heksadesimal valid tanpa spasi.")
                        
# ============================================================
# MENU 5 — SUPER ENKRIPSI
# ============================================================
elif menu == "5. Super Enkripsi Fleksibel":
    st.markdown(
        '<p class="main-header">⚡ Menu 5: Super Enkripsi Fleksibel</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="sub-header">Rantai kombinasi dari metode kriptografi yang tersedia</p>',
        unsafe_allow_html=True,
    )
    st.markdown("*Dikerjakan bersama (Integrasi Kelompok)*")

    st.markdown(
        """
        <div class="info-box">
            <h4>📖 Panduan & Konsep Super Enkripsi</h4>
            <p>Beberapa metode dijalankan secara berurutan.
            Output dari satu metode menjadi input metode berikutnya.</p>
            <p>Super enkripsi menggunakan fungsi metode yang sama dengan
            menu masing-masing.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    jumlah_kombinasi = st.slider(
    "Pilih jumlah metode yang dikombinasikan dalam rantai:",
    min_value=2,
    max_value=4,
    value=3,
    )

    opsi_tersedia = [
        "Caesar Cipher",
        "Rail Fence",
        "Stream Cipher",
        "Block Cipher",
    ]

    pilihan_metode = []

    col_config, col_main = st.columns([1, 1], gap="medium")

    with col_config:
        st.markdown("### ⚙️ Pengaturan Rantai Metode")

        for i in range(jumlah_kombinasi):
            pilih = st.selectbox(
                f"Urutan Algoritma ke-{i + 1}:",
                opsi_tersedia,
                key=f"super_method_{i}",
            )
            pilihan_metode.append(pilih)

        st.markdown("---")
        st.markdown("### 🔑 Parameter Pendukung")

        pilihan_aksi = st.radio(
            "Pilih Aksi Super Enkripsi:",
            ["Enkripsi", "Dekripsi"],
            horizontal=True,
        )

        teks_super = st.text_area(
            "Teks Awal:",
            placeholder="Masukkan plaintext atau ciphertext...",
            key="text_super_in",
        )

        kunci_super = st.text_input(
            "Kunci Universal (Stream/Blok):",
            value="123",
            key="key_super_in",
            help="Stream Cipher membutuhkan kunci berupa angka.",
        )

        geser_super = st.number_input(
            "Nilai Caesar Shift:",
            min_value=1,
            max_value=25,
            value=3,
            step=1,
            key="shift_super_in",
        )

        rail_super = st.number_input(
            "Jumlah Rail Fence:",
            min_value=2,
            max_value=20,
            value=3,
            step=1,
            key="rail_super_in",
        )

        blok_super = st.number_input(
            "Ukuran Blok (Bytes):",
            min_value=2,
            max_value=16,
            value=4,
            step=1,
            key="blok_super_in",
        )

        jalankan_btn = st.button(
            f"⚡ Jalankan Super {pilihan_aksi}",
            type="primary",
            use_container_width=True,
        )

    with col_main:
        st.markdown(f"### 🔄 Alur & Hasil {pilihan_aksi}")

        if jalankan_btn:
            if not teks_super:
                st.warning("Mohon masukkan teks awal terlebih dahulu.")
            elif not kunci_super:
                st.warning("Mohon masukkan kunci terlebih dahulu.")
            else:
                try:
                    key_stream = int(kunci_super)
                except ValueError:
                    st.error("Kunci Universal untuk Stream Cipher harus berupa angka.")
                    st.stop()

                current_text = teks_super
                
                # Jika dekripsi, urutan metode harus dibalik
                urutan_proses = pilihan_metode if pilihan_aksi == "Enkripsi" else list(reversed(pilihan_metode))

                for idx, metode in enumerate(urutan_proses):
                    teks_sebelumnya = current_text  # Simpan teks sebelum diproses untuk keperluan visualisasi
                    
                    try:
                        with st.expander(f"Tahap {idx + 1}: {metode}", expanded=True):
                            
                            # --------------------------------------------------------
                            # 1. CAESAR CIPHER
                            # --------------------------------------------------------
                            if metode == "Caesar Cipher":
                                if pilihan_aksi == "Enkripsi":
                                    current_text = encrypt_caesar(current_text, int(geser_super))
                                else:
                                    current_text = decrypt_caesar(current_text, int(geser_super))
                                
                                st.write(f"Hasil setelah melalui **{metode}**:")
                                st.code(current_text, language="plaintext")
                                
                                st.markdown("**🔍 Detail Proses (Mapping Caesar):**")
                                mapping = get_caesar_mapping(teks_sebelumnya, int(geser_super), pilihan_aksi)
                                st.dataframe(pd.DataFrame(mapping), use_container_width=True, hide_index=True)

                            # --------------------------------------------------------
                            # 2. RAIL FENCE
                            # --------------------------------------------------------
                            elif metode == "Rail Fence":
                                if pilihan_aksi == "Enkripsi":
                                    current_text, matriks = encrypt_rail_fence(current_text, int(rail_super))
                                else:
                                    current_text, matriks = decrypt_rail_fence(current_text, int(rail_super))
                                
                                st.write(f"Hasil setelah melalui **{metode}**:")
                                st.code(current_text, language="plaintext")
                                
                                st.markdown("**🔍 Detail Proses (Matriks Transposisi):**")
                                df = pd.DataFrame(
                                    matriks,
                                    index=[f"Rail {i + 1}" for i in range(int(rail_super))],
                                    columns=[f"P-{i + 1}" for i in range(len(teks_sebelumnya))],
                                )
                                styler = df.style
                                style_func = styler.map if hasattr(styler, "map") else styler.applymap
                                st.dataframe(style_func(highlight_zigzag), use_container_width=True)

                            # --------------------------------------------------------
                            # 3. STREAM CIPHER
                            # --------------------------------------------------------
                            elif metode == "Stream Cipher":
                                if pilihan_aksi == "Enkripsi":
                                    current_text, teks_langkah = stream_cipher_encrypt(current_text, key_stream)
                                else:
                                    current_text, teks_langkah = stream_cipher_decrypt(current_text, key_stream)
                                
                                st.write(f"Hasil setelah melalui **{metode}**:")
                                st.code(current_text, language="plaintext")
                                st.info(f"🔍 Diproses menggunakan keystream pseudo-random dengan seed '{key_stream}'.")

                                st.markdown(f"**🔍 Detail Proses {metode}:**")
                                st.code(teks_langkah, language="plaintext")

                            # --------------------------------------------------------
                            # 4. BLOCK CIPHER
                            # --------------------------------------------------------
                            elif metode == "Block Cipher":
                                ukuran = int(blok_super)
                                if pilihan_aksi == "Enkripsi":
                                    current_text, kunci_bytes = block_cipher_encrypt(current_text, kunci_super, ukuran)
                                    
                                    st.write(f"Hasil setelah melalui **{metode}**:")
                                    st.code(current_text, language="plaintext")
                                    
                                    st.markdown(f"**🔍 Detail Proses Enkripsi (Kunci Hex: `{kunci_bytes.hex().upper()}`):**")
                                    text_bytes = teks_sebelumnya.encode('utf-8')
                                    pad_len = ukuran - (len(text_bytes) % ukuran)
                                    padded_data = text_bytes + bytes([pad_len] * pad_len)

                                    for i in range(0, len(padded_data), ukuran):
                                        blok = padded_data[i:i + ukuran]
                                        encrypted_b = bytearray(b ^ k for b, k in zip(blok, kunci_bytes))
                                        
                                        try: teks_asli = blok.decode('utf-8')
                                        except: teks_asli = "[Padding PKCS#7]"
                                        
                                        bin_teks = " ".join(f"{b:08b}" for b in blok)
                                        bin_kunci = " ".join(f"{k:08b}" for k in kunci_bytes)
                                        bin_hasil = " ".join(f"{e:08b}" for e in encrypted_b)

                                        st.code(
                                            f"Teks Asli: {teks_asli!r}\n"
                                            f"Teks(Hex): {blok.hex().upper()} | Bin: {bin_teks}\n"
                                            f"Kunc(Hex): {kunci_bytes.hex().upper()} | Bin: {bin_kunci}\n"
                                            f"-------------------------------------------------- (XOR)\n"
                                            f"Hasl(Hex): {encrypted_b.hex().upper()} | Bin: {bin_hasil}"
                                        )
                                else:
                                    current_text, kunci_bytes = block_cipher_decrypt(current_text, kunci_super, ukuran)
                                    
                                    st.write(f"Hasil setelah melalui **{metode}**:")
                                    st.code(current_text, language="plaintext")
                                    
                                    st.markdown(f"**🔍 Detail Proses Dekripsi (Kunci Hex: `{kunci_bytes.hex().upper()}`):**")
                                    ciphertext_bytes = bytes.fromhex(teks_sebelumnya)
                                    for i in range(0, len(ciphertext_bytes), ukuran):
                                        blok = ciphertext_bytes[i:i + ukuran]
                                        decrypted_b = bytearray(b ^ k for b, k in zip(blok, kunci_bytes))
                                        teks_pulih = decrypted_b.decode('utf-8', errors='replace')
                                        
                                        bin_cipher = " ".join(f"{b:08b}" for b in blok)
                                        bin_kunci = " ".join(f"{k:08b}" for k in kunci_bytes)
                                        bin_hasil = " ".join(f"{e:08b}" for e in decrypted_b)

                                        st.code(
                                            f"Ciph(Hex): {blok.hex().upper()} | Bin: {bin_cipher}\n"
                                            f"Kunc(Hex): {kunci_bytes.hex().upper()} | Bin: {bin_kunci}\n"
                                            f"-------------------------------------------------- (XOR)\n"
                                            f"Hasl(Hex): {decrypted_b.hex().upper()} | Bin: {bin_hasil}\n"
                                            f"Teks Pulih: {teks_pulih!r}"
                                        )

                    except Exception as e:
                        st.error(f"Terjadi kesalahan pada tahap {metode}: {e}")
                        st.stop()

                st.success(f"🎉 Super {pilihan_aksi} Selesai!")
                st.markdown(f"**Hasil Akhir ({pilihan_aksi}):**")
                st.code(current_text, language="plaintext")

                st.download_button(
                    f"📥 Unduh Hasil Akhir",
                    data=current_text,
                    file_name=f"hasil_super_{pilihan_aksi.lower()}.txt",
                    mime="text/plain",
                    use_container_width=True,
                )