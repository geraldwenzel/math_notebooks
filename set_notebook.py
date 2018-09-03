# set all imports for notebook



from decimal import Context, Decimal, ROUND_HALF_UP, getcontext

import re

from IPython import get_ipython
import matplotlib.pyplot as plt
import numpy as np
#https://github.com/sympy/sympy/issues/13319
from sympy import (Eq, FiniteSet, Function, N, Rational, S, Union, init_printing, lcm, nsimplify, pprint,
                   solveset, sqrt, symbols, pi, sympify)
from sympy.solvers import solve

get_ipython().run_line_magic('matplotlib', 'inline')
a, b, c = symbols('a b c')
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

init_printing(use_latex='mathjax')

#https://github.com/jupyter/help/issues/109

# round decimals up if last digit is 5
getcontext().rounding=ROUND_HALF_UP

