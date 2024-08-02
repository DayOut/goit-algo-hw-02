import pulp

# Створюємо модель
model = pulp.LpProblem("Maximize_Drink_Production", pulp.LpMaximize)

# Змінні для кількості вироблених "Лимонаду" і "Фруктового соку"
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Обмеження ресурсів
water_limit = 100
sugar_limit = 50
lemon_juice_limit = 30
fruit_puree_limit = 40

# Кількість ресурсів, необхідних для виробництва одиниці продукції
water_per_lemonade = 2
sugar_per_lemonade = 1
lemon_juice_per_lemonade = 1

water_per_fruit_juice = 1
fruit_puree_per_fruit_juice = 2

# Функція цілі: максимізація загальної кількості вироблених продуктів
model += lemonade + fruit_juice, "Total_Production"

# Обмеження на ресурси
model += (water_per_lemonade * lemonade + water_per_fruit_juice * fruit_juice <= water_limit), "Water_Constraint"
model += (sugar_per_lemonade * lemonade <= sugar_limit), "Sugar_Constraint"
model += (lemon_juice_per_lemonade * lemonade <= lemon_juice_limit), "Lemon_Juice_Constraint"
model += (fruit_puree_per_fruit_juice * fruit_juice <= fruit_puree_limit), "Fruit_Puree_Constraint"

# Розв'язання моделі
model.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade: {lemonade.varValue}")
print(f"Fruit Juice: {fruit_juice.varValue}")