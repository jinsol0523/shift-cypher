import string
"""
Shift Cipher Encryption & Decryption

This Python script allows users to encrypt and decrypt text using a Caesar cipher, also known as a shift cipher. The script provides options for both encryption and decryption, prompting the user to choose the desired operation. 

For encryption, the user can input the plaintext and specify the encryption key. The script then outputs the encrypted text.

For decryption, the user can input the ciphered text, and the script outputs all possible decrypted texts for all key cases (0 to 25).

This project was created as a learning exercise inspired by the Math 4175 Cryptography class, aiming to provide a convenient tool for experimenting with shift ciphers.

Author: Jin Sol Park
Date: 01/26/2024
"""

def main():
    action = input("Do you want to (E)ncrypt or (D)ecrypt a text? ").lower()
    if action == 'e':
        plain_text = input("Enter the text to encrypt: ")
        key = int(input("Enter the encryption key (an integer between 0 and 25): "))
        encrypt(plain_text, key)
    elif action == 'd':
        ciphered_text = input("Enter the text to decrypt: ")
        decrypt(ciphered_text)
    else:
        print("Invalid choice. Enter 'E' for encrpytion or 'D' for decryption.")

def encrypt(plain_text, key):
    encrypted_text = ''
    for char in plain_text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) + key - 97) % 26 + 97)
            else:
                encrypted_text += chr((ord(char) + key - 65) % 26 + 65)
        else:
            encrypted_text += char
    print(f"Encrypted text: {encrypted_text}")

def decrypt(ciphered_text):
    for key in range(26):
        decrypted_text = ''
        for char in ciphered_text:
            if char.isalpha():
                if char.islower():
                    decrypted_text += chr((ord(char) - key - 97) % 26 + 97)
                else:
                    decrypted_text += chr((ord(char) - key - 65) % 26 + 65)
            else:
                decrypted_text += char
        print(f"Key {key}: {decrypted_text}")


if __name__ == "__main__":
    main()