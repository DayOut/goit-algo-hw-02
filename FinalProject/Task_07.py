import random
import matplotlib.pyplot as plt
from collections import defaultdict


def simulate_dice_rolls(num_rolls):
    results = defaultdict(int)

    # Симуляція кидків
    for step in range(num_rolls):
        print(f"Current step: {step}", end="\r")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        results[dice1 + dice2] += 1

    # Обчислення ймовірностей
    probabilities = {sum_: count / num_rolls for sum_, count in results.items()}

    return probabilities


# Введіть кількість кидків
num_rolls = 1000000
probabilities = simulate_dice_rolls(num_rolls)

# Виведення результатів
for sum_, prob in sorted(probabilities.items()):
    print(f"Сума: {sum_}, Ймовірність: {(prob*100):.2f}% ({prob:.4f})")

# Сортування сум і відповідних ймовірностей
sums = sorted(probabilities.keys())
prob_values = [probabilities[sum_] for sum_ in sums]

# Графічне відображення результатів
plt.figure(figsize=(10, 6))
plt.bar(sums, prob_values, color='skyblue')
plt.xlabel('Сума чисел на кубиках')
plt.ylabel('Ймовірність')
plt.title('Ймовірність сум чисел на двох кубиках (Метод Монте-Карло)')
plt.xticks(sums)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()