def find_median(numbers):
    # sort the list of numbers in ascending order
    numbers.sort()
    # find the length of the list
    n = len(numbers)

    # check if the list has an odd or even number of elements
    if (n % 2 == 1):  # odd number of elements
        # return the middle element as the median
        return numbers[n // 2]
    else:  # even number of elements
        # calculate the average of the two middle elements as the median
        middle1 = numbers[(n // 2) - 1]
        middle2 = numbers[n // 2]
        return (middle1 + middle2) / 2


some_nums = [13, 7, -3, 82, 4]
result = find_median(some_nums)
print("Median:", result)