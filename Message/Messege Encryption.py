def encrypt(message, key):
    secret_code = ""
    for char in message:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) + key - shift) % 26 + shift)
            secret_code += encrypted_char
        else:
            secret_code += char
    return secret_code

message = input("Enter your message: ")
key = int(input("Enter an encryption key (a number): "))

secret_code = encrypt(message, key)
print("Secret Code:", secret_code)

