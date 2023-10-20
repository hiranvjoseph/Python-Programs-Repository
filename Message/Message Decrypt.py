def decrypt(secret_code, key):
    decrypted_message = ""
    for char in secret_code:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - key - shift) % 26 + shift)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

secret_code = input("Enter the secret code: ")

decrypted_message = decrypt(secret_code, key)
print("Decrypted Message:", decrypted_message)
