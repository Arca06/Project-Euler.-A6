def sum_of_multiples(limit, divisors):
    return sum(x for x in range(limit) if any(x % div == 0 for div in divisors))

print(sum_of_multiples(1000, [3, 5]))