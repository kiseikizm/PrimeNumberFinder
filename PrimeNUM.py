print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
import math

def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * limit
    for current in range(2, limit):
        if sieve[current]:
            primes.append(current)
            for multiple in range(current*current, limit, current):
                sieve[multiple] = False
    return primes

def segmented_sieve(n):
    limit = math.floor(math.sqrt(n)) + 1
    primes = sieve_of_eratosthenes(limit)

    with open('prime_numbers.txt', 'w') as f:
        for prime in primes:
            f.write(str(prime) + '\n')

        segments = range(limit, n + 1, limit)
        for low in segments:
            sieve = [True] * limit
            high = min(n, low + limit - 1)
            for prime in primes:
                start = max(prime * prime, (low // prime) * prime)
                if start < low:
                    start += prime
                for multiple in range(start, high + 1, prime):
                    sieve[multiple - low] = False
            for i in range(low, high + 1):
                if sieve[i - low]:
                    f.write(str(i) + '\n')
segmented_sieve(1000000000)  # Finds prime numbers up to 1000000000 and writes to 'prime_numbers.txt'
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
