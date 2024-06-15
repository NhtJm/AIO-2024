# Viết function đọc các câu trong một file txt, đếm số lượng các từ xuất hiện và trả về một dictionary
# với key là từ và value là số lần từ đó xuất hiện.
# Input: Đường dẫn đến file txt
# Output: dictionary đếm số lần các từ xuất hiện
# Note: Giả sử các từ trong file txt đều có các chữ cái thuộc [a-z] hoặc [A-Z]
# Không cần các thao tác xử lý string phức tạp nhưng cần xử lý các từ đều là viết thường

file_path = 'module1/week2/P1_data.txt'


def word_count(file_path):  # return dictionary of word count
    with open(file_path, 'r') as f:
        data = f.read()
        words = data.split()
        word_dict = {}
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        return word_dict


print(word_count(file_path))
