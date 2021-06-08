def score(word):
    word = word.lower()
    letters = list(word)
    myDict = {
        **dict.fromkeys(['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'], 1),
        **dict.fromkeys([ 'd', 'g'], 2),
        **dict.fromkeys(['b', 'c', 'm', 'p'], 3),
        **dict.fromkeys(['f', 'h', 'v', 'w', 'y'], 4),
        **dict.fromkeys(['k'], 5),
        **dict.fromkeys(['j', 'x'], 8),
        **dict.fromkeys(['q', 'z'], 10)
    }
    count = 0
    for letter in letters:
        count += myDict.get(letter)
    return count

print(score('cabbage'))
