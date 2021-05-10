

from itertools import groupby
import itertools

def encode(string):
    if len(string) <= 1:    return string
    encoded = ""
    counts = []
    count = 1
    for a, b in itertools.zip_longest(string, string[1:], fillvalue=None):
        if a==b:
            count += 1
        else:
            counts.append((a, count))
            count = 1

    for x, y in counts:
        if y == 1:
            encoded += x
        else:
            encoded += str(y)
            encoded += x
    return encoded

def decode(string):
    if len(string) <= 1:    return string
    output = ""
    digits = ""

    if string[0].isdigit():
        digits += string[0]
    else:
        output += string[0]


    for i in range(1, len(string)):
        if string[i].isdigit():
            digits += string[i]
        else:
            if digits == "":
                output += string[i]
            else:
                n = int(digits)
                for cnt in range(0, n):
                    output += string[i]
            digits = ""

    return output
