def sum_square_difference(limit):
    sum_of_squares = sum(i**2 for i in range(1, limit+1))
    square_of_sum = sum(i for i in range(1, limit+1))**2
    return square_of_sum - sum_of_squares

print(sum_square_difference(100))