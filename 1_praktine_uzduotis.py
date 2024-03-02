import string

def cypher(text, key):

    # alphabet = list(string.ascii_letters + string.digits) #uppercase, lowercase and digits
    alphabet = list(string.printable) #all ascii letters, numbers, digits and symbols

    text_length = len(text)
    key_length = len(key)
    coded = []

    x = 0
    i = 0
    while x < text_length and i < text_length:
        a = key[x % key_length]
        c = text[i]
        b = alphabet.index(a)
        d = alphabet.index(c)
        y = (b + d) % len(alphabet)
        coded.append(alphabet[y])
        x += 1
        i += 1
    coded_string = ''.join(coded)
    print(coded_string)
    return coded

def decypher(coded, key):

    # alphabet = list(string.ascii_letters + string.digits) #uppercase, lowercase and digits
    alphabet = list(string.printable) #all ascii letters, numbers, digits and symbols

    key_length = len(key)
    decoded = []

    xx = 0
    ii = 0
    while xx < len(coded) and ii < len(coded):
        aa = key[xx % key_length]
        cc = coded[ii]
        bb = alphabet.index(aa)
        dd = alphabet.index(cc)
        yy = (dd - bb) % len(alphabet)
        decoded.append(alphabet[yy])
        xx += 1
        ii += 1
    decoded_string = ''.join(decoded)
    print(decoded_string)
    return decoded



print('Input text: ')
text = input()
print('Input a key: ')
key = input()

print('\nWhat would you like to do with this text? \n \nA) cipher \nB) decipher')
choice = input()
choice = choice.upper()

if choice == 'A':
    coded_result = cypher(text, key)
elif choice == 'B':
    decypher_result = decypher(text, key)
else:
    print('Invalid choice')