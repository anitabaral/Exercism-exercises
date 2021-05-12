def rotate(text, key):
    rotated = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                number = ord(char) - 96
                shift_number = number + key
                if(shift_number > 26):
                    shift_number = shift_number - 26
                rotated += chr(shift_number + 96)
            else:
                number = ord(char) - 64
                shift_number = number + key
                if(shift_number > 26):
                    shift_number = shift_number - 26
                rotated += chr(shift_number + 64)
        else:
            rotated += char

    return rotated

# def rotate (s, amount):
#
#     UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
#     upper_shifted = UPPERCASE[amount:] + UPPERCASE[:amount]
#     print(UPPERCASE[amount:])
#     print(UPPERCASE[:amount])
#     print (upper_shifted)
#     lower_shifted = LOWERCASE[amount:] + LOWERCASE[:amount]
#     print(lower_shifted)
#     translation = str.maketrans(UPPERCASE + LOWERCASE, upper_shifted + lower_shifted)
#     print(translation)
#     return s.translate(translation)
#
#
# rotate("O M G", 5)
