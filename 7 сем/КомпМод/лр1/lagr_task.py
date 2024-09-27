# this code requires SymPy v1.4
# следующие две строки не нужны при запуске кода на live.sympy.org
from sympy import init_printing, sin

init_printing()

from sympy import Symbol, Function, Derivative, dsolve, solve
x = Symbol('x')
y = Function('y')(x)
dy = Derivative(y)

F = dy+y**2+2*y*sin(x)
F.doit() # выводиим выражение в человекочитаемом формате ...
print(F) # ... и в машиночитаемом виде
dFdy = Derivative(F, y)
dFd1y = Derivative(F, dy)
dFdy.doit() 
dFd1y.doit()
L = dFdy - Derivative(dFd1y, x)
sol = dsolve(L)
eq1 = sol.subs({x:0, y:1})
eq2 = sol.subs({x:1, y:4})
coeffs = solve([eq1, eq2])
res = sol.subs(coeffs)
print(res.doit())