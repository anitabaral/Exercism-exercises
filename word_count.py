
def count_words(sentence):
    sentence_lower = sentence.lower()
    punc = '''!()-[]{};:"\, <>./?@#$%^&*_~'''

    for ele in sentence_lower:
        if ele in punc:
            sentence_lower = sentence_lower.replace(ele, " ")

    sentence_words = sentence_lower.split()
    counts = dict()
    for word in sentence_words:
        word = word.strip("'")
        if len(word)>0:
            counts[word] = counts.get(word, 0)+1

    return counts

parts = count_words(""""That's the password: 'PASSWORD 123'!", cried the Special Agent.\nSo I fled.""")
print(parts)
