def hex_to_bin(hex_string):
    return bin(int(hex_string, 16))[2:]

def bin_to_hex(binary_string):
    return hex(int(binary_string, 2))[2:]

def encrypt_ecb(plaintext_hex, key_bin):
    # Convert plaintext to binary
    plaintext_bin = hex_to_bin(plaintext_hex)

    # Pad the plaintext if needed
    while len(plaintext_bin) % 4 != 0:
        plaintext_bin = '0' + plaintext_bin

    # Divide plaintext into blocks of 4 bits
    blocks = [plaintext_bin[i:i+4] for i in range(0, len(plaintext_bin), 4)]

    # Initialize the result list
    encrypted_result = []

    # Encrypt each block
    for block in blocks:
        # XOR block with key
        xor_result = ''.join(str(int(b) ^ int(k)) for b, k in zip(block, key_bin))

        # Shift each bit to the left
        shifted_result = xor_result[1:] + xor_result[0]

        # Convert the result to hexadecimal and add to the list
        encrypted_result.append(bin_to_hex(shifted_result))

    return encrypted_result

# Input plaintext dan key dari pengguna
plaintext_hex = input("Masukkan plaintext dalam hexadecimal: ")
key_bin = input("Masukkan kunci dalam biner: ")

# Enkripsi plaintext menggunakan ECB
encrypted_result = encrypt_ecb(plaintext_hex, key_bin)

# Tampilkan hasil dalam bentuk list
print(f"\nPlaintext: {plaintext_hex}")
print(f"Key: {key_bin}")
print(f"Hasil Enkripsi ECB: {encrypted_result}")
