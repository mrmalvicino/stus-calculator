import sympy as sp
import stus_functions as fn
from sympy import Piecewise, pi


B = fn.genBase()

print(f'B = {B}\n')

x = sp.Symbol('x')
f = Piecewise((0, x<-pi/2), (0, x>pi/2) , (x**0, True))
proy = fn.genProy(f, B)

print(f'proy_S(f) = {proy}\n')

sp.plot(proy, f, (x, -3.14, 3.14), show=True)
