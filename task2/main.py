def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_target = None

    while left <= right:
        iterations += 1
        middle = left + (right - left) // 2
        middle_value = arr[middle]

        if middle_value == target:
            return (iterations, middle_value)
        elif middle_value < target:
            left = middle + 1
        else:
            upper_target = middle_value
            right = middle - 1

    return (iterations, upper_target)