import random
import timeit

iteration = 0

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Реалізація сортування вставками
def insertion_sort(arr):
    global iteration
    for i in range(1, len(arr)):
        print(f"\r(iteration {iteration}) Processing insertion sort: {i}/{len(arr)}", end="")
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    iteration += 1
    print("\r", end="")

# Функція для вимірювання часу сортування
def measure_time(sort_func, data):
    def wrapper():
        sort_func(data.copy())
    return wrapper

# Генерація випадкових даних
sizes = [1000, 5000, 10000, 20000, 30000]
results = []

for size in sizes:
    print(f"Processing size:\t{size}\r", end="")
    data = [random.randint(0, size) for _ in range(size)]
    print(f"Generated data size:\t{size}\r", end="")
    iteration = 0
    merge_time = timeit.timeit(measure_time(merge_sort, data), number=10)
    print(f"Finished sorting via merge sort: {merge_time}\r", end="")
    iteration = 0
    insertion_time = timeit.timeit(measure_time(insertion_sort, data), number=10)
    print(f"Finished sorting via insertion sort: {insertion_time}\r", end="")
    iteration = 0
    timsort_time = timeit.timeit(measure_time(sorted, data), number=10)
    print(f"Finished sorting via Timsort: {timsort_time}\r", end="")

    results.append((size, merge_time, insertion_time, timsort_time))
    print((" " * 60) + "\r", end="")

# Виведення результатів
for result in results:
    print(f"Array Size: {result[0]}")
    print(f"Merge Sort Time: {result[1]:.6f} seconds")
    print(f"Insertion Sort Time: {result[2]:.6f} seconds")
    print(f"Timsort Time: {result[3]:.6f} seconds")
    print()

# Аналіз результатів
for result in results:
    size, merge_time, insertion_time, timsort_time = result
    print(f"For array of size {size}:")
    print(f"Merge Sort is {insertion_time / merge_time:.2f} times faster than Insertion Sort")
    print(f"Timsort is {insertion_time / timsort_time:.2f} times faster than Insertion Sort")
    print(f"Timsort is {merge_time / timsort_time:.2f} times faster than Merge Sort")
    print()