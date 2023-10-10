from scipy.optimize import linprog

obj = [-2, -3]
#      ─┬  ─┬
#       │   └┤ Коэффициент для y
#       └────┤ Коэффициент для x

lhs_ineq = [[ 1,  2], 
            [3,  1],  
            [ 2, 1]]  

rhs_ineq = [8,  
            6,  
            3]
           


bnd = [(0, float("inf")),  # Границы x
       (0, float("inf"))]  # Границы y

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              method="revised simplex")

print(opt)
print("оптимальное решение: X:",max(opt.x))