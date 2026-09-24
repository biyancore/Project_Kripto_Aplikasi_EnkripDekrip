import random

def aliran_chiper(text, key, mode):
    print ("Chiper Aliran")
    random.seed(key)
    result = ""

    for char in text:
        keystream = random.randint(0, 255)
        processed_char = chr(ord(char) ^ keystream)
        result += processed_char   

        print(f"Char: {char} | Keystream: {keystream} | Processed Char: {processed_char}")

    print(f"Final Result: {result}")
    return result

def main():
    print("Chiper Aliran")

    pesan = input("Masukkan Pesan: ")

    while True:
        try:
            kunci = int(input("Masukkan Kunci (angka): "))
            break
        except ValueError:
            print("Kunci harus berupa angka. Silakan coba lagi.")

    print("\nPilih Mode: ")
    print("1. Enkripsi")
    print("2. Dekripsi")
    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == '1':
        aliran_chiper(pesan, kunci, "enkripsi")
    elif pilihan == '2':
        aliran_chiper(pesan, kunci, "dekripsi")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
