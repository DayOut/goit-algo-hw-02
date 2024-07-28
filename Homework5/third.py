import timeit

#region algs
def build_shift_table(pattern):
    """Створити таблицю зсувів для алгоритму Боєра-Мура."""
    table = {}
    length = len(pattern)
    # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    # Створюємо таблицю зсувів для патерну (підрядка)
    shift_table = build_shift_table(pattern)
    i = 0  # Ініціалізуємо початковий індекс для основного тексту

    # Проходимо по основному тексту, порівнюючи з підрядком
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # Починаємо з кінця підрядка

        # Порівнюємо символи від кінця підрядка до його початку
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  # Зсуваємось до початку підрядка

        # Якщо весь підрядок збігається, повертаємо його позицію в тексті
        if j < 0:
            return i  # Підрядок знайдено

        # Зсуваємо індекс i на основі таблиці зсувів
        # Це дозволяє "перестрибувати" над неспівпадаючими частинами тексту
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    # Якщо підрядок не знайдено, повертаємо -1
    return -1


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено


def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(main_string, substring):
    # Довжини основного рядка та підрядка пошуку
    substring_length = len(substring)
    main_string_length = len(main_string)

    # Базове число для хешування та модуль
    base = 256
    modulus = 101

    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_length - 1) % modulus

    # Проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1
#endregion

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Зчитування статей
article1 = read_file('Homework5/article1.txt')
article2 = read_file('Homework5/article2.txt')

# Пошук підрядків
existing_substring1 = 'розглянемо проблему виплати'
non_existing_substring1 = 'неіснуючий рядок'

existing_substring2 = 'відмінність у часі генерації сесій'
non_existing_substring2 = 'nonexistent substring'

# Вимірювання часу виконання
time_boyer_moore_1 = timeit.timeit(lambda: boyer_moore_search(article1, existing_substring1), number=10)
time_boyer_moore_2 = timeit.timeit(lambda: boyer_moore_search(article2, existing_substring2), number=10)
time_boyer_moore_non_1 = timeit.timeit(lambda: boyer_moore_search(article1, non_existing_substring1), number=10)
time_boyer_moore_non_2 = timeit.timeit(lambda: boyer_moore_search(article2, non_existing_substring2), number=10)

time_kmp_1 = timeit.timeit(lambda: kmp_search(article1, existing_substring1), number=10)
time_kmp_2 = timeit.timeit(lambda: kmp_search(article2, existing_substring2), number=10)
time_kmp_non_1 = timeit.timeit(lambda: kmp_search(article1, non_existing_substring1), number=10)
time_kmp_non_2 = timeit.timeit(lambda: kmp_search(article2, non_existing_substring2), number=10)

time_rabin_karp_1 = timeit.timeit(lambda: rabin_karp_search(article1, existing_substring1), number=10)
time_rabin_karp_2 = timeit.timeit(lambda: rabin_karp_search(article2, existing_substring2), number=10)
time_rabin_karp_non_1 = timeit.timeit(lambda: rabin_karp_search(article1, non_existing_substring1), number=10)
time_rabin_karp_non_2 = timeit.timeit(lambda: rabin_karp_search(article2, non_existing_substring2), number=10)

# Виведення результатів
print("Boyer-Moore для статті 1 (існуючий):", time_boyer_moore_1)
print("Boyer-Moore для статті 1 (неіснуючий):", time_boyer_moore_non_1)
print("Boyer-Moore для статті 2 (існуючий):", time_boyer_moore_2)
print("Boyer-Moore для статті 2 (неіснуючий):", time_boyer_moore_non_2)

print("KMP для статті 1 (існуючий):", time_kmp_1)
print("KMP для статті 1 (неіснуючий):", time_kmp_non_1)
print("KMP для статті 2 (існуючий):", time_kmp_2)
print("KMP для статті 2 (неіснуючий):", time_kmp_non_2)

print("Rabin-Karp для статті 1 (існуючий):", time_rabin_karp_1)
print("Rabin-Karp для статті 1 (неіснуючий):", time_rabin_karp_non_1)
print("Rabin-Karp для статті 2 (існуючий):", time_rabin_karp_2)
print("Rabin-Karp для статті 2 (неіснуючий):", time_rabin_karp_non_2)

# Визначення найшвидшого алгоритму для кожного тексту та в цілому
fastest_1 = min(time_boyer_moore_1, time_kmp_1, time_rabin_karp_1)
fastest_2 = min(time_boyer_moore_2, time_kmp_2, time_rabin_karp_2)
fastest_non_1 = min(time_boyer_moore_non_1, time_kmp_non_1, time_rabin_karp_non_1)
fastest_non_2 = min(time_boyer_moore_non_2, time_kmp_non_2, time_rabin_karp_non_2)

# Визначення найшвидшого алгоритму для кожного тексту та в цілому
def get_fastest_algorithm(times, algorithms):
    min_time = min(times)
    index = times.index(min_time)
    return algorithms[index], min_time

algorithms = ["Boyer-Moore", "KMP", "Rabin-Karp"]

fastest_1, time_1 = get_fastest_algorithm([time_boyer_moore_1, time_kmp_1, time_rabin_karp_1], algorithms)
fastest_2, time_2 = get_fastest_algorithm([time_boyer_moore_2, time_kmp_2, time_rabin_karp_2], algorithms)
fastest_non_1, time_non_1 = get_fastest_algorithm([time_boyer_moore_non_1, time_kmp_non_1, time_rabin_karp_non_1], algorithms)
fastest_non_2, time_non_2 = get_fastest_algorithm([time_boyer_moore_non_2, time_kmp_non_2, time_rabin_karp_non_2], algorithms)

print("Найшвидший алгоритм для статті 1 (існуючий):", fastest_1, "з часом:", time_1)
print("Найшвидший алгоритм для статті 1 (неіснуючий):", fastest_non_1, "з часом:", time_non_1)
print("Найшвидший алгоритм для статті 2 (існуючий):", fastest_2, "з часом:", time_2)
print("Найшвидший алгоритм для статті 2 (неіснуючий):", fastest_non_2, "з часом:", time_non_2)

overall_fastest_existing, overall_time_existing = get_fastest_algorithm([time_1, time_2], [f"Article 1 ({fastest_1})", f"Article 2 ({fastest_2})"])
overall_fastest_non_existing, overall_time_non_existing = get_fastest_algorithm([time_non_1, time_non_2], [f"Article 1 ({fastest_1})", f"Article 2 ({fastest_2})"])

print("Найшвидший алгоритм в цілому (існуючий):", overall_fastest_existing, "з часом:", overall_time_existing)
print("Найшвидший алгоритм в цілому (неіснуючий):", overall_fastest_non_existing, "з часом:", overall_time_non_existing)