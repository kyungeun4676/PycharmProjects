input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for element in array:  # array 의 길이만큼 연산문 실
        if number == element:  # 비교 연산 1번 실
            return True     # N * 1 = N만큼의 시간이 걸림

    return False


result = is_number_exist(3, input)
print(result)