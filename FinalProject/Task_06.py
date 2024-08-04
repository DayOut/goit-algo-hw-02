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
    # Вибираємо всі можливі вартості від 0 до бюджету
    dp = [0] * (budget + 1)

    for cost in range(1, budget + 1):
        for item, info in items.items():
            if cost >= info['cost']:
                dp[cost] = max(dp[cost], dp[cost - info['cost']] + info['calories'])

    # Знаходимо оптимальний набір
    optimal_set = []
    while budget > 0:
        for item, info in items.items():
            if budget >= info['cost'] and dp[budget] == dp[budget - info['cost']] + info['calories']:
                optimal_set.append(item)
                budget -= info['cost']
                break

    return optimal_set, dp[-1]

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