
dict = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 50: 'L', 100: 'C', 500 : 'D', 1000: 'M', 40:'XL', 90: 'XC', 400: 'CD', 900:'CM'}

def identify_last_part(last_part):
    if int(last_part) <= 10:
        return less_than_10(last_part)
    if 10 < int(last_part) < 40:
        return less_than_40(last_part)
    if 40 <= int(last_part) < 50:
        return less_than_50(last_part)
    if 50 <= int(last_part) < 90:
        return less_than_90(last_part)
    if 90 <= int(last_part) < 100:
        return less_than_100(last_part)

def less_than_40(number):
    first_final_value = ''
    first_part = number[0]
    last_part = number[1]

    if first_part == '0':
        first_part = number[1]
        last_part = number[2]
    for i in range(int(first_part)):
        first_final_value += dict[10]
    return first_final_value+dict[int(last_part)]

def less_than_50(number):
    if int(number) == 40:
        return dict[40]
    last_part = number[1]
    return dict[40]+dict[int(last_part)]

def less_than_90(number):
    if int(number) == 50:
        return dict[50]
    num = int(number) - 50
    if num<10:
        last_part = less_than_10(str(num))

    else:
        last_part = less_than_40(str(num))
    return dict[50]+last_part

def less_than_100(number):
    if int(number) == 90:
        return dict[90]
    last_part = number[1]
    return dict[90]+dict[int(last_part)]

def less_than_400(number):
    first_final_value = ''
    first_part =number[0]
    last_part = number[1:]

    for i in range(int(first_part)):
        first_final_value += dict[100]

    return first_final_value + identify_last_part(last_part)

def less_than_500(number):
    if int(number) == 400:
        return dict[400]
    last_part = number[1:]

    return dict[400] + identify_last_part(last_part)

def less_than_900(number):
    if int(number) == 500:
        return dict[500]
    last_part = number[1:]

    return dict[500] + identify_last_part(last_part)

def less_than_1000(number):
    if int(number) == 900:
        return dict[900]
    last_part = number[1:]

    return dict[900] + identify_last_part(last_part)

def less_than_3000(number):

    first_final_value = ''
    first_part =number[0]
    last_part = number[1:]

    for i in range(int(first_part)):
        first_final_value += dict[1000]
    if int(number) == 3000:
        return first_final_value

    if 10 < int(last_part) < 100:
        final_val = identify_last_part(last_part)
    if 100< int(last_part)<400:
        final_val = less_than_400(last_part)
    if 400<= int(last_part)<500:
        final_val = less_than_500(last_part)
    if 500<= int(last_part)<900:
        final_val = less_than_900(last_part)
    if 900 <= int(last_part) < 1000:
        final_val = less_than_1000(last_part)
    return first_final_value + final_val

def roman(number):
    if number == 100:
        return dict[100]

    if number<=10:
        return dict[int(number)]

    if 10 < number < 40:
        return less_than_40(str(number))

    if 40 <= number < 50:
        return less_than_50(str(number))

    if 50 <= number < 90:
        return less_than_90(str(number))

    if 90 <= number < 100:
        return less_than_100(str(number))


    if 100 < number < 400:
        return less_than_400(str(number))

    if 400 <= number<500:
        return less_than_500(str(number))

    if 500<=number<900:
        return less_than_900(str(number))

    if 900<=number<1000:
        return less_than_1000(str(number))

    if 1000<=number<=3000:
        return less_than_3000(str(number))
