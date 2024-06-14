# Simulate 3 activation functions(sigmoid, ELU, ReLU)
import math


def is_number(n):
    try:
        float(n)  # Type-casting the string to ‘float‘.
        # If string is not a valid ‘float‘,
        # it’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True


# activation functions(sigmoid, ELU, ReLU)
def sigmoid(x):
    print(f"""sigmoid: f({x})= {1 / (1 + math.exp(-x))}""")
    return


def elu(x, alpha=0.01):
    if x > 0:
        print(f"""elu: f({x})= {x}""")
    else:
        print(f"""elu: f({x})= {alpha * (math.exp(x) - 1)}""")
    return


def relu(x):
    print(f"""relu: f({x})= {max(0, x)}""")
    return


def activation_func(func, x):
    if not is_number(x):
        print("x must be a number")
        return None
    x = float(x)
    if func == "sigmoid":
        return sigmoid(x)
    elif func == "elu":
        return elu(x)
    elif func == "relu":
        return relu(x)
    else:
        print("Invalid activation function")
        return None


def Hello():
    print("Hello")
    return


# Test the function
x = input('Input x: ')
func = input('Input activation function (sigmoid, relu, elu): ')
activation_func(func, x)
