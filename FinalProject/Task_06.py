def greedy_algorithm(items, budget):
    # Сортуємо елементи за співвідношенням калорії/вартість
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []

    for item, info in sorted_items:
        if budget >= info['cost']:
            selected_items.append(item)
            total_calories += info['calories']
            budget -= info['cost']

    return selected_items, total_calories

def dynamic_programming(items, budget):
    # Створюємо список страв з їхніми витратами та калорійністю
    item_list = [(name, details['cost'], details['calories']) for name, details in items.items()]

    dp = [[0] * (budget + 1) for _ in range(len(item_list) + 1)]

    # Заповнюємо dp таблицю
    for i in range(1, len(item_list) + 1):
        name, cost, calories = item_list[i - 1]
        for j in range(budget + 1):
            if j >= cost:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
            else:
                dp[i][j] = dp[i - 1][j]

    # Визначаємо набір предметів, які дають максимальну калорійність
    result = []
    j = budget
    for i in range(len(item_list), 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            name, cost, calories = item_list[i - 1]
            result.append(name)
            j -= cost

    return result, dp[len(item_list)][budget]

items = {
    "pizza": {"cost": 50, "calories": 300}, # 6 calories per cent
    "hamburger": {"cost": 40, "calories": 250}, # 6.25
    "hot-dog": {"cost": 30, "calories": 200}, # 6.67
    "pepsi": {"cost": 10, "calories": 100}, # 10
    "cola": {"cost": 15, "calories": 220}, # 14.67
    "potato": {"cost": 25, "calories": 350} # 14
}

budget = 100
selected_items, total_calories = greedy_algorithm(items, budget)
print(f"[Greedy Algorithm] Selected items: {selected_items}, total calories: {total_calories}")

selected_items, total_calories = dynamic_programming(items, budget)
print(f"[Dynamic Algorithm] Selected items: {selected_items}, total calories: {total_calories}")