from collections import Counter

def find_anagrams(word, candidates):
    anagrams = []
    sorted_word = sorted(word.lower())

    for candidate in candidates:
        sorted_candidate = sorted(candidate.lower())
        if(word.lower() == candidate.lower()):
            continue
        if sorted_word == sorted_candidate:
            anagrams.append(candidate)
    return anagrams
