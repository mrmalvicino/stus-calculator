import numpy as np
import matplotlib.pyplot as plt

import sympy as sp
from sympy import integrate, init_printing, cos, sin, pi
from sympy.abc import x # Variable de integración, equivalente a x = sp.Symbol('x')
init_printing(use_latex="mathjax")

def intProd(v,w):
    a = integrate((v*w), (x,-pi,pi))
    return a

f = x*x # Función a proyectar, definida por el usuario
dim_S = int(7) # Dimensión del espacio de polinomios trigonométricos, definido por usuario

B = np.array([1]) # Base ortogonal de S
B_sin = np.array([]) # Base de senos
B_cos = np.array([]) # Base de cosenos

for v_i in range(0,int((dim_S-1)/2),1): # Genera la base B
    B_sin = np.append(B_sin, sin((v_i+1)*x))
    B_cos = np.append(B_cos, cos((v_i+1)*x))
    B = np.append(B,B_sin[v_i])
    B = np.append(B,B_cos[v_i])

print('B =', B)

proy = intProd(f,1)/intProd(1,1)

for a_i in range(0,int((dim_S-1)/2),1):
    proy = proy + (intProd(f,B[a_i])/intProd(B[a_i],B[a_i]))*B[a_i]

print('proy_S(f) = ', proy)














#plt.plot(x,proy,"-o")
#plt.grid