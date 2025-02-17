"""Set all imports and variables for notebook."""

# pylint: disable=unused-import

import re
from decimal import ROUND_HALF_UP, Context, Decimal, getcontext

import matplotlib.pyplot as plt
import mpmath
import numpy as np
from ipywidgets import interact, widgets
from matplotlib.patches import Rectangle
from sympy import (
    Eq,
    FiniteSet,
    Float,
    Function,
    Interval,
    N,
    Rational,
    S,
    Union,
    cos,
    cot,
    csc,
    div,
    expand,
    factor,
    factorint,
    floor,
    lcm,
    limit,
    nsimplify,
    nsolve,
    oo,
    pi,
    powdenest,
    radsimp,
    real_root,
    real_roots,
    root,
    sec,
    simplify,
    sin,
    solveset,
    sqrt,
    symbols,
    tan,
)
from sympy.solvers import solve

a, b, c, d = symbols("a b c d")
k, m, n = symbols("k m n", integer=True)
f, g, h = symbols("f g h", cls=Function)
q, r, s, t = symbols("q r s t")
u, v = symbols("u v")
x, y, z = symbols("x y z")

# round decimals up if last digit is 5
getcontext().rounding = ROUND_HALF_UP
