import random
from string import ascii_lowercase
from itertools import cycle

class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = "".join(random.choice(ascii_lowercase) for _ in range(100))
        else:
            self.key = key

    def encode(self, text):
        encoded = []
        for ch1, ch2 in zip(text, cycle(self.key)):
            encoded.append(ascii_lowercase[(ascii_lowercase.index(ch1) + ascii_lowercase.index(ch2)) % 26 ])
            # encoded.append(ascii_lowercase[(ord(ch1) % 97 + ord(ch2) % 97) % 26])
        return "".join(encoded)

    def decode(self, text):
        decoded = []
        for ch1, ch2 in zip(text, cycle(self.key)):
            decoded.append(ascii_lowercase[(ascii_lowercase.index(ch1) - ascii_lowercase.index(ch2)) % 26 ])
            # decoded.append(ascii_lowercase[(ord(ch1) % 97 - ord(ch2) % 97) % 26])
        return "".join(decoded)
