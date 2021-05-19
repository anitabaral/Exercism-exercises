def primes(limit):
    primes = []
    if(limit==1):
        return primes

    for i in range(2, limit+1):
        count = 0
        if i==2:
            primes.append(i)
            continue
        for j in primes:
            if i%j == 0:
                count+=1
                break
        if count==0:
            primes.append(i)
    return primes
