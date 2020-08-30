# set all imports for notebook


from decimal import Context, Decimal, ROUND_HALF_UP, getcontext

import re

from IPython import get_ipython
import matplotlib.pyplot as plt
import numpy as np
#https://github.com/sympy/sympy/issues/13319
from sympy import (Eq, FiniteSet, Function, Float, Interval, N, Rational, S, Union)
from sympy import (cos, sin, tan, cot, sec, csc)
from sympy import (div, init_printing, lcm, nsimplify, nsolve, oo, pprint, real_root, real_roots,
                   simplify, solveset, sqrt, symbols, pi, powdenest, sympify)
from sympy.solvers import solve

get_ipython().run_line_magic('matplotlib', 'inline')
a, b, c, d = symbols('a b c d')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
q, r, s, t = symbols('q r s t')
u, v = symbols('u v')
x, y, z = symbols('x y z')

init_printing(use_latex='mathjax')

#https://github.com/jupyter/help/issues/109

# round decimals up if last digit is 5
getcontext().rounding=ROUND_HALF_UP

# raise exception on numpy error
np.seterr('raise')
