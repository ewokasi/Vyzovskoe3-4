import numpy as np
from matplotlib import pyplot as plt

def generate_poisson_process(lmbda, T):
    T0 = 0
    events = []
    
    while True:
        xi = np.random.rand()
        t_i = -np.log(xi) / lmbda
        
        if len(events) == 0:
            T_j = T0 + t_i
        else:
            T_j = events[-1] + t_i
        
        if T_j > T:
            break 

        events.append(T_j)
    return events


N=34
T=N
T2= N+100
lam1 = (N+8)/(N+24)
lam2 = (N+9)/(N+25)

T = T2-T  
print(f"Теоретические lam1 и lam2: {lam1, lam2}")


poisson_events1 = generate_poisson_process(lam1, T)
poisson_events2 = generate_poisson_process(lam2, T)
sum_events = np.sort(np.concatenate((poisson_events1, poisson_events2)))

print(f"Практические lam1 и lam2: {len(poisson_events1)/T, len(poisson_events2)/T}")


import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))

# График 1: Первый пуассоновский процесс
plt.subplot(311)
plt.scatter(poisson_events1, y=[0]*len(poisson_events1), color='b')
plt.title('Пуассоновский процесс 1')
plt.xlim(0, T)
plt.xlabel('Время')
plt.ylabel('События')

# График 2: Второй пуассоновский процесс
plt.subplot(312)
plt.scatter(poisson_events2, y=[0]*len(poisson_events2), color='r')
plt.title('Пуассоновский процесс 2')
plt.xlim(0, T)
plt.xlabel('Время')
plt.ylabel('События')

# Наложенный график
plt.subplot(313)
plt.scatter(poisson_events1, y=[0]*len(poisson_events1), alpha=0.5, color='b', label='Процесс 1')
plt.scatter(poisson_events2, y=[0]*len(poisson_events2), alpha=0.5, color='r', label='Процесс 2')
plt.title('Наложенные пуассоновские процессы')
plt.xlim(0, T)
plt.xlabel('Время')
plt.ylabel('События')
plt.legend()

plt.tight_layout()
plt.show()

