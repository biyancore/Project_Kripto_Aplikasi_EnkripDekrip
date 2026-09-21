import time
import pandas as pd
import streamlit as st

# ==========================================
# 1. HELPER LOGIC RAIL FENCE 
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

def highlight_zigzag(val):
    if val != ".":
        return "background-color: #2980b9; color: #ffffff; font-weight: bold; text-align: center; border: 1px solid #3498db;"
    return "color: #bdc3c7; text-align: center; border: 1px dashed #ecf0f1; background-color: #fafbfc;"


# ==========================================
# 2. FUNGSI UTAMA HALAMAN RAIL FENCE
# ==========================================
def render_rail_fence_page():
    
    # Kustomisasi UI dengan CSS Murni & Statis
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

    # Header Spektakuler
    st.markdown('''
    <div class="header-box">
        <h1 class="header-title">🎢 Algoritma Rail Fence</h1>
        <p class="header-subtitle">Modul Kriptografi Transposisi | Enginer: Andini</p>
    </div>
    ''', unsafe_allow_html=True)

    # Interaksi Layout & Input
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        teks_input = st.text_input("Teks Pesan:", value="TEKNIK INFORMATIKA", help="Masukkan teks yang ingin diproses tanpa karakter spesial", key="rf_teks")
    with col2:
        jumlah_rail = st.number_input("Kedalaman Rail:", min_value=2, max_value=20, value=3, key="rf_rail")
    with col3:
        pilihan_aksi = st.selectbox("Operasi:", ["Enkripsi", "Dekripsi"], key="rf_aksi")

    btn_proses = st.button("⚡ Eksekusi Algoritma", use_container_width=True, key="rf_btn")
    st.markdown("---")

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
                mime="text/plain",
                key="rf_download"
            )

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
