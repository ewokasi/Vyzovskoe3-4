import numpy as np

# Данные
x = np.array([-3, -2, -1, 0, 3])
y = np.array([-5, -7, -5, -2, 20])

# Вычисление сумм для системы нормальных уравнений
n = len(x)
sum_x = np.sum(x)
sum_x2 = np.sum(x**2)
sum_x3 = np.sum(x**3)
sum_x4 = np.sum(x**4)
sum_y = np.sum(y)
sum_x_y = np.sum(x * y)
sum_x2_y = np.sum(x**2 * y)

# Составляем матрицу A и вектор Y
A = np.array([[n, sum_x, sum_x2],
              [sum_x, sum_x2, sum_x3],
              [sum_x2, sum_x3, sum_x4]])

Y = np.array([sum_y, sum_x_y, sum_x2_y])

# Решение матричного уравнения для коэффициентов регрессии
b = np.linalg.inv(A).dot(Y)

# Выводим коэффициенты
print(b)
