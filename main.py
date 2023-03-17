import numpy as np
import sympy as sp
from sympy import Piecewise, pi
import functions


# GENERATE BASIS:

dim_S = 7 # Dimention of the vector space S. The bigger the dimention is, the better the approximation is, but the slower the process is.
B = functions.gen_basis(dim_S)

print(f'B = {B}\n')


# GENERATE PROJECTION:

x_start = -pi
x_final = pi
x = sp.Symbol('x')
f = Piecewise((0, x<x_start/2), (0, x>x_final/2) , (x**0, True))
p = functions.gen_projection(f, B)

print(f'p_S(f) = {p}\n')


# PLOT THE FUNCTION AND THE PROJECTION:

# sp.plot(p, f, (x, x_start, x_final), show=True) # Faster plotting, but only supported in Spyder

x_start_np = float(x_start.evalf())
x_final_np = float(x_final.evalf())
pitch = float(0.01) # The smaller the pitch is, the sharper the plot is but the slower the process is.
x_np = np.arange(x_start_np, x_final_np + pitch, pitch)

f_np = np.zeros(len(x_np))
for i in range(0, len(x_np), 1):
    f_np[i] = f.subs(x, x_np[i])

p_np = np.zeros(len(x_np))
for i in range(0, len(x_np), 1):
    p_np[i] = p.subs(x, x_np[i])

kwargs = {
        'figsize': (10,5),
        'title': f'dim_{dim_S}',
        'xlabel': 'tiempo',
        'ylabel': ('projection','function'),
        'xscale': 'linear',
        'yscale': ('linear','linear'),
        'legend': ('projection','function'),
        'xticks': [-3.14, -1.57, 0, 1.57, 3.14],
        'yticks': ([0, 0.5, 1],[0, 0.5, 1]),
        'xticklabels': ['-pi', '-pi/2', 0, 'pi/2', 'pi'],
        'yticklabels': ('default','default'),
        'xlim': 'default',
        'ylim': ((-0.5, 1.5),(-0.5,1.5)),
        'save': False
    }

functions.plot_LR(x_np, (p_np, f_np), **kwargs)