# Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

decision = input("Do you want to encrypt or decrypt? ")
word = input("Enter a word: ")
shift = int(input("By how many places should the letters be shifted? "))


def encrypt(shift_number, text):
    new_word = ""
    for char in text:
        position = alphabet.index(char)
        new_position = position + shift_number
        new_letter = alphabet[new_position]
        new_word += new_letter
    print(f"The encrypted word is {new_word}")


def decrypt(shift_number, new_word):
    text = ""
    for char in new_word:
        position = alphabet.index(char)
        new_position = position - shift_number
        new_letter = alphabet[new_position]
        text += new_letter
    print(f"The decrypted word is {text}")


if decision == 'encode':
    encrypt(shift, word)
elif decision == 'decode':
    decrypt(shift, word)