# return single 2 

from functools import reduce
from operator import mul


def factorial(n):
    return reduce(mul, range(1, n + 1), 1)


print(factorial(5))
