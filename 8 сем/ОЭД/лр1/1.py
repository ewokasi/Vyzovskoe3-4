import math
import pandas as pd
from scipy.stats import norm

# Данные
arr = [1.3, 1.8, 3.2, 4.5, 6.7, 8.1, 7.8, 5.9, 4.3, 3.4, 1.7, 1]
df = pd.DataFrame(arr, columns=["Value"])
df.reset_index(drop=True, inplace=True)

# 1. Оценка математического ожидания (среднее)
avg = df["Value"].mean()
print("Матожидание:", avg)

# 2. Доверительный интервал (95% -> коэффициент 1.96 для нормального распределения)
std = df["Value"].std(ddof=1)  # Выборочное стандартное отклонение
print("Среднее квадратическое отклонение:", std)

dov_int = [avg - 2 * std, avg + 2 * std]
print("95% доверительный интервал:", dov_int)

# 3. Отсеивание аномальных значений
filtered_values = [x for x in arr if dov_int[0] <= x <= dov_int[1]]

if len(filtered_values) < len(arr):
    print("Аномальные значения:", set(arr) - set(filtered_values))
else:
    print("Аномальных значений не найдено")

# 4. Уточнённая оценка математического ожидания после отсеивания
filtered_avg = sum(filtered_values) / len(filtered_values)
print("Уточнённое матожидание:", filtered_avg)

# 5. Проверка качества оценивания
# Доверительный интервал для уточнённого математического ожидания
filtered_std = pd.Series(filtered_values).std(ddof=1)  # Новое стандартное отклонение
n = len(filtered_values)  # Новое количество значений

confidence_level = 0.99  # Заданная доверительная вероятность
t_value = 2.576  # Значение для 99% доверительного уровня

quality_error = (filtered_std * t_value) / math.sqrt(n)
interval = [filtered_avg - quality_error, filtered_avg + quality_error]

print("Качество оценивания:", quality_error)
print("Доверительный интервал для матожидания с учётом качества:", interval)


epsilon = 0.14
df["Z-score"] = (epsilon * math.sqrt(n)) / filtered_std
df["P-confidence"] = norm.cdf(df["Z-score"]) - norm.cdf(-df["Z-score"])
print(f"Доверительная вероятность для погрешности {epsilon}: {df['P-confidence'].iloc[0]:.4f}")
# Вывод результата

