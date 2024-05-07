import random

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

def text_to_ascii(text):
    return [ord(char) for char in text]

def ascii_to_text(ascii_list):
    return ''.join([chr(symbol) for symbol in ascii_list])

def generate_signature(message, private_key):
    n, d = private_key
    signature = pow(message, d, n)
    return signature

def verify_signature(signature, message, public_key):
    n, e = public_key
    decrypted_signature = pow(signature, e, n)
    return decrypted_signature == message

p = 157
q = 179
input_text = "It worked somehow"

n = p * q
phi_n = (p - 1) * (q - 1)
e = generate_e(phi_n)
d = mod_inv(e, phi_n)

public_key = (n, e)
private_key = (n, d)

ascii_values = text_to_ascii(input_text)
message = sum(ascii_values)

signature = generate_signature(message, private_key)

print("Message:", input_text)
print("Digital Signature:", signature)

is_valid = verify_signature(signature, message, public_key)

if is_valid:
    print("Signature is valid.")
else:
    print("Signature is invalid.")