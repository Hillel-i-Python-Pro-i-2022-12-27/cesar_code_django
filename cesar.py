import string
from gettext import find


def crypto(text: str, key: int):
    obrazec = string.printable

    newtext = []

    key = key % len(obrazec)

    if key == len(obrazec):
        return text

    for i in text:
        index = obrazec.find(i)
        if i == ' ':
            if_key = obrazec.find(' ')
        else:
            if_key = index + key

        if if_key > len(obrazec):
            if_key = if_key - len(obrazec)

        letter = obrazec[if_key]
        newtext.append(letter)
    return "".join(newtext)


def decrypto(text: str, key: int):
    obrazec = string.printable
    newtext = []

    key = key % len(obrazec)

    if key == len(obrazec):
        return text

    for i in text:
        index = obrazec.find(i)

        if i == ' ':
            if_key = obrazec.find(' ')
        else:
            if_key = index - key

        if if_key > len(obrazec):
            if_key = len(obrazec) - if_key

        letter = obrazec[if_key]
        newtext.append(letter)
    return "".join(newtext)


crypto_result = crypto(text="aaaa ,bbbb", key=7234)
print(crypto_result)
print(decrypto(text=crypto_result, key=7234))