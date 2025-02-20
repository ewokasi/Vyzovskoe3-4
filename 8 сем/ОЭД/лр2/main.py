import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from scipy.stats import chi2


intervals = [(-5, -4), (-4, -3), (-3, -2), (-2, -1), (-1, 0), (0, 1), (1, 2)]
frequencies = np.array([4, 11, 31, 26, 16, 7, 5])
n = frequencies.sum()  # Общее число наблюдений

midpoints = np.array([(a + b) / 2 for a, b in intervals])

# Оценка математического ожидания и стандартного отклонения (метод моментов)
mean_empirical = np.sum(midpoints * frequencies) / n
std_empirical = np.sqrt(np.sum(frequencies * (midpoints - mean_empirical)**2) / n)

# Строим гистограмму экспериментальных данных
plt.bar(midpoints, frequencies / n, width=1, alpha=0.6, label='Эмпирическое распределение')

# Теоретическая плотность нормального распределения
x = np.linspace(-5.5, 2.5, 100)
pdf = stats.norm.pdf(x, mean_empirical, std_empirical)
plt.plot(x, pdf, 'r-', label='Теоретическая плотность')

# Проверка гипотезы хи-квадрат Пирсона
cdf_values = stats.norm.cdf([b for _, b in intervals], mean_empirical, std_empirical)
expected_probs = np.diff([0] + list(cdf_values))
expected_frequencies = expected_probs * n

# Вычисление статистики критерия хи-квадрат
chi_square_stat = np.sum((frequencies - expected_frequencies)**2 / expected_frequencies)
df = len(intervals) - 1 - 2  # Число степеней свободы (число интервалов - 1 - число оцененных параметров)
alpha = 0.025  # Уровень значимости
chi_critical = chi2.ppf(1 - alpha, df)
p_value = 1 - chi2.cdf(chi_square_stat, df)

# Вывод результатов
print(f'Эмпирическое среднее: {mean_empirical:.4f}')
print(f'Эмпирическое стандартное отклонение: {std_empirical:.4f}')
print(f'Хи-квадрат статистика: {chi_square_stat:.4f}')
print(f'Критическое значение хи-квадрат: {chi_critical:.4f}')
print(f'P-значение: {p_value:.4f}')
print('Гипотеза о нормальном распределении', 'принимается' if chi_square_stat < chi_critical else 'отклоняется')

plt.xlabel('Интервалы')
plt.ylabel('Частота')
plt.legend()
plt.grid()
plt.show()