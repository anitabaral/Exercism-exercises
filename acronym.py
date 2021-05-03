def abbreviate(words):
    words = words.upper()
    words_splitted = words.split()
    abb = ''
    for word in words_splitted:
        abb += word[0]
    return abb
