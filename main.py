import sympy as sp
from sympy import Piecewise, pi
import functions

B = functions.genBasis(dim_S=7)

print(f'B = {B}\n')

x = sp.Symbol('x')
f = Piecewise((0, x<-pi/2), (0, x>pi/2) , (x**0, True))
proy = functions.genProy(f, B)

print(f'proy_S(f) = {proy}\n')

sp.plot(proy, f, (x, -pi, pi), show=True)