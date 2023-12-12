from pulp import *
import time

x1 = pulp.LpVariable("x1", lowBound=0, cat=LpInteger)
x2 = pulp.LpVariable("x2", lowBound=0, cat=LpInteger)
x3 = pulp.LpVariable("x3", lowBound=0, cat=LpInteger)
x4 = pulp.LpVariable("x4", lowBound=0, cat=LpInteger) #определяем переменные кол-ва товара

problem = pulp.LpProblem('0', LpMaximize) #условие на максимум

problem += 3100*x1+4200*x2+7000*x3+2000*x4, "Функция цели" #переносим матрицу
problem += 10*x1+20*x2+8*x3+15*x4<=200, "1"
problem += 20*x1+10*x2+10*x3+30*x4<=500, "2"
problem += 2*x1+3*x2+5*x3+1*x4<=30, "3"
problem.solve() #запускаем расчет

print ("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Прибыль:")
print (value(problem.objective))


