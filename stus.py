import numpy as np
import matplotlib.pyplot as plt
import math as mt

from sympy import integrate, init_printing, cos, sin, pi
from sympy.abc import x # Variable de integración, equivalente a x = sp.Symbol('x')
init_printing(use_latex="mathjax")


def inProd(v,w):
    k = integrate((v*w), (x,-pi/2,pi/2))
    return k


# INPUTS
# ------
'''
V = ['Vectors of n coordinates', 'Arrays of m rows and n columns', 'Grade n polynomials', 'Locally integrable functions']
S = ['Standard basis', 'Trigonometric polynomials', 'Custom basis']
v = ['Step', 'Ramp', ]


print('Define V:\n') # Definición de V

for V_i in range(0,len(V),1):
    print(f'({V_i+1}) {V[V_i]}')

V_i = len(V)

while V_i != 3: # provisorio
    V_i = int(input('Select vector space: ')) - 1

print(f'V = {V[V_i]}\n')


print('Define S:\n') # Definición de S

for S_i in range(0,len(S),1):
    print(f'({S_i+1}) {S[S_i]}')

S_i = len(S)

while S_i != 1: # provisorio
    S_i = int(input('Select subspace: ')) - 1

print(f'S = {S[S_i]}\n')
'''

dim_S = int(21) # Dimensión del subespacio

f = x**0 # Función a proyectar

f_s = 20 # Sample rate
a = -np.pi # Inicio del intervalo
b = np.pi # Final del intervalo
closedInterval = True # Cerrar intervalo con el mayorante


# ORTHOGONAL BASE
# ---------------

B_trig = np.array([1]) # Base ortogonal de S

for v_i in range(1,int(mt.ceil(dim_S/2)),1): # Genera la base B
    B_trig = np.append(B_trig, sin((v_i)*x))
    B_trig = np.append(B_trig, cos((v_i)*x))

if dim_S%2 == 0:
    B_trig = np.append(B_trig, sin(int(dim_S/2)*x))

print('B =', B_trig)

B = B_trig


# PROJECTION
# ----------

proy = 0

for a_i in range(0,int(dim_S),1):
    proy = proy + (inProd(f,B[a_i])/inProd(B[a_i],B[a_i]))*B[a_i]

print('proy_S(f) = ', proy)


# GRAPHS
# ------

t = np.arange(a,b+int(closedInterval)/f_s,1/f_s)
x_axis = []
y_axis = []
y_axis_f = []

for t_i in t:
    x_axis.append(t_i)
    y_axis.append(proy.subs(x,t_i))
    y_axis_f.append(f.subs(x,t_i))

plt.plot(x_axis,y_axis,"-y")
plt.plot(x_axis,y_axis_f,"-r")
plt.grid

















































































