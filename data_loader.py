def load_numbers_from_file(filename):
    """Reads numbers from a file and returns a list."""
    numbers = []
    with open(filename, "r") as file:
        for line in file:
            numbers.append(int(line.strip())) 
    return numbers

def filter_positive_numbers(numbers):
    """Filters out non-positive numbers using a manual loop."""
    positive_numbers = []
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)  
    return positive_numbers
