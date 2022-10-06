import math as mt
from sympy import integrate, cos, sin, pi
from sympy.abc import x


def inProd(v,w):
    
    k = integrate((v*w), (x,-pi/1,pi/1))
    
    return k


def genBase(S='Trigonometric polynomials', dim_S=21):
    
    if S == 'Trigonometric polynomials':
        B = [1]
    
        for v_i in range(1, int(mt.ceil(dim_S/2)), 1):
            B.append(sin((v_i)*x))
            B.append(cos((v_i)*x))
    
        if dim_S%2 == 0:
            B.append(sin(int(dim_S/2)*x))
            
    return B


def genProy(f, B):

    dim_S = len(B)
    proy = 0

    for a_i in range(0,int(dim_S),1):
        proy = proy + (inProd(f,B[a_i])/inProd(B[a_i],B[a_i]))*B[a_i]
    
    return proy


def spToList(n, y, var=x):

    y_list = []

    for n_i in n:
        y_list.append(y.subs(var,n_i))
        
    return y_list
