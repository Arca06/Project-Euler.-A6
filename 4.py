def is_palindrome(number):
    return str(number) == str(number)[::-1]

def largest_palindrome_product(digits):
    start = 10**(digits-1)
    end = 10**digits - 1
    largest = 0
    for i in range(end, start-1, -1):
        for j in range(i, start-1, -1):
            product = i * j
            if product > largest and is_palindrome(product):
                largest = product
    return largest

print(largest_palindrome_product(3))