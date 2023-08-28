def is_even(number):
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# values come in streams which can only be accessed once

even_numbers = list(filter(is_even, numbers))

print(even_numbers)
