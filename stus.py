import numpy as np
import matplotlib.pyplot as plt

from sympy import integrate, init_printing, cos, sin, pi
from sympy.abc import x # Variable de integración, equivalente a x = sp.Symbol('x')
init_printing(use_latex="mathjax")


def intProd(v,w):
    a = integrate((v*w), (x,-pi,pi))
    return a


# INPUTS
# ------

f = x**3 # Función a proyectar
dim_S = int(40) # Dimensión del subespacio
resolution = 0.05 # Error en el gráfico

# ORTHOGONAL BASE
# ---------------

B = np.array([1]) # Base ortogonal de S
B_sin = np.array([]) # Base de senos
B_cos = np.array([]) # Base de cosenos

for v_i in range(0,int((dim_S-1)/2),1): # Genera la base B
    B_sin = np.append(B_sin, sin((v_i+1)*x))
    B_cos = np.append(B_cos, cos((v_i+1)*x))
    B = np.append(B,B_sin[v_i])
    B = np.append(B,B_cos[v_i])

print('B =', B)


# PROJECTION
# ----------

proy = intProd(f,1)/intProd(1,1)

for a_i in range(0,int((dim_S-1)/2),1):
    proy = proy + (intProd(f,B[a_i])/intProd(B[a_i],B[a_i]))*B[a_i]

print('proy_S(f) = ', proy)


# GRAPHS
# ------

t = np.arange(-np.pi,np.pi,resolution)
x_axis = []
y_axis = []
y_axis_f = []

for t_i in t:
    x_axis.append(t_i)
    y_axis.append(proy.subs(x,t_i))
    y_axis_f.append(f.subs(x,t_i))

plt.plot(x_axis,y_axis,"-b")
plt.plot(x_axis,y_axis_f,"-r")
plt.grid




























