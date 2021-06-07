def factors(value):
    factors_here , num = [], 2
    while value>1:
        if (value % num) == 0:
            factors_here.append(num)
            value /= num
        else:
            num += 1
    return factors_here
