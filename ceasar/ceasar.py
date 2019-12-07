# coding: utf-8

import re

# lower_cyrillic = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
# upper_cyrillic = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']

# class Ceasar:
#     @staticmethod
#     def encrypt(text, shift):
#         return text.translate(
#             str.maketrans(
#                 string.ascii_uppercase + string.ascii_lowercase,
#                 string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift] +
#                 string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
#             )
#         )

#     @staticmethod
#     def decrypt(text, shift):
#         return Ceasar.encrypt(text, 26-shift)

# __lower_cyrillic = [chr(i) for i in range(ord('а'), ord('я') + 1)]
# lower_cyrillic.insert(6,'ё')
# __upper_cyrillic = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
# upper_cyrillic.insert(6,'Ё')

__lower_cyrillic = ''.join(map(chr, range(ord('а'), ord('я') + 1)))
__upper_cyrillic = ''.join(map(chr, range(ord('А'), ord('Я') + 1)))


def __countWords(s):
    if len(s) == 0:
        return []
    res = {}
    words = re.split(r' |\n|\,|\.|\!|\?|\;|\:|\!\?|\?\!', s)
    for word in words:
        if len(word) == 0:
            continue
        word = word.casefold()
        res[word] = res[word] + 1 if res.get(word) else 1
        # res.setdefault(word, res.get(word) if res.get(word) + 1 else 1)
    # return Array.from(res).sort((a, b) => a[1] - b[1]);
    return res


def __read_dictionary(dict_file="./dictionary.txt"):
    with open(dict_file) as file:
        lines = [line.strip() for line in file]
        return lines


def __alphabet(shift):
    shift = shift % len(__lower_cyrillic)
    return __lower_cyrillic[shift:] + \
        __lower_cyrillic[:shift] + \
        __upper_cyrillic[shift:] + \
        __upper_cyrillic[:shift]


def encrypt(text, shift):
    a1 = __lower_cyrillic + __upper_cyrillic
    a2 = __alphabet(shift)
    return text.translate(
        str.maketrans(a1, a2)
    )


def decrypt(text):
    # a1 = __lower_cyrillic + __upper_cyrillic
    # a2 = __alphabet(shift)
    russian_dict = __read_dictionary()
    words_encrypted = list(__countWords(text).keys())
    words_in_rudict = {}
    for i in range(31, 1, -1):
        for word in words_encrypted:
            if encrypt(word, i) in russian_dict:
                words_in_rudict[i] = words_in_rudict[i] + \
                    1 if words_in_rudict.get(i) else 1
    decrypt_shift = (
        max(words_in_rudict, key=lambda key: words_in_rudict[key]))
    decrypted_text = encrypt(text, decrypt_shift)
    return decrypted_text
    # return text.translate(
    #     str.maketrans(a2, a1)
    # )
