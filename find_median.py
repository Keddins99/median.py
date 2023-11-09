def find_median(numbers):
    if not numbers:
        return None

    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    if length % 2 == 1:
        return sorted_numbers[length // 2]
    else:
        mid1 = sorted_numbers[length // 2 - 1]
        mid2 = sorted_numbers[length // 2]
        return (mid1 + mid2) / 2



values = [13, 7, -3, 82, 4]
result = find_median(values)
print("Result is:", result)  # Output: Result is: 7
