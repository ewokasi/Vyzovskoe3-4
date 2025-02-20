import numpy as np
from scipy.stats import t

# Данные
x = np.array([-3, -2, -1, 0, 3])
y = np.array([-5, -7, -5, -2, 20])

# Степени свободы
n = len(x)
k = 3  # Количество коэффициентов (a0, a1, a2)

# Матрица X для полиномиальной регрессии второй степени
X = np.vstack([np.ones(n), x, x**2]).T

# Оценки коэффициентов регрессии (a0, a1, a2)
b = np.array([-2.11250654, 4.22370487, 1.05363684])  

# Расчет остатков (ошибок)
y_pred = X.dot(b)  # Предсказанные значения
residuals = y - y_pred

# Средняя квадратичная ошибка
SQR_res = np.sum(residuals**2)
MSE_res = SQR_res / (n - k)

# Обратная матрица (X^T X)^(-1)
XTX_inv = np.linalg.inv(X.T @ X)

# Стандартные ошибки для коэффициентов
standard_errors = np.sqrt(MSE_res * np.diagonal(XTX_inv))

# t-статистики для коэффициентов
t_stats = b / standard_errors

# Степени свободы для критического значения t
df = n - k

# Критическое значение t для уровня значимости α = 0.01
t_critical = t.ppf(1 - 0.01 / 2, df)

# Проверка значимости коэффициентов
for i in range(k):
    print(f"Коэффициент a{i}: {b[i]}")
    print(f"t-статистика: {t_stats[i]}")
    print(f"Критическое значение t: {t_critical}")
    
    if abs(t_stats[i]) > t_critical:
        print(f"Коэффициент a{i} статистически значим.")
    else:
        print(f"Коэффициент a{i} не статистически значим.")
    print()
