from scipy.optimize import linprog

obj = [-1, -3]
#      ─┬  ─┬
#       │   └┤ Коэффициент для y
#       └────┤ Коэффициент для x

lhs_ineq = [[ 2,  1], 
            [1,  -1],  
            [ 1, -1]]  

rhs_ineq = [2,  
            0,  
            1]
           


bnd = [(0, float("inf")),  # Границы x
       (0, float("inf"))]  # Границы y

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd)

print(opt)
print("оптимальное решение: X:",max(opt.x))