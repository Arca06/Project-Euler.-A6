def largest_prime_factor(number):
    i = 2
    while i * i <= number:
        while number % i == 0:
            number = number // i
        i += 1
    return number

print(largest_prime_factor(600851475143))