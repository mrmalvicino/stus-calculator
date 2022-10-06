import sympy as sp
from sympy import Piecewise, pi
import stus_functions as fn

B = fn.genBase(dim_S=9)

print(f'B = {B}\n')

x = sp.Symbol('x')
f = Piecewise((0, x<-pi/2), (0, x>pi/2) , (x**0, True))
proy = fn.genProy(f, B)

print(f'proy_S(f) = {proy}\n')

sp.plot(proy, f, (x, -pi, pi), show=True)
