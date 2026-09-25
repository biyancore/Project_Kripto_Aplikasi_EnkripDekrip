import random

def stream_cipher_process(pesan: str, kunci: int):
    """
    Fungsi inti untuk memproses teks menggunakan Stream Cipher (XOR).
    Mengembalikan teks hasil (enkripsi/dekripsi) dan teks penjelasan langkah-langkah.
    """
    random.seed(kunci)
    result = ""
    langkah_text = ""  

    for char in pesan:
        # Menghasilkan aliran kunci (keystream)
        keystream = random.randint(0, 255)
        
        # Mengubah karakter dan keystream ke format Biner 8-bit untuk ditampilkan
        bin_char = format(ord(char), '08b')
        bin_key = format(keystream, '08b')
        
        # Proses XOR (Logika inti)
        hasil_xor = ord(char) ^ keystream
        bin_hasil = format(hasil_xor, '08b')
        
        processed_char = chr(hasil_xor)
        result += processed_char   

        # Menyusun teks langkah-langkah dengan format biner bersusun ke bawah
        langkah_text += f"Karakter: '{char}' (ASCII: {ord(char)})\n"
        langkah_text += f"Biner Teks  : {bin_char}\n"
        langkah_text += f"Biner Kunci : {bin_key} ⊕\n"
        langkah_text += f"-----------------------\n"
        langkah_text += f"Hasil XOR   : {bin_hasil} -> Karakter Sandi: {repr(processed_char)}\n\n"

    return result, langkah_text

def stream_cipher_encrypt(pesan: str, kunci: int):
    """
    Fungsi untuk enkripsi Stream Cipher.
    """
    return stream_cipher_process(pesan, kunci)

def stream_cipher_decrypt(pesan: str, kunci: int):
    """
    Fungsi untuk dekripsi Stream Cipher.
    (Pada Stream Cipher dengan XOR, proses enkripsi dan dekripsi sama)
    """
    return stream_cipher_process(pesan, kunci)