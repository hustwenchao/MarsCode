def solution(num, data):
    left = 0
    left_m = 0  # 左边的标记
    right = num - 1
    right_m = 0  # 右边的标记
    count = 0  # 直立的牌

    records_l_to_r = [0] * num
    records_r_to_l = [0] * num

    records_l_to_r[0] = 1 if data[0] == 'R' else 0
    # 先从左向右遍历，只统计向右倒的牌
    for i in range(1, num):
        if data[i] == 'R':
            records_l_to_r[i] += 1
        elif data[i] == 'L':
            if records_l_to_r[i - 1] > 0:
                records_l_to_r[i] = records_l_to_r[i - 1] - 1
        else:
            if records_l_to_r[i - 1] > 0:
                records_l_to_r[i] = records_l_to_r[i - 1] + 1

    print(records_l_to_r)

    for i in range(num - 2, 0, -1):
        if data[i] == 'L':
            records_r_to_l[i] -= 1
        elif data[i] == 'R':
            if records_r_to_l[i + 1] < 0:
                records_r_to_l[i] = records_r_to_l[i + 1] + 1
        else:
            if records_r_to_l[i + 1] < 0:
                records_r_to_l[i] = records_r_to_l[i + 1] - 1

    print(records_r_to_l)

    return -2


if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(14, ".L.R...LR..L..") == "4:3,6,13,14")
    print(solution(5, "R....") == "0")
    print(solution(1, ".") == "1:1")