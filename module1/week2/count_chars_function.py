# Viết function trả về một dictionary đếm số lượng chữ xuất hiện trong một từ, với key là chữ cái và value là số lần xuất hiện
# Input: một từ
# Output: dictionary đếm số lần các chữ xuất hiện
# Note: Giả sử các từ nhập vào đều có các chữ cái thuộc [a-z] hoặc [A-Z]


def count_chars(string):
    char_dict = {}
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


# Examples
string1 = 'Happiness'
print(count_chars(string1))
string2 = 'smiles'
print(count_chars(string2))
