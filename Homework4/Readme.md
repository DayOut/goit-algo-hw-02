# Порівняльний аналіз алгоритмів сортування

## Вступ
В даній роботі виконано порівняльний аналіз трьох алгоритмів сортування: сортування злиттям, 
сортування вставками та Timsort. Аналіз проведено шляхом тестування алгоритмів на різних наборах 
даних, що дозволило емпірично перевірити теоретичні оцінки їх складності.

## Методологія
Для порівняння було використано наступні алгоритми сортування: 
- **Merge Sort** (Сортування злиттям)
- **Insertion Sort** (Сортування вставками)
- **Timsort** (Вбудований алгоритм сортування в Python, що поєднує сортування злиттям та сортування 
- вставками)

Вимірювання часу виконання алгоритмів проводилося за допомогою модуля **timeit** на наборах даних 
розміром 1000, 5000, 10000, 20000 та 30000 елементів. Для кожного набору відбувалось 10 ітерацій, для отримання 
середніх значень і зменшення похибки разового сортування

## Результати
### Емпіричні дані
```
Array Size: 1000
Merge Sort Time: 0.012843 seconds
Insertion Sort Time: 0.136411 seconds
Timsort Time: 0.000568 seconds

Array Size: 5000
Merge Sort Time: 0.051113 seconds
Insertion Sort Time: 3.134921 seconds
Timsort Time: 0.003709 seconds

Array Size: 10000
Merge Sort Time: 0.110315 seconds
Insertion Sort Time: 11.752913 seconds
Timsort Time: 0.008340 seconds

Array Size: 20000
Merge Sort Time: 0.238325 seconds
Insertion Sort Time: 46.053736 seconds
Timsort Time: 0.018514 seconds

Array Size: 30000
Merge Sort Time: 0.381422 seconds
Insertion Sort Time: 104.015965 seconds
Timsort Time: 0.029004 seconds
```
### Аналіз результатів
```
For array of size 1000:
Merge Sort is 10.62 times faster than Insertion Sort
Timsort is 240.04 times faster than Insertion Sort
Timsort is 22.60 times faster than Merge Sort

For array of size 5000:
Merge Sort is 61.33 times faster than Insertion Sort
Timsort is 845.33 times faster than Insertion Sort
Timsort is 13.78 times faster than Merge Sort

For array of size 10000:
Merge Sort is 106.54 times faster than Insertion Sort
Timsort is 1409.16 times faster than Insertion Sort
Timsort is 13.23 times faster than Merge Sort

For array of size 20000:
Merge Sort is 193.24 times faster than Insertion Sort
Timsort is 2487.45 times faster than Insertion Sort
Timsort is 12.87 times faster than Merge Sort

For array of size 30000:
Merge Sort is 272.71 times faster than Insertion Sort
Timsort is 3586.21 times faster than Insertion Sort
Timsort is 13.15 times faster than Merge Sort
```
## Висновки
Емпіричні дані підтверджують теоретичні оцінки складності алгоритмів. Поєднання сортування злиттям і 
сортування вставками робить алгоритм Timsort набагато ефективнішим, ніж окреме використання сортування 
злиттям або вставками. Саме тому Timsort використовується як вбудований алгоритм сортування в Python.

Зокрема, Timsort показує значно кращі результати на всіх наборах даних, що підтверджує його ефективність 
для реальних застосувань. 