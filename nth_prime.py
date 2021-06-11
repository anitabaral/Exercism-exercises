#This solution requires takes brute force approach not suitable here
import math

def prime_range(number):
    primes, n= [], 2
    while number >= 1:
        primes.append(2)
        for num in range (3, n, 2):
            if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
                primes.append(num)
        if number == len(primes):
            break;
        else:
            del primes[:]
            n = n + 1
    return primes

def prime(number):
    return prime_range(number)[-1]

#A better approach by manurFR's
def prime(n):
    if n <= 0:
        raise ValueError('Number has to be greater than zero')
    primes = []
    current = 2
    while len(primes) < n:
        if not is_divisible(current, primes):
            primes.append(current)
        current += 1
    return primes[-1]


def is_divisible(current, primes):
    return any(current % p == 0 for p in primes if current >= p ** 2)
