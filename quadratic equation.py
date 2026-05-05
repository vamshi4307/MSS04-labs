#python code for solving a quadratic equation 
import cmath

def q_solve(a, b, c):
    if a == 0:
        return "Not a quadratic equation"
    
    D = b**2 - 4*a*c
    
    x1 = (-b + cmath.sqrt(D)) / (2*a)
    x2 = (-b - cmath.sqrt(D)) / (2*a)
    
    return x1, x2