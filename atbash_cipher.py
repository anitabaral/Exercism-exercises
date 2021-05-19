import re

chars = "abcdefghijklmnopqrstuvwxyz"
chars_back = "zyxwvutsrqponmlkjihgfedcba"

def _segments(segment):
    if len(segment) <= 5:
        return segment
    return segment[:5] + " " + _segments(segment[5:])

def encode(plain_text):
    trans = str.maketrans(chars + chars.upper(), chars_back + chars_back.upper())
    encoded_text = plain_text.translate(trans).lower().replace(" ", "")
    encoded_text_no_punc = re.sub(r'[^\w\s]', '', encoded_text)
    return _segments(encoded_text_no_punc)

def decode(ciphered_text):
    trans = str.maketrans(chars_back + chars_back.upper(), chars + chars.upper())
    decoded_text = ciphered_text.translate(trans).lower().replace(" ", "")
    return decoded_text
