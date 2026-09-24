def encrypt_caesar(text, shift):
    hasil = []
    for char in text:
        if char.isupper():
            hasil.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        elif char.islower():
            hasil.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            hasil.append(char)
    return "".join(hasil)


def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)


def get_caesar_mapping(text, shift, mode="Enkripsi"):
    efektif_shift = shift if mode == "Enkripsi" else -shift
    mapping = []
    for char in text:
        if char.isalpha():
            mapping.append({
                "Karakter Asli": char,
                "Karakter Hasil": encrypt_caesar(char, efektif_shift),
                "Pergeseran": efektif_shift % 26,
            })
        else:
            mapping.append({
                "Karakter Asli": char,
                "Karakter Hasil": char,
                "Pergeseran": 0,
            })
    return mapping
