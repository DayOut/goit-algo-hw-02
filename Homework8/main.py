import heapq


def min_cost_to_connect_cables(cables):
    # Перетворюємо список кабелів на heap
    heapq.heapify(cables)
    total_cost = 0

    # Поки в купі більше одного кабелю
    while len(cables) > 1:
        # Виймаємо два найменші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Вартість їх з'єднання
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost


cables = [4, 3, 2, 6]
print("Мінімальні витрати на об'єднання кабелів:", min_cost_to_connect_cables(cables))