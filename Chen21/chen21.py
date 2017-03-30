# %%
from sympy import *
from sympy import Sum, factorial, oo
from sympy.abc import i, k, m, n, x
init_printing(use_unicode=True)

C = Function('C')
n = symbols('n', integer=True)
catalan_expr = 1 / (n + 1) * binomial(2 * n, n)
catalan_rec = Eq(C(n), catalan_expr)
Cn = Lambda([n], catalan_expr)
catalan_rec
[(i, Cn(i).doit()) for i in range(0, 11)]

# %%
centralBinomialCoef = Sum(binomial(2 * n, n) * x**n, (n, 0, oo))
centralBinomialCoef
# %%
x = symbols('x', integer=True)
centralBinomialCoef_expr = 1 / (sqrt(1 - 4 * x))
centralBinomialCoef = centralBinomialCoef_expr
centralBinomialCoef
