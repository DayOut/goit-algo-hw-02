def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        if arr[mid] == target:
            upper_bound = arr[mid]
            return (iterations, upper_bound)
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    if upper_bound is None:
        upper_bound = arr[left] if left < len(arr) else None

    return (iterations, upper_bound)

# Приклад використання
sorted_array = [1.1, 2.3, 3.5, 4.8, 6.7, 8.9]
target_value = 5.0
result = binary_search(sorted_array, target_value)
print(result)