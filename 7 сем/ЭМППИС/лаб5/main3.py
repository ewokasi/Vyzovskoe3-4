import numpy as np
import matplotlib.pyplot as plt
import time

# Новая функция оценки для трёх генов
def fitness_function(f):
    return sum((5 * i + 1) * (f[i] ** 2) for i in range(len(f)))

# Параметры эволюционной стратегии
population_size = 300          # Размер популяции
max_generations = 300          # Максимальное количество поколений
mutation_probability = 0.5     # Вероятность мутации
mutation_sigma = 0.5           # Стандартное отклонение для мутации
no_improvement_limit = 100     # Лимит поколений без улучшений для остановки

# Диапазоны для ограничений популяции
x_min_vis, x_max_vis = -5.12, 5.12

# Инициализация начальной популяции (трёхмерной)
initial_population = np.random.uniform(x_min_vis, x_max_vis, (population_size, 3))

# Начало замера времени
start_time = time.time()

best_fitness_history = []
best_solution = initial_population[0]
best_fitness = fitness_function(best_solution)

# Основной цикл эволюционной стратегии
no_improvement_count = 0

for generation in range(max_generations):
    # Оценка популяции
    fitness_values = np.array([fitness_function(ind) for ind in initial_population])

    # Поиск лучшего решения
    current_best_fitness = np.min(fitness_values)
    best_idx = np.argmin(fitness_values)

    if current_best_fitness < best_fitness:
        best_fitness = current_best_fitness
        best_solution = initial_population[best_idx]
        no_improvement_count = 0  # Сброс при улучшении
    else:
        no_improvement_count += 1  # Увеличиваем счетчик без улучшения

    best_fitness_history.append(best_fitness)

    # Проверка условия остановки
    if no_improvement_count >= no_improvement_limit:
        print(f"Остановка на поколении {generation} из-за отсутствия улучшений за {no_improvement_limit} поколений.")
        break

    # Создание новой популяции
    new_population = []
    for _ in range(population_size):
        # Выбор родителя случайным образом
        parent = initial_population[np.random.choice(population_size)]
        
        # Мутация с вероятностью
        if np.random.rand() < mutation_probability:
            child = parent + np.random.normal(0, mutation_sigma, 3)
            child = np.clip(child, x_min_vis, x_max_vis)
        else:
            child = parent
        new_population.append(child)

    initial_population = np.array(new_population)

# Окончание замера времени
end_time = time.time()
execution_time = end_time - start_time

# Вывод результатов
print(f'Лучшее найденное решение (ЭС): x1 = {best_solution[0]:.6f}, x2 = {best_solution[1]:.6f}, x3 = {best_solution[2]:.6f}')
print(f'Значение функции в этой точке (ЭС): {best_fitness:.6f}')
print(f'Время выполнения программы: {execution_time:.2f} секунд')

# История изменения лучшего фитнеса
plt.figure(figsize=(10, 6))
plt.plot(best_fitness_history, label='Лучший фитнес')
plt.title('История изменения лучшего фитнеса')
plt.xlabel('Поколение')
plt.ylabel('Фитнес')
plt.legend()
plt.grid()
plt.show()
