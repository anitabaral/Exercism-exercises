def distance(strand_a, strand_b):
    if (len(strand_a) == len(strand_b)):
        count = 0
        for i in range(len(strand_a)):
            if (strand_a[i] != strand_b[i]):
                count += 1

    else:
        raise ValueError("Length of two DNA strands must be equal")

    return count

# print(distance('caacga', 'gaacct'))

#only this statement can also be used
#return sum(a != b for a, b in zip(strand_a, strand_b))
