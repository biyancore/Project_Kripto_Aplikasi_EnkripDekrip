import streamlit as st
import random

def main():
    st.set_page_config(page_title="Kriptografi", layout="wide", page_icon="🔐")
    st.title("Cipher Aliran")

    st.caption("Algoritma *Stream Cipher* memproses pesan satu per satu per karakter dengan prinsip **FIFO (First-In, First-Out)**. Cocok untuk pengiriman data cepat tanpa harus menunggu semua pesan terkumpul (seperti *streaming*).")
    st.markdown("<hr style='margin-top: 5px; margin-bottom: 15px;'>", unsafe_allow_html=True)
    
    pesan = st.text_input("Masukkan Pesan : ")
    kunci = st.number_input("Masukkan Kunci (angka) : ", min_value=0, step=1)
    st.caption("*Kunci ini berfungsi sebagai patokan agar sistem menghasilkan aliran angka acak (keystream) yang sama persis saat proses enkripsi maupun dekripsi.*")

    mode = st.radio("Pilih Mode : ", ("Enkripsi", "Dekripsi"), horizontal=True)
    
    if st.button("Proses Sekarang"):
        st.markdown("<hr style='margin-top: 5px; margin-bottom: 15px;'>", unsafe_allow_html=True)

        if not pesan: 
            st.warning("Pesan belum diisi. Silakan masukkan teks terlebih dahulu!")
        
        else: 
            st.subheader(f"Menampilkan Proses {mode}")
            st.caption("Proses di bawah ini menunjukkan bagaimana **Karakter Asli** (diubah ke format Biner 8-bit) digabungkan dengan **Kunci Acak (Keystream)** menggunakan **Gerbang Logika XOR** bit demi bit.")
            
            random.seed(kunci)
            result = ""
            langkah_text = ""  

            for char in pesan:
                keystream = random.randint(0, 255)
                
                # Mengubah karakter dan keystream ke format Biner 8-bit untuk ditampilkan
                bin_char = format(ord(char), '08b')
                bin_key = format(keystream, '08b')
                
                # Proses XOR (Logika inti tetap dipertahankan)
                hasil_xor = ord(char) ^ keystream
                bin_hasil = format(hasil_xor, '08b')
                
                processed_char = chr(hasil_xor)
                result += processed_char   

                # Menampilkan penjelasan dengan format biner bersusun ke bawah
                langkah_text += f"Karakter: '{char}' (ASCII: {ord(char)})\n"
                langkah_text += f"Biner Teks  : {bin_char}\n"
                langkah_text += f"Biner Kunci : {bin_key} ⊕\n"
                langkah_text += f"-----------------------\n"
                langkah_text += f"Hasil XOR   : {bin_hasil} -> Karakter Sandi: {repr(processed_char)}\n\n"

            st.code(langkah_text, language="text")

            st.success("Pemrosesan Selesai")
            st.markdown("Hasil Akhir : ")
            st.code(result, language="text")

if __name__ == "__main__":
    main()
