import random
import os

def euclidean_alg(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_euclidean_alg(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        max_divisor, x, y = extended_euclidean_alg(b % a, a)
        return (max_divisor, y - (b // a) * x, x)

def mod_inv(a, m):
    gcd, x, y = extended_euclidean_alg(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def generate_e(phi_n):
    while True:
        e = random.randint(2, phi_n - 1)
        if euclidean_alg(e, phi_n) == 1:
            return e

def rsa_encrypt(m, e, n):
    encrypted = pow(m, e, n)
    return encrypted

def rsa_decrypt(c, d, n):
    decrypted = pow(c, d, n)
    return decrypted

def text_to_ascii(text):
    return [ord(char) for char in text]

def ascii_to_text(ascii_list):
    return ''.join([chr(symbol) for symbol in ascii_list])

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().strip().split(',')
    except FileNotFoundError:
        print("File not found. Make sure to provide the correct file path.")
        exit()

print("RSA algorithm app")
print("A) Data encryption")
print("B) Data decryption")
print("")

choice = input("Choose what you would like to achieve: ").upper()

if choice == 'A':
    input_text = input("Enter text to encrypt: ")
    p = int(input("Enter number p (suggestion - 157): "))
    q = int(input("Enter number q (suggestion - 179): "))

    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = generate_e(phi_n)
    d = mod_inv(e, phi_n)

    public_key = (n, e)
    private_key = (n, d)

    ascii_symbols = text_to_ascii(input_text)
    encrypted_symbols = [rsa_encrypt(symbol, e, n) for symbol in ascii_symbols]

    print("Generated public key:", public_key)
    print("Generated private key:", private_key)
    print("Encrypted Text:", encrypted_symbols)

    save_choice_1 = input("Would you like to save the encrypted text to a file? (Y/N): ").upper()

    if save_choice_1 == 'Y':
        filename = input("Enter name for file: ").strip()
        full_filename = os.path.join(os.path.dirname(__file__), f"{filename}.txt")
        with open(full_filename, 'w') as file:
            file.write(','.join(map(str, encrypted_symbols)))
        print(f"Encrypted text saved to: {full_filename}")

    save_choice_2 = input("Would you like to save the public key to a file? (Y/N): ").upper()

    if save_choice_2 == 'Y':
        filename = input("Enter name for file: ").strip()
        full_filename = os.path.join(os.path.dirname(__file__), f"{filename}.txt")
        with open(full_filename, 'w') as file:
            file.write(','.join(map(str, public_key)))
        print(f"Public key saved to: {full_filename}")

    save_choice_3 = input("Would you like to save the private key to a file? (Y/N): ").upper()

    if save_choice_3 == 'Y':
        filename = input("Enter name for file: ").strip()
        full_filename = os.path.join(os.path.dirname(__file__), f"{filename}.txt")
        with open(full_filename, 'w') as file:
            file.write(','.join(map(str, private_key)))
        print(f"Private key saved to: {full_filename}")

elif choice == 'B':
    encrypted_text_file = input("Enter the filename for the encrypted text: ").strip()
    private_key_file = input("Enter the filename for the private key: ").strip()

    encrypted_text = read_from_file(encrypted_text_file)
    private_key = read_from_file(private_key_file)

    n = int(private_key[0])
    d = int(private_key[1])

    encrypted_symbols = [int(symbol) for symbol in encrypted_text]

    decrypted_symbols = [rsa_decrypt(symbol, d, n) for symbol in encrypted_symbols]
    decrypted_text = ascii_to_text(decrypted_symbols)
    print("Decrypted Text:", decrypted_text)

