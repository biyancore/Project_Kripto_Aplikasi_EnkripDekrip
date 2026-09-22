# ==========================================
# MODUL RAIL FENCE CIPHER (Oleh: Andini)
# Logika murni — dipakai di Menu 2 (Rail Fence) DAN Menu 5 (Super Enkripsi)
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
