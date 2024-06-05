# Câu hỏi 1 : Viết function thực hiện đánh giá classification model bằng F1-Score.
# Function nhận vào 3 giá trị tp, fp, fn và trả về F1-score
import math


def calc_f1_score(tp, fp, fn):
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * (p * r) / (p + r)


assert round(calc_f1_score(tp=2, fp=3, fn=5), 2) == 0.33
print(round(calc_f1_score(tp=2, fp=4, fn=5), 2))

# Câu hỏi 2 : Viết function is_number nhận input có thể là string hoặc một số kiểm tra n (một số)
# có hợp lệ hay không (vd: n=’10’, is_number(n) sẽ trả về True ngược lại là False).
# Đầu ra của chương trình sau đây là gì?
import math
import numbers


def is_number(n):
    if isinstance(n, numbers.Number):
        return True
    return False


assert is_number(3) == 1.0
assert is_number("-2a") == 0.0
print(is_number(1))
print(is_number("n"))

# Câu hỏi 4 : Viết function thực hiện Sigmoid Function f(x)=1/(1+e^(-x)).
# Nhận input là x và return kết quả tương ứng trong Sigmoid Function.
# Đầu ra của chương trình sau đây là gì?
import math


def calc_sig(x):
    return 1 / (math.exp(-x) + 1)


assert round(calc_sig(3), 2) == 0.95
print(round(calc_sig(2), 2))

# Câu hỏi 5: Viết function thực hiện Elu Function
# Nhận input là x và return kết quả tương ứng trong Elu Function.
# Đầu ra của chương trình sau đây là gì khi α = 0.01?
import math


def calc_elu(x):
    if x <= 0:
        return 0.01 * (math.exp(x) - 1)
    return x


assert round(calc_elu(1)) == 1
print(round(calc_elu(-1), 2))

# Câu hỏi 6 : Viết function nhận 2 giá trị x,
# và tên của activation function act_name activation function chỉ có
# 3 loại (sigmoid, relu, elu), thực hiện tính toán activation function
# tương ứng với name nhận được trên giá trị của x và trả kết quả.
# Đầu ra của chương trình sau đây là gì?
import math


def calc_activation_func(x, act_name):
    if act_name == "sigmoid":
        return 1 / (1 + math.exp(-x))
    if act_name == "relu":
        if x <= 0:
            return 0
        return x
    if act_name == "elu":
        if x <= 0:
            return 0.01 * (math.exp(x) - 1)
        return x
    raise KeyError


assert calc_activation_func(x=1, act_name="relu") == 1
print(round(calc_activation_func(x=3, act_name="sigmoid"), 2))


# Câu hỏi 7 : Viết function tính absolute error = |y − yˆ|. Nhận input là y và yˆ,
# return về kết quả absolute error tương ứng. Đầu ra của chương trình sau đây là gì?
def calc_ae(y, y_hat):
    if y > y_hat:
        return y - y_hat
    return y_hat - y


y = 1
y_hat = 6
assert calc_ae(y, y_hat) == 5
y = 2
y_hat = 9
print(calc_ae(y, y_hat))


# Câu hỏi 8 : Viết function tính squared error = (y−yˆ)2. Nhận input là y và yˆ,
# return về kết quả squared error tương ứng. Đầu ra của chương trình sau đây là gì?
def calc_se(y, y_hat):
    return (y - y_hat) * (y - y_hat)


y = 4
y_hat = 2
assert calc_se(y, y_hat) == 4
print(calc_se(2, 1))

# Câu hỏi 9 :Viết function xấp xỉ cos khi nhận x là giá trị muốn tính cos(x) và n là số lần lặp muốn xấp xỉ.
# Return về kết quả cos(x) với bậc xấp xỉ tương ứng. Đầu ra của chương trình sau đây là gì?
import math


def approx_cos(x, n):
    total = 0
    for i in range(n):
        total = total + ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    return total


assert round(approx_cos(x=1, n=10), 2) == 0.54
print(round(approx_cos(x=3.14, n=10), 2))

# Câu hỏi 10 : Viết function xấp xỉ sin khi nhận x là giá trị muốn tính sin(x) và n là số lần lặp muốn xấp xỉ.
# Return về kết quả sin(x) với bậc xấp xỉ tương ứng. Đầu ra của chương trình sau đây là gì?
import math


def approx_sin(x, n):
    total = 0
    for i in range(n):
        total = total + ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    return total


assert round(approx_sin(x=1, n=10), 4) == 0.8415
print(round(approx_sin(x=3.14, n=10), 4))

# Câu hỏi 11 :Viết function xấp xỉ sinh khi nhận x là giá trị muốn tính sinh(x) và n là số lần lặp muốn xấp xỉ.
# Return về kết quả sinh(x) với bậc xấp xỉ tương ứng. Đầu ra của chương trình sau đây là gì?
import math


def approx_sinh(x, n):
    total = 0
    for i in range(n):
        total = total + (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    return total


assert round(approx_sinh(x=1, n=10), 2) == 1.18
print(round(approx_sinh(x=3.14, n=10), 2))

# Câu hỏi 12 :Viết function xấp xỉ cosh khi nhận x là giá trị muốn tính cosh(x) và n là số lần lặp muốn xấp xỉ.
# Return về kết quả cosh(x) với bậc xấp xỉ tương ứng. Đầu ra của chương trình sau đây là gì?
import math


def approx_cosh(x, n):
    total = 0
    for i in range(n):
        total = total + (x ** (2 * i)) / math.factorial(2 * i)
    return total


assert round(approx_cosh(x=1, n=10), 2) == 1.54
print(round(approx_cosh(x=3.14, n=10), 2))
