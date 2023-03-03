import math

def smallest_multiple(limit):
    result = 1
    for i in range(2, limit+1):
        result *= i // math.gcd(i, result)
    return result

print(smallest_multiple(20))