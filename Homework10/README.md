# Порівняльний аналіз результатів обчислення інтегралу
## Результати:
- Метод Монте-Карло: 2.6482464749931163
- Аналітичне обчислення: 2.6666666666666665
- Обчислення за допомогою функції `quad`: 2.6666666666666665

## Висновки:
Результати, отримані методом Монте-Карло, аналітичним методом та за допомогою функції `quad`, 
є дуже близькими, що підтверджує правильність розрахунків. Метод Монте-Карло є ефективним для 
обчислення визначених інтегралів, особливо коли функція є складною для аналітичного інтегрування. 
Проте, він дає лише наближене значення, точність якого залежить від кількості випадкових точок. 
Аналітичний розрахунок та функція `quad` з SciPy надають більш точні результати для перевірки.