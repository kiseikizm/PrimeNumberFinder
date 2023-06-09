
# import numpy as np
#
# print("-----------------------------------")
# arr=np.array([[1,2,3,4],[2,3,5,6],[5,4,3,2]])
# for row in arr:
#     for sayi in row:
#         print(sayi, end=' ')
#     print()
# print("-----------------------------------")
# square=np.square(arr)
# for row in square:
#     for item in row:
#         print(item, end=' ')
#     print()
# print("-----------------------------------")
# arrayim = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# xd = arrayim.reshape(2, 5)
#
# for row in xd:
#     for item in row:
#         print(item, end=' ')
#     print()
# print("-----------------------------------")
# random_arr = np.random.random((3, 3))
# print(random_arr[0])
# print(random_arr[1])
# print(random_arr[2])
# print("-----------------------------------")
# arr = np.array([1, 2, 3, 4, 5])
# print("Ortalama:", int(np.mean(arr)))  # Ortalama
# print("Median:", int(np.median(arr)))  # Medyan
# print("Maksimum:", np.max(arr))  # Maksimum
# print("Minimum:", np.min(arr))  # Minimum
# print("-----------------------------------")




# print("------------------------------------------------------------------------")
# def asal_sayilari_bul(ust_limit):
#     asal_sayilar = []
#     for num in range(2, ust_limit+1):
#         if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     break
#             else:
#                 asal_sayilar.append(num)
#     return asal_sayilar
#
# asal10000=(asal_sayilari_bul(10000))  # 10000'e kadar olan asal sayıları bulur
#
# print(asal10000)
# print("------------------------------------------------------------------------")
# print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# def sieve_of_eratosthenes(n):
#     prime = [True for i in range(n+1)]
#     p = 2
#     while (p * p <= n):
#         if (prime[p] == True):
#             for i in range(p * p, n+1, p):
#                 prime[i] = False
#         p += 1
#     asal_sayilar = []
#     for p in range(2, n):
#         if prime[p]:
#             asal_sayilar.append(p)
#     return asal_sayilar
#
# print(sieve_of_eratosthenes(10000000))  # 10000000'e kadar olan asal sayıları bulur
# print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

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

segmented_sieve(1000000000)  # 1.000.000.000'a kadar olan asal sayıları bulur ve 'prime_numbers.txt' dosyasına yazar


print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
