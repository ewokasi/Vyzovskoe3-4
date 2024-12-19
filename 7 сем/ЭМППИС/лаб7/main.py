import numpy as np
import matplotlib.pyplot as plt
import time

# Заданная функция оптимизации 
def fitness_function(f):
    return sum((5 * i + 1) * (f[i] ** 2) for i in range(len(f)))

# Параметры PSO
def pso_optimization(
    n=3,                      # Размерность задачи
    population_size=20,       # Размер роя
    max_iterations=50,       # Максимальное количество итераций
    w=0.9,                    # Коэффициент инерции
    c1=0.4,                   # Когнитивный коэффициент
    c2=0.4,                   # Социальный коэффициент
    x_min=-5.12,              # Нижняя граница поиска
    x_max=5.12                # Верхняя граница поиска
):
    # Инициализация
    particles = np.random.uniform(x_min, x_max, (population_size, n))
    velocities = np.random.uniform(-0.1, 0.1, (population_size, n))
    
    personal_best_positions = np.copy(particles)
    personal_best_scores = np.array([fitness_function(p) for p in particles])
    
    global_best_position = particles[np.argmin(personal_best_scores)]
    global_best_score = np.min(personal_best_scores)
    
    # История изменений
    best_scores_history = []
    start_time = time.time()
    
    for iteration in range(max_iterations):
        for i in range(population_size):
            # Обновление скорости и позиции
            cognitive_component = c1 * np.random.rand(n) * (personal_best_positions[i] - particles[i])
            social_component = c2 * np.random.rand(n) * (global_best_position - particles[i])
            velocities[i] = w * velocities[i] + cognitive_component + social_component
            particles[i] += velocities[i]
            
            # Ограничение в пределах поиска
            particles[i] = np.clip(particles[i], x_min, x_max)
            
            # Оценка новой позиции
            fitness = fitness_function(particles[i])
            if fitness < personal_best_scores[i]:
                personal_best_scores[i] = fitness
                personal_best_positions[i] = particles[i]
        
        # Обновление глобального лучшего результата
        current_best_index = np.argmin(personal_best_scores)
        if personal_best_scores[current_best_index] < global_best_score:
            global_best_score = personal_best_scores[current_best_index]
            global_best_position = personal_best_positions[current_best_index]
        
        best_scores_history.append(global_best_score)
        
        # Визуализация для n=2
        if n == 2:
            x1, x2 = np.linspace(x_min, x_max, 200), np.linspace(x_min, x_max, 200)
            X1, X2 = np.meshgrid(x1, x2)
            Z = np.array([[fitness_function([x, y]) for x, y in zip(row_x, row_y)] for row_x, row_y in zip(X1, X2)])
            
            plt.cla()
            plt.contourf(X1, X2, Z, cmap='viridis', levels=50, alpha=0.7)
            plt.scatter(particles[1, 0], particles[1, 1], color='blue', label='Частицы', alpha=1)
            plt.scatter(particles[3:, 0], particles[3:, 1], color='red', label='Частица', alpha=0.6)
            plt.scatter(particles[2, 0], particles[2, 1], color='orange', label='Частица', alpha=1)
            plt.scatter(global_best_position[0], global_best_position[1], color='red', label='Глобальный минимум', s=100)
            plt.title(f'Итерация {iteration + 1}')
            plt.xlabel('x1')
            plt.ylabel('x2')
            plt.legend()
            plt.pause(0.1)
    
    execution_time = time.time() - start_time
    
    return global_best_position, global_best_score, best_scores_history, execution_time

# Выполнение алгоритма для n=2
best_pos, best_score, scores_history, exec_time = pso_optimization(n=2)

# Вывод результата
print(f"Найденное решение: {best_pos}")
print(f"Значение фитнес-функции: {best_score}")
print(f"Время выполнения: {exec_time:.2f} секунд")

# Построение графика изменения глобального лучшего результата
plt.figure()
plt.plot(scores_history, label='Лучший фитнес')
plt.xlabel('Итерация')
plt.ylabel('Фитнес')
plt.title('История изменения лучшего фитнеса')
plt.legend()
plt.grid()
plt.show()

# Повтор для n=3, n=5, n=10
results = []
for n_dim in [3, 5, 10]:
    print(f"Оптимизация для n={n_dim}")
    best_pos, best_score, scores_history, exec_time = pso_optimization(n=n_dim)
    results.append((n_dim, best_pos, best_score, exec_time))
    print(f"Найденное решение: {best_pos}")
    print(f"Значение фитнес-функции: {best_score}")
    print(f"Время выполнения: {exec_time:.2f} секунд")

# Сравнение результатов
print("\nСравнение времени выполнения:")
for result in results:
    print(f"n={result[0]}: Время={result[3]:.2f} секунд, Фитнес={result[2]:.6f}")
