import sys


def convert(number):
    num, words = (3, 5, 7), ('Pling', 'Plang', 'Plong')
    result = ""

    for i in range(len(num)):
        if (int(number)%num[i] == 0):
            result += words[i]

    if (result == 0):
        result = str(number)

    print(result)
    return(result)

if __name__ =='__main__':
    globals()[sys.argv[1]](sys.argv[2])
