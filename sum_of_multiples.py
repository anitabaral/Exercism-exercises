def sum_of_multiples(limit, multiples):
    sum_numbers = []
    for multiple in multiples:
        if(multiple == 0):
            continue
        for i in range(limit):
            if i%multiple == 0:
                sum_numbers.append(i)
    return (sum(set(sum_numbers)))
