import math as mt
from sympy import integrate, cos, sin, pi
from sympy.abc import x
import os
from matplotlib import pyplot as plt


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


def plot_LR(x, y, **kwargs):
    
    """
    Generates a plot using matplotlib.

    Parameters
    ----------

    x : NUMPY ARRAY
        Data for the horizontal axis.
    
    y : TUPLE OF NUMPY ARRAYS
        Data for the vertical axes. A two dimentions tuple is expected, containing the data for the left and right vertical axes in each component respectively.

    **kwargs : UNPACKED DICTIONARY
        Object orientated kwargs values for matplotlib.pyplot.plot() and matplotlib.pyplot.setp() methods.
        Bidimentional tuples are expected for the keys that involves the vertical axes.
        For example, the scale could be determined by defining the dictionary kwargs = {'xscale': 'linear', 'yscale': ('logit','log')} and using it into plot_LR(x, y, **kwargs).

    Returns
    -------

    none
    """

    # Store the **kwargs in a new dictionary:
    user_inputs = kwargs

    # Define possible **kwargs:
    kwargs = {
        'figsize': (10,5),
        'title': 'plot',
        'xlabel': '',
        'ylabel': ('',''),
        'xscale': 'linear',
        'yscale': ('linear','linear'),
        'legend': ('',''),
        'xticks': 'default',
        'yticks': ('default','default'),
        'xticklabels': 'default',
        'yticklabels': ('default','default'),
        'xlim': 'default',
        'ylim': ('default','default'),
        'save': False
    }

    # Overwrite the possible **kwargs with the actual inputs:
    for key, value in user_inputs.items():
        if key in kwargs:
            kwargs[key] = value
    
    # Split the plt.setp kwargs into 2 dictionaries:
    setpL = dict()
    setpR = dict()

    setpL_keys = ['yticks', 'yticklabels', 'ylim', 'xticks', 'xticklabels', 'xlim']
    setpR_keys = ['yticks', 'yticklabels', 'ylim']

    for key in setpL_keys:
        if len(kwargs[key]) == 2:
            if kwargs[key][0] != 'default':
                setpL.update({key: kwargs[key][0]})
        else:
            if kwargs[key] != 'default':
                setpL.update({key: kwargs[key]})

    for key in setpR_keys:
        if len(kwargs[key]) == 2:
            if kwargs[key][1] != 'default':
                setpR.update({key: kwargs[key][1]})

    # Generate plot:
    fig, (axisL) = plt.subplots(1,1, figsize=kwargs['figsize'])
    axisR = axisL.twinx()
    
    axisL.plot(x, y[0], color='blue')
    axisR.plot(x, y[1], color='red', linestyle='--')
    
    axisL.set_xlabel(kwargs['xlabel'])
    axisL.set_ylabel(kwargs['ylabel'][0])
    axisR.set_ylabel(kwargs['ylabel'][1])
    
    axisL.set_xscale(kwargs['xscale'])
    axisL.set_yscale(kwargs['yscale'][0])
    axisR.set_yscale(kwargs['yscale'][1])
    
    axisL.set_title(kwargs['title'])
    axisL.legend([kwargs['legend'][0]], loc='lower left')
    axisR.legend([kwargs['legend'][1]], loc='lower right')

    plt.setp(axisL, **setpL)
    plt.setp(axisR, **setpR)
    
    axisL.grid()
    plt.tight_layout()
    graph = plt.gcf()

    # Save plot:
    if kwargs['save'] == True:
        title=kwargs['title']
        graph.savefig(os.path.join(os.path.dirname(__file__), 'images', f'{title}'+'.png'))
    else:
        plt.show()

    return