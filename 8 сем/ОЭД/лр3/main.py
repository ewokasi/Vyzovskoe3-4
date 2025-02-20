import numpy as np
import scipy.stats as stats

# Данные из таблицы
x_values = np.array([7.9, 8.6, 9.3, 9.2, 10.7, 13.4, 11.3, 10.4, 8.4, 6.2])
y_values = np.array([6.3, 10.2, 11.8, 12.3, 13.1, 11.9, 10.8, 9.9, 9.7, 4.8])

# Оценка математических ожиданий
mean_x = np.mean(x_values)
mean_y = np.mean(y_values)
std_x = np.std(x_values, ddof=1)
std_y = np.std(y_values, ddof=1)
n_x = len(x_values)
n_y = len(y_values)

# Проверка гипотезы с использованием t-критерия Стьюдента (двухвыборочный t-тест)
t_stat, p_value = stats.ttest_ind(x_values, y_values, alternative='less')

# Вывод результатов
print(f'Среднее X: {mean_x:.4f}')
print(f'Среднее Y: {mean_y:.4f}')
print(f'Стандартное отклонение X: {std_x:.4f}')
print(f'Стандартное отклонение Y: {std_y:.4f}')
print(f'T-статистика: {t_stat:.4f}')
print(f'P-значение: {p_value:.4f}')

alpha = 0.05  # Уровень значимости
if p_value < alpha:
    print('Гипотеза о равенстве математических ожиданий отвергается.')
else:
    print('Нет оснований отвергнуть гипотезу о равенстве математических ожиданий.')
