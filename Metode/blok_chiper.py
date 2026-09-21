# Metode/blok_chiper.py

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