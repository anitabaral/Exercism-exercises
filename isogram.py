def is_isogram(string):
    string = string.lower()
    
    k = len(string)
    for i in range(len(string)):
        m = i
        k = k-1
        for j in range(k):
            m = m + 1
            if ((string[i] == string[m]) & (string[i] != ' ') & (string[i] != '-')):
                    return ('not Isogram');

    return ('isogram');
