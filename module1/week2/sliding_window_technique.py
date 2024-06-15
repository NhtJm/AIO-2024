# Cho một list các số nguyên num_list và một sliding window có kích thước size k di
# chuyển từ trái sang phải. Mỗi lần dịch chuyển 1 vị trí sang phải có thể nhìn thấy
# đươc k số trong num_list và tìm số lớn nhất trong k số này sau mỗi lần trượt
# k phải lớn hơn hoặc bằng 1


def sliding_window(num_list, k):
    size = len(num_list)
    if k > size:
        return []
    if k < 1:
        return []

    result = []

    for i in range(size - k + 1):
        max_num = max(num_list[i:i+k])
        result.append(max_num)

    return result


num_list = [6, 4, 5, 9, -44, 5, 10, 12, 33, 1]
k = 3
print(sliding_window(num_list, k))
