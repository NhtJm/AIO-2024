# Trigonometry functions
import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def approx_sin(x, n):
    total = 0
    for i in range(n):
        total = total + ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    print(total)
    return


def approx_cos(x, n):
    total = 0
    for i in range(n):
        total = total + ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    print(total)
    return


def approx_sinh(x, n):
    total = 0
    for i in range(n):
        total = total + (x ** (2 * i + 1)) / factorial(2 * i + 1)
    print(total)
    return


def approx_cosh(x, n):
    total = 0
    for i in range(n):
        total = total + (x ** (2 * i)) / factorial(2 * i)
    print(total)
    return

approx_sin(x=3.14, n=10) #>> 0.0015926529267151343
approx_cos(x=3.14, n=10) #>> -0.9999987316527259
approx_sinh(x=3.14, n=10) #>> 11.53029203039954
approx_cosh(x=3.14, n=10) #>> 11.573574828234543
