#-----------------------------1-----------------------------

def encrypt(k, message):
    numbers = []
    for char in message:
        numbers.append(ord(char))

    code = ""
    for index in numbers:
        code += chr((index + k) % 65536)

    return code

def decrypt(k, code):
    numbers = []
    for char in code:
        numbers.append(ord(char))

    message = ""
    for index in numbers:
        message += chr((index - k) % 65536)

    return message


#print(decrypt(3,encrypt(3,"asdfgzxc123")))

#-----------------------------2-----------------------------

from collections import Counter

def hacking(code):
    space = ord(" ")
    most_common_char = ord(Counter(code).most_common()[0][0])
    k = abs(space - most_common_char)

    numbers = []
    for char in code:
        numbers.append(ord(char))

    message = ""
    for index in numbers:
        message += chr((index - k) % 65536)

    return message


#print(hacking(encrypt(3,"asd fgh ghj vb rt gh vb vb gh kl ui o jk bn c e d f y b k c s m")))

#-----------------------------3-----------------------------

def encryptV(key, message):
    if len(message) > len(key):
        n = int(len(message) / len(key)) + 1
        key *= n

    key = list(key)
    for i, symbol in enumerate(key):
        key[i] = ord(symbol)

    numbers = []
    for char in message:
        numbers.append(ord(char))

    code = ""
    for i, index in enumerate(numbers):
        code += chr((index + key[i]) % 65536)

    return code

def decryptV(key, code):
    if len(code) > len(key):
        n = int(len(code) / len(key)) + 1
        key *= n

    key = list(key)
    for i, symbol in enumerate(key):
        key[i] = ord(symbol)

    numbers = []
    for char in code:
        numbers.append(ord(char))

    message = ""
    for i, index in enumerate(numbers):
        message += chr((index - key[i]) % 65536)

    return message


#print(decryptV("qwerty", encryptV("qwerty", "asdfgzxc123")))