def nth_prime(n):
    primes = [2]
    i = 3
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if p * p > i:
                break
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i += 2
    return primes[-1]

print(nth_prime(10001))