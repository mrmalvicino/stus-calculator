import math as mt
from sympy import integrate, cos, sin, pi
from sympy.abc import x


def gen_basis(dim_S):
    
    """
    Generates an orthogonal basis (B) for the trigonometric polynomials vector space (S) which is a subset of the integrable functions vector space.

    Parameters
    ----------
    
    dim_S : POSITIVE INTEGER
        Dimension of the trigonometric polynomials vector space.

    Raises
    ------
    
    ValueError
        dim_S must be a positive integer.

    Returns
    -------
    
    B : LIST OF SYMPY OBJECTS
        List containing the elements of the basis.
    """
    
    if type(dim_S) != int or dim_S <= 0:
        raise ValueError(f'dim_S = {dim_S} must be a positive integer.')
    
    B = [1]

    for v_i in range(1, int(mt.ceil(dim_S/2)), 1):
        B.append(sin((v_i)*x))
        B.append(cos((v_i)*x))

    if dim_S%2 == 0:
        B.append(sin(int(dim_S/2)*x))
    
    return B


def inner_product(v, w):
    
    """
    Calculates the inner product for two given vectors. Only integrable functions betwen -pi and pi are currently supported as valid vectors.

    Parameters
    ----------

    v : SYMPY OBJECT
        First vector to define the inner product with.

    w : SYMPY OBJECT
        Second vector to define the inner product with.

    Returns
    -------
    
    k : FLOAT
        Result of the inner product.
    """

    k = integrate((v*w), (x,-pi,pi))
    
    return k


def gen_projection(v, B):
    
    """
    Generates the orthogonal projection of v for a given basis (B). Only integrable functions betwen -pi and pi are currently supported as a valid vector v.

    Parameters
    ----------
    
    v : SYMPY OBJECT
        Vector which the orthogonal projection is going to be calculated for. The Piecewise() method is recomended to define periodic functions.
        
    B : LIST OF SYMPY OBJECTS
        List containing the elements of an orthogonal basis.

    Returns
    -------
    
    projection : SYMPY OBJECT
        Result of the projection.
    """
    
    dim_S = len(B)
    projection = 0

    for i in range(0,int(dim_S),1):
        projection = projection + (inner_product(v,B[i])/inner_product(B[i],B[i]))*B[i]
    
    return projection