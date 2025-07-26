def square_numbers(numbers):
    """Computes the square of each number in the list."""
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num * num) 
    return squared_numbers

def sum_of_squares(numbers):
    """Computes the sum of squared numbers"""
    total = 0
    for num in numbers:
        total += num * num 
    return total
