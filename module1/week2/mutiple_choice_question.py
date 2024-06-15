# Question 1

def max_kernel(num_list, k):
    result = []
    # Your Code Here
    size = len(num_list)
    if k > size:
        return []
    if k < 1:
        return []
    for i in range(size - k + 1):
        max_num = max(num_list[i:i+k])
        result.append(max_num)
    # End Code Here
    return result


assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))

# Question 2


def character_count(word):
    character_statistic = {}
    # Your Code Here
    word = word.strip()
    for char in word:
        if char in character_statistic:
            character_statistic[char] += 1
        else:
            character_statistic[char] = 1
    # End Code Here
    return character_statistic


assert character_count(" Baby ") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))

# Question 3


def count_word(file_path):
    counter = {}
    with open(file_path, 'r') as f:
        data = f.read()
        words = data.split()
        for word in words:
            word = word.lower()
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    return counter


file_path = 'module1/week2/P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])

# Question 4


def levenshtein_distance(token1, token2):
    len_str1 = len(token1)
    len_str2 = len(token2)
    dp = [[0 for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]
    for i in range(len_str1 + 1):
        dp[i][0] = i
    for j in range(len_str2 + 1):
        dp[0][j] = j
    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            if token1[i - 1] == token2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1],
                                   dp[i - 1][j], dp[i][j - 1])
    distance = dp[len_str1][len_str2]
    return distance


assert levenshtein_distance("hi", "hello") == 4.0
print(levenshtein_distance(" hola ", " hello "))

# Question 5


def check_the_number(N):
    list_of_numbers = []
    result = ""
    for i in range(1, 5):
        list_of_numbers.append(i)
    if N in list_of_numbers:
        results = "True"
    if N not in list_of_numbers:
        results = "False"
    return results


N = 7
assert check_the_number(N) == "False"
N = 2
results = check_the_number(N)
print(results)

# Question 6


def my_function(data, max, min):
    result = []
    for i in data:  # Your code here
        # Neu i < min thi them min vao result
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


my_list = [5, 2, 5, 0, 1]
max = 1
min = 0
assert my_function(max=max, min=min, data=my_list) == [1, 1, 1, 0, 1]
my_list = [10, 2, 5, 0, 1]
max = 2
min = 1
print(my_function(max=max, min=min, data=my_list))


# Question 7
def my_function1(x, y):
    # Your code here
    # Su dung extend de noi y vao x #return x
    x.extend(y)
    return x


list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]
assert my_function1(list_num1, my_function1(list_num2, list_num3)) == [
    'a', 2, 5, 1, 1, 0, 0]
list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]
print(my_function1(list_num1, my_function1(list_num2, list_num3)))

# Question 8


def my_function2(n):
    # Your code here
    sorted_list = sorted(n)
    return sorted_list[0]


my_list = [1, 22, 93, -100]
assert my_function2(my_list) == -100
my_list = [1, 2, 3, -1]
print(my_function2(my_list))


# Question 9
def my_function3(n):
    # Your code here
    sorted_list = sorted(n)
    return sorted_list[-1]


my_list = [1001, 9, 100, 0]
assert my_function3(my_list) == 1001
my_list = [1, 9, 9, 0]
print(my_function3(my_list))


# Question 10
def my_function4(my_list, num=1):
    return any(
        [True for i in my_list if i == num]
    )


my_list = [1, 3, 9, 4]
assert my_function4(my_list, -1) == False
my_list = [1, 2, 3, 4]
print(my_function4(my_list, 2))


# Question 11
def my_function5(list_nums=[0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var/len(list_nums)


assert my_function5([4, 6, 8]) == 6
print(my_function5())

# Question 12


def my_function6(data):
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)
    return var


assert my_function6([3, 9, 4, 5]) == [3, 9]
print(my_function6([1, 2, 3, 5, 6]))

# Question 13


def my_function7(y):
    var = 1
    while (y > 1):  # Your code here
        var = var * y
        y = y - 1
    return var


assert my_function7(8) == 40320
print(my_function7(4))

# Question 14


def my_function8(x):
    # your code here
    return x[::-1]


x = 'I can do it'
assert my_function8(x) == "ti od nac I"
x = 'apricot'
print(my_function8(x))

# Question 15


def function_helper(x):
    # Your code here
    # Neu x>0 tra ve ’T’, nguoc lai tra ve ’N’
    if x > 0:
        return 'T'
    else:
        return 'N'


def my_function9(data):
    res = [function_helper(x) for x in data]
    return res


data = [10, 0, -10, -1]
assert my_function9(data) == ['T', 'N', 'N', 'N']
data = [2, 3, 5, -1]
print(my_function9(data))

# Question 16


def function_helper2(x, data):
    for i in data:
        # Your code here
        # Neu x == i thi return 0
        if x == i:
            return 0
    return 1


def my_function10(data):
    res = []
    for i in data:
        if function_helper2(i, res):
            res.append(i)
    return res


lst = [10, 10, 9, 7, 7]
assert my_function10(lst) == [10, 9, 7]
lst = [9, 9, 8, 1, 1]
print(my_function10(lst))
