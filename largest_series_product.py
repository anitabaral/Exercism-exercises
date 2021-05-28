def largest_product(series, size):

    if(len(series) < size or size < 0):
        raise ValueError("Invalid inputs")

    if(len(series) == 0):
        return 1

    final_mul = []
    for i in range(len(series)-(size-1)):
        value = 1
        for j in range(size):
            value *= int(series[i+j])
        final_mul.append(value)
    return(max(final_mul))
