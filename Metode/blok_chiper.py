# Metode/blok_cipher.py

def pad_bytes(data: bytes, block_size: int) -> bytes:
    # Menggunakan standar PKCS#7 Padding modern
    pad_len = block_size - (len(data) % block_size)
    return data + bytes([pad_len] * pad_len)

def unpad_bytes(data: bytes) -> bytes:
    pad_len = data[-1]
    return data[:-pad_len]

def siapkan_kunci_bytes(key: str, block_size: int) -> bytes:
    key_bytes = key.encode('utf-8') if key else b"KUNCI"
    # Mengulang/memotong bit kunci agar panjangnya sama persis dengan blok
    return (key_bytes * ((block_size // len(key_bytes)) + 1))[:block_size]

def block_cipher_encrypt(text: str, key: str, block_size: int):
    text_bytes = text.encode('utf-8')
    padded_data = pad_bytes(text_bytes, block_size)
    key_block = siapkan_kunci_bytes(key, block_size)
    
    ciphertext_bytes = bytearray()
    
    for i in range(0, len(padded_data), block_size):
        blok = padded_data[i:i+block_size]
        # Operasi XOR (^) bit per bit antara plainteks dan kunci
        encrypted_block = bytearray(b ^ k for b, k in zip(blok, key_block))
        ciphertext_bytes.extend(encrypted_block)
        
    # Mengembalikan hasil dalam format Heksadesimal agar bersih dari simbol aneh
    return ciphertext_bytes.hex().upper(), key_block

def block_cipher_decrypt(hex_ciphertext: str, key: str, block_size: int):
    # Mengubah Heksadesimal kembali menjadi susunan bit
    ciphertext_bytes = bytes.fromhex(hex_ciphertext)
    key_block = siapkan_kunci_bytes(key, block_size)
    
    plaintext_bytes = bytearray()
    
    for i in range(0, len(ciphertext_bytes), block_size):
        blok = ciphertext_bytes[i:i+block_size]
        # Operasi XOR (^) bit per bit untuk mengembalikan data
        decrypted_block = bytearray(b ^ k for b, k in zip(blok, key_block))
        plaintext_bytes.extend(decrypted_block)
        
    # Membuang padding dan mengubah bit kembali menjadi teks
    unpadded_data = unpad_bytes(plaintext_bytes)
    return unpadded_data.decode('utf-8'), key_block