less_than_20_dict = {0: '',1 : 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

tens_dict = {10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred'}

dict = {100: ' hundred',1000: ' thousand', 1000000: ' million', 1000000000: ' billion'}

def less_than_20(num):
    return less_than_20_dict[num]

def less_than_100(num):
    if(num == 100):
        return less_than_20_dict[1] + dict[num]

    first_part = int(num / 10) * 10
    last_part = num % 10
    if(first_part == 0 ):
        return less_than_20(last_part)
    if(last_part == 0):
        return tens_dict[first_part]
    return tens_dict[first_part] + "-" + less_than_20_dict[last_part]

def less_than_1000(num):
    if(num == 1000):
        return less_than_20_dict[1] + dict[num]

    first_part = int(num / 100)
    second_part = num % 100
    if(first_part == 0 ):
        return less_than_100(second_part)
    return less_than_20_dict[first_part] + " hundred " + less_than_100(second_part)

def less_than_1000000(num):
    if(num == 1000000):
        return less_than_20_dict[1] + dict[num]

    first_part = int(num / 1000)
    second_part = num % 1000
    return less_than_1000(first_part) + " thousand " + less_than_1000(second_part)

def less_than_1000000000(num):
    if(num == 1000000000):
        return less_than_20_dict[1] + dict[num]


    first_part = int(num / 1000000)
    second_part = num % 1000000
    print(first_part)
    print(second_part)
    return less_than_1000(first_part) + " million " + less_than_1000000(second_part)

def less_than_1000000000000(num):
    if(num == 1000000000):
        return less_than_20_dict[1] + dict[num]

    first_part = int(num / 1000000000)
    second_part = num % 1000000000
    return less_than_1000(first_part) + " billion " + less_than_1000000000(second_part)

def say(number):
    if(number < 0):
        raise ValueError('Negative number')

    if(number == 0):
        return 'zero'

    if(number < 20):
        return less_than_20(number)

    if(number <= 100):
        return less_than_100(number)

    if(number <= 1000):
        return less_than_1000(number)

    if(number <= 1000000):
        return less_than_1000000(number)

    if(number <= 1000000000):
        return less_than_1000000000(number)

    if(number < 1000000000000):
        return less_than_1000000000000(number)

    else:
        raise ValueError("Number not valid")
print(say(1002345))
