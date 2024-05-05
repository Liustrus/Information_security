from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

Static_IV = b"ThisIsMyIV123456"


def encrypt_ecb(message, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_message = message.encode() + b"\0" * (16 - len(message) % 16)
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()
    return ciphertext


def decrypt_ecb(ciphertext, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_message.decode().rstrip('\x00')


def encrypt_cbc(message, key):
    cipher = Cipher(algorithms.AES(key), modes.CBC(Static_IV), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_message = message.encode() + b"\0" * (16 - len(message) % 16)
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()
    return ciphertext


def decrypt_cbc(ciphertext, key):
    cipher = Cipher(algorithms.AES(key), modes.CBC(Static_IV), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_message.decode().rstrip('\x00')


def encrypt_cfb(message, key):
    cipher = Cipher(algorithms.AES(key), modes.CFB(Static_IV), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_message = message.encode() + b"\0" * (16 - len(message) % 16)
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()
    return ciphertext


def decrypt_cfb(ciphertext, key):
    cipher = Cipher(algorithms.AES(key), modes.CFB(Static_IV), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_message.decode().rstrip('\x00')


print("LIFE HAS MANY DOORS. DO YOU HAVE YOUR KEY?")
print("A) Data encryption")
print("B) Data decryption")
print("")
choice = input("Choose what you would like to achieve: ").upper()

if choice == 'A':
    mode_choice = input("Choose encryption mode (ECB/CBC/CFB): ").upper()
    message = input("Enter text to encrypt: ")
    key = input("Enter key (16 characters): ").encode()

    if mode_choice == 'ECB':
        encrypted_message = encrypt_ecb(message, key)
        print("Encrypted (ECB mode):", encrypted_message.hex())
    elif mode_choice == 'CBC':
        encrypted_message = encrypt_cbc(message, key)
        print("Encrypted (CBC mode):", encrypted_message.hex())
    elif mode_choice == 'CFB':
        encrypted_message = encrypt_cfb(message, key)
        print("Encrypted (CFB mode):", encrypted_message.hex())
    else:
        print("No such mode")

    save_choice = input("Would you like to save the encrypted text to a file? (Y/N): ").upper()
    if save_choice == 'Y':
        filename = input("Enter name for file: ").strip()
        full_filename = os.path.join(os.path.dirname(__file__), f"{filename}.txt")
        with open(full_filename, 'wb') as file:
            file.write(encrypted_message)
            print(f"Encrypted text saved to: {full_filename}")

elif choice == 'B':
    mode_choice = input("Choose decryption mode (ECB/CBC/CFB): ").upper()
    decryption_choice = input("How would you like to provide the text? (Text/File): ").upper()

    if decryption_choice == 'TEXT':
        ciphertext = bytes.fromhex(input("Enter text to decrypt: "))
    elif decryption_choice == 'FILE':
        filename = input("Enter the file path to read text from (remove .txt at the end of path name): ").strip()
        full_filename = os.path.join(os.path.dirname(__file__), f"{filename}.txt")
        try:
            with open(full_filename, 'rb') as file:
                ciphertext = file.read()
        except FileNotFoundError:
            print("File not found. Make sure to remove .txt from file path")
            exit()

    key = input("Enter key (16 characters): ").encode()

    if mode_choice == 'ECB':
        decrypted_message = decrypt_ecb(ciphertext, key)
        print("Decrypted (ECB mode):", decrypted_message)
    elif mode_choice == 'CBC':
        decrypted_message = decrypt_cbc(ciphertext, key)
        print("Decrypted (CBC mode):", decrypted_message)
    elif mode_choice == 'CFB':
        decrypted_message = decrypt_cfb(ciphertext, key)
        print("Decrypted (CFB mode):", decrypted_message)
    else:
        print("No such mode")


else:
    print("No such choice")
