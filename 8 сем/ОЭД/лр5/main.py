import numpy as np
import scipy.stats as stats

# Данные
x1 = np.array([-4, -1, 0, 2, 1, -2])
x2 = np.array([-3, -2, 2, 3, 4, -1])
y = np.array([-16, -3, -3, 5, -2, -9])

# Центрирование данных
x1_centered = x1 - np.mean(x1)
x2_centered = x2 - np.mean(x2)
y_centered = y - np.mean(y)

print("Отцентрованные данные:")
print(x1_centered)
print(x2_centered)
print(y_centered)
print()

# Составляем матрицу X с добавлением столбца для свободного члена
X = np.column_stack((np.ones(len(x1_centered)), x1_centered, x2_centered))  # столбец для 1 (свободный член)
Y = y_centered
print("Матрица X и вектор Y")
print(X)
print(Y)
print()


# Матричное уравнение для нахождения коэффициентов
X_transpose = X.T
beta = np.linalg.inv(X_transpose @ X) @ X_transpose @ Y

# Предсказания и остатки
y_pred = X @ beta
residuals = Y - y_pred

# Средняя квадратическая ошибка регрессии (MSR)
MSR = np.sum((y_pred - np.mean(y))**2) / (X.shape[1] - 1)

# Средняя квадратическая ошибка (MSE)
MSE = np.sum(residuals**2) / (len(y) - X.shape[1])

# Статистика Фишера
F_stat = MSR / MSE
F_critical = stats.f.ppf(1 - 0.05, X.shape[1] - 1, len(y) - X.shape[1])
print("Статистика Фишера", F_stat)
print("Критическая Фишера", F_critical)
print()
# Стандартные ошибки коэффициентов
se_beta = np.sqrt(MSE * np.diagonal(np.linalg.inv(X_transpose @ X)))

# t-статистики и p-значения
t_stats = beta / se_beta
p_values = 2 * (1 - stats.t.cdf(np.abs(t_stats), df=len(y) - X.shape[1]))

# Выводим t-статистики и p-значения
print("t-статистики:", t_stats)
print("p-значения:", p_values)
print()
# Исключаем незначимые факторы (с p-значением > 0.05)
significant_factors = p_values < 0.05
X_significant = X[:, significant_factors]

# Пересчитываем коэффициенты с учетом значимых факторов
beta_significant = np.linalg.inv(X_significant.T @ X_significant) @ X_significant.T @ Y

# Повторная проверка адекватности после исключения незначимых факторов
y_pred_significant = X_significant @ beta_significant
residuals_significant = Y - y_pred_significant

# Средняя квадратическая ошибка регрессии (MSR) для значимых факторов
MSR_significant = np.sum((y_pred_significant - np.mean(y))**2) / (X_significant.shape[1] - 1)

# Средняя квадратическая ошибка (MSE) для значимых факторов
MSE_significant = np.sum(residuals_significant**2) / (len(y) - X_significant.shape[1])

# Статистика Фишера для значимых факторов
F_stat_significant = MSR_significant / MSE_significant
F_critical_significant = stats.f.ppf(1 - 0.05, X_significant.shape[1] - 1, len(y) - X_significant.shape[1])

# Вывод результатов
print("Коэффициенты регрессии для значимых факторов:", beta_significant)
print(f"Статистика Фишера после исключения незначимых факторов: {F_stat_significant:.4f}")
print(f"Критическое значение F для значимых факторов: {F_critical_significant:.4f}")
