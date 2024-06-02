def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                char_code = ord(char) + shift_amount
                if char_code > ord('z'):
                    char_code -= 26
                encrypted_text += chr(char_code)
            elif char.isupper():
                char_code = ord(char) + shift_amount
                if char_code > ord('Z'):
                    char_code -= 26
                encrypted_text += chr(char_code)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption and Decryption")
    print("Type '1' to encrypt or '2' to decrypt:")
    choice = input().strip()

    if choice not in ['1', '2']:
        print("Invalid choice! Please type '1' for encryption or '2' for decryption.")
        return

    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == '1':
        result = caesar_cipher_encrypt(text, shift)
    else:
        result = caesar_cipher_decrypt(text, shift)

    print(f"The resulting text is: {result}")

if __name__ == "__main__":
    main()
