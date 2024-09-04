from math import exp
from numpy.random import lognormal

N = [10, 10000, 10000000]
x = [lognormal(-10.0, 10.0) for _ in range(max(N))]
# print(x)
print("Range of input values: [{}, {}]".format(min(x), max(x)))
# print(sum(N))


def alg_sum_accurate(x):  # x == x[:n]
    s = 0.
    u = sorted(x)
    print(type(s))
    for i in u:  # x_0, x_1, \ldots, x_{n-1}
        s += i
    return s


print(alg_sum_accurate(x))
