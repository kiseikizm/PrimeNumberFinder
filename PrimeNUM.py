print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Required library
import math

# Function to implement sieve of eratosthenes algorithm
def sieve_of_eratosthenes(limit):
    # Initialize an array to store the prime numbers
    primes = []
    # Initialize an array to mark the numbers
    sieve = [True] * limit
    # Loop through all numbers from 2 to the limit
    for current in range(2, limit):
        if sieve[current]:
            # If the current number is marked as True, then it is a prime number
            primes.append(current)
            # Mark all multiples of the current number as False
            for multiple in range(current*current, limit, current):
                sieve[multiple] = False
    # Return the list of prime numbers
    return primes

# Function to implement segmented sieve algorithm
def segmented_sieve(n):
    # Calculate the limit for the sieve of eratosthenes algorithm
    limit = math.floor(math.sqrt(n)) + 1
    # Get all prime numbers up to the limit
    primes = sieve_of_eratosthenes(limit)

    # Open the file in write mode
    with open('prime_numbers.txt', 'w') as f:
        # Write the prime numbers to the file
        for prime in primes:
            f.write(str(prime) + '\n')

        # Start the segmented sieve algorithm
        segments = range(limit, n + 1, limit)
        for low in segments:
            # Initialize an array to mark the numbers in the current segment
            sieve = [True] * limit
            # Calculate the high limit for the current segment
            high = min(n, low + limit - 1)
            for prime in primes:
                start = max(prime * prime, (low // prime) * prime)
                if start < low:
                    start += prime
                # Mark all multiples of the prime numbers as False
                for multiple in range(start, high + 1, prime):
                    sieve[multiple - low] = False
            # Write the prime numbers in the current segment to the file
            for i in range(low, high + 1):
                if sieve[i - low]:
                    f.write(str(i) + '\n')

# Call the function to find prime numbers up to 1000000000 and write them to 'prime_numbers.txt'
segmented_sieve(1000000000)

print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
