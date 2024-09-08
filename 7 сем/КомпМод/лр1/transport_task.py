import pulp

# Данные о запасах на складах
supply = [15, 25, 20]  # w1, w2, w3
warehouses = ['W1', 'W2', 'W3']

# Данные о потребностях в магазинах
demand = [20, 12, 5, 9]  # m1, m2, m3, m4
stores = ['M1', 'M2', 'M3', 'M4']

# Стоимость перевозки
cost = {
    ('W1', 'M1'): 2, ('W1', 'M2'): 2, ('W1', 'M3'): 2, ('W1', 'M4'): 4,
    ('W2', 'M1'): 3, ('W2', 'M2'): 1, ('W2', 'M3'): 1, ('W2', 'M4'): 3,
    ('W3', 'M1'): 3, ('W3', 'M2'): 6, ('W3', 'M3'): 3, ('W3', 'M4'): 4,
}

problem = pulp.LpProblem("Transportation_Problem", pulp.LpMinimize)

# Переменные: количество кроватей, которые будут перевезены со склада в магазин
x = pulp.LpVariable.dicts("x", [(w, s) for w in warehouses for s in stores], lowBound=0, cat='Continuous')

# Целевая функция: минимизация стоимости перевозки
problem += pulp.lpSum(cost[(w, s)] * x[(w, s)] for w in warehouses for s in stores), "Total_Cost"

# Ограничения по запасам на складах
for i, w in enumerate(warehouses):
    problem += pulp.lpSum(x[(w, s)] for s in stores) <= supply[i], f"Supply_Constraint_{w}"

# Ограничения по потребностям в магазинах
for j, s in enumerate(stores):
    problem += pulp.lpSum(x[(w, s)] for w in warehouses) >= demand[j], f"Demand_Constraint_{s}"

# Решение задачи
problem.solve()

# Вывод результатов

print("Оптимальное распределение кроватей:")
for w in warehouses:
    for s in stores:
        print(f"Склад {w} -> Магазин {s}: {x[(w, s)].varValue} кроватей")

print("Минимальная стоимость перевозки:", pulp.value(problem.objective))
