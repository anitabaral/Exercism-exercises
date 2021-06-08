import re
from math import ceil, sqrt

def cipher_text(plain_text):
    if plain_text == '':
        return ''

    text = re.sub('[^A-Za-z0-9]+','', plain_text).lower()

    coloumns = int(ceil(sqrt(len(text))))
    rows = ceil(len(text)/coloumns)

    text += ' ' * ((coloumns * rows) - len(text))

    return " ".join([text[i::coloumns] for i in range(coloumns)])
