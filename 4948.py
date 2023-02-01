import math

while True:
    n = int(input())
    if n == 0:
        break

    a = [False, False] + [True] * (2 * n-1)
    primes = []

    for i in range(2, 2*n+1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, 2 * n + 1, i):
                a[j] = False

    for j in primes:
        if j > n:
            idx = primes.index(j)
            print(len(primes[idx:]))
            break





