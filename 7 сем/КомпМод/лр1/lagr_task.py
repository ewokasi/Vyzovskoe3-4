# this code requires SymPy v1.4
# следующие две строки не нужны при запуске кода на live.sympy.org
from sympy import init_printing, sin
import numpy as np

init_printing()

from sympy import Symbol, Function, Derivative, dsolve, solve
x = Symbol('x')
y = Function('y')(x)
dy = Derivative(y)

F = (y-(1/2)*y**2)*sin(x)
F.doit() # выводиим выражение в человекочитаемом формате ...
print(F) # ... и в машиночитаемом виде
dFdy = Derivative(F, y)
dFd1y = Derivative(F, dy)
dFdy.doit() 
dFd1y.doit()
L = dFdy - Derivative(dFd1y, x)
sol = dsolve(L)
eq1 = sol.subs({x:np.pi/4, y:-np.log(np.sqrt(2))})
eq2 = sol.subs({x:np.pi/2, y:0})
coeffs = solve([eq1, eq2])
res = sol.subs(coeffs)
print(res.doit())