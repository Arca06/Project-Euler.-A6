def sum_of_even_fibonacci(limit):
    result = 0
    fib1 = 1
    fib2 = 2
    while fib2 <= limit:
        if fib2 % 2 == 0:
            result += fib2
        fib1, fib2 = fib2, fib1 + fib2
    return result

print(sum_of_even_fibonacci(4000000))