# coding: utf-8
from ceasar import ceasar


def main():
    text = "Привет мир!"
    s = 4
    print("Plain Text: " + text)
    print("Shift pattern: " + str(s))
    encrypted_text = ceasar.encrypt(text, s)
    print("Cipher: " + encrypted_text)
    print("Decrypted: " + ceasar.decrypt(encrypted_text))
    # print(ceasar.__countWords(text))


main()
