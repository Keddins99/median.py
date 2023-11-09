def find_median(numbers: list) -> float:
    if not numbers:
        return None

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        # If the number of elements is even, calculate the average of the middle two numbers
        mid_left = sorted_numbers[n // 2 - 1]
        mid_right = sorted_numbers[n // 2]
        median = (mid_left + mid_right) / 2
    else:
        # If the number of elements is odd, the median is the middle number
        median = sorted_numbers[n // 2]

    return median

# Example usage
if __name__ == "__main__":
    values = [13, 7, -3, 82, 4]
    result = find_median(values)
    print(result)
