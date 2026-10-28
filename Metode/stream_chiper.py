import random

def stream_cipher_process(pesan: str, kunci: int):
    random.seed(kunci)
    result = ""
    langkah_text = ""

    for char in pesan:
        keystream = random.randint(0, 255)
        hasil_xor = ord(char) ^ keystream
        result += chr(hasil_xor)

        langkah_text += f"Karakter: {repr(char)} (ASCII: {ord(char)})\n"
        langkah_text += f"Biner Teks  : {format(ord(char), '08b')}\n"
        langkah_text += f"Biner Kunci : {format(keystream, '08b')} ⊕\n"
        langkah_text += "-----------------------\n"
        langkah_text += f"Hasil XOR   : {format(hasil_xor, '08b')} -> Karakter Sandi: {repr(chr(hasil_xor))}\n\n"

    return result, langkah_text


def stream_cipher_encrypt(pesan: str, kunci: int):
    hasil, langkah = stream_cipher_process(pesan, kunci)
    hasil_hex = hasil.encode("utf-16-be").hex()   # aman disalin
    return hasil_hex, langkah


def stream_cipher_decrypt(hex_pesan: str, kunci: int):
    hex_bersih = "".join(hex_pesan.split())       # buang spasi/newline kalau ada
    pesan = bytes.fromhex(hex_bersih).decode("utf-16-be")
    return stream_cipher_process(pesan, kunci)
