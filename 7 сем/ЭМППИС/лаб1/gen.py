import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(2 * x) / (x ** 2)

population_size = 30
generations = 30
mutation_rate = 0.1
mutation_chance = 0.9
x_bounds = [-20, -3.1]

population = np.random.uniform(x_bounds[0], x_bounds[1], population_size)

fitness_history = []
population_history=[]

for generation in range(generations):
    fitness = f(population)
    fitness_history.append(fitness)
    population_history.append(population)
    
    
    selected_indices = np.argsort(fitness)[-population_size // 2:]
    selected_population = population[selected_indices]
    
    offspring = []
    for i in range(len(selected_population) // 2):
        parent1 = selected_population[2 * i]
        parent2 = selected_population[2 * i + 1]
        crossover_point = np.random.rand()
        child = crossover_point * parent1 + (1 - crossover_point) * parent2
        offspring.append(child)
    
    offspring = np.array(offspring)
    if np.random.uniform(0,1)<=mutation_chance:
        mutation = np.random.uniform(-1, 1, offspring.shape) * mutation_rate
        offspring += mutation
    
    population = np.concatenate((selected_population, offspring))

def plot_generation(generation):
    print(fitness_history[generation])
    print(population_history[generation])
    plt.figure(figsize=(10, 6))
    plt.plot( population_history[generation], fitness_history[generation],'o', label=f'Поколение {generation + 1}', alpha=0.7)
    
    # Построение графика исходной функции
    x_values = np.linspace(x_bounds[0], x_bounds[1], 400)
    plt.plot(x_values, f(x_values), label='Исходная функция', color='red', linewidth=2)
    
    plt.title(f'Приспособленность индивидов в поколении {generation + 1}')
    plt.xlabel('Индивид')
    plt.ylabel('Приспособленность')
    plt.ylim(-0.5, 1)  # Установите пределы по оси Y для лучшей визуализации
    plt.legend(loc='upper right', fontsize='small')
    plt.grid()
    plt.show()


while 1:
    # Запрос ввода от пользователя
    user_input = input("Введите номер поколения (1-100) или 'all' для отображения всех поколений: ")

    if user_input.lower() == 'q':
        break
    if user_input.lower() == 'all':
        # Визуализация всех поколений на одном графике
        plt.figure(figsize=(12, 8))
        for i in range(generations):
            plt.plot(population_history[i],fitness_history[i], 'o', label=f'Поколение {i + 1}' if i < generations else "", alpha=0.5)

        # Построение графика исходной функции
        x_values = np.linspace(x_bounds[0], x_bounds[1], 400)
        plt.plot(x_values, f(x_values), label='Исходная функция', color='red', linewidth=2)

        plt.title(f'Приспособленность индивидов на протяжении {generations} поколений')
        plt.xlabel('Индивид')
        plt.ylabel('Приспособленность')
        plt.ylim(-0.5, 1)  # Установите пределы по оси Y для лучшей визуализации
        plt.legend(loc='upper right', fontsize='small')
        plt.grid()
        plt.show()
    else:
        try:
            generation_number = int(user_input) - 1  # Преобразуем в индекс (0-99)
            if 0 <= generation_number < generations:
                plot_generation(generation_number)
            else:
                print(f"Пожалуйста, введите номер поколения от 1 до {generations}.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите номер поколения или 'all'.")
