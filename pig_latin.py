import re

def _rotate(text):
    return text[1:] + text[0]

def translate_word(text):
    if re.match('^xr', text) or re.match('^yt', text):
        return text + 'ay'

    if text[0] == 'y':
        text = _rotate(text)
    else:
        while text[0] not in 'aeiouy':
            text = _rotate(text)

    if text[-1] == 'q' and text[0] == 'u':
        text = _rotate(text)

    return text + 'ay'


def translate(text):
    return ' '.join([translate_word(word) for word in text.split(' ')])
