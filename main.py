from data_loader import load_numbers_from_file, filter_positive_numbers
from processor import square_numbers, sum_of_squares

def main():
    """Main function that executes the workflow."""
    filename = "numbers.txt"
    numbers = load_numbers_from_file(filename)

    # Filter positive numbers
    positive_numbers = filter_positive_numbers(numbers)

    # Compute squares (extra step, not used directly)
    squared_numbers = square_numbers(positive_numbers)

    # Compute sum of squares
    total_sum = sum_of_squares(positive_numbers) 

    print(f"Sum of squares of positive numbers: {total_sum}")

if __name__ == "__main__":
    main()
