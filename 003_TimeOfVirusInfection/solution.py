# 四种状态
# 0：没有戴口罩
# 1: 戴了口罩
# 2: 戴了口罩的第一次感染
# 3: 感染者

def print_seats(seats):
    # 没有口罩：0
    # 戴了口罩：M
    # 戴了口罩的第一次感染：1
    # 感染者：P
    # 按行输出

    num_dict = {0: "0", 1: "M", 2: "1", 3: "P"}
    for row in seats:
        print("".join([str(x) for x in row]))


def check_all_infected(row_n, column_m, seats):
    for row in range(row_n):
        for column in range(column_m):
            if seats[row][column] < 3:
                return False
    return True


def solution(row_n, column_m, seats, patient):
    seconds = 0

    if patient[0] >= row_n or patient[1] >= column_m or patient[0] < 0 or patient[1] < 0:
        return 0

    seats[patient[0]][patient[1]] = 3
    while not check_all_infected(row_n, column_m, seats):
        # print("After {} seconds:".format(seconds))
        # print_seats(seats)

        # 拷贝一个新的座位表
        new_seats = [[ 3 if seats[row][column] >= 2 else seats[row][column] for column in range(column_m)] for row in range(row_n)]

        for i in range(row_n):
            for j in range(column_m):
                if seats[i][j] == 2:
                    new_seats[i][j] = 3
                if seats[i][j] == 3:
                    # 左边
                    if i - 1 >= 0:
                        if seats[i - 1][j] == 0:
                            new_seats[i - 1][j] = 3
                        elif seats[i - 1][j] == 1:
                            if new_seats[i - 1][j] == 2:
                                new_seats[i - 1][j] = 3
                            else:
                                new_seats[i - 1][j] = 2
                        elif seats[i - 1][j] == 2:
                            new_seats[i - 1][j] = 3
                    if i + 1 < row_n:
                        if seats[i + 1][j] == 0:
                            new_seats[i + 1][j] = 3
                        elif seats[i + 1][j] == 1:
                            if new_seats[i + 1][j] == 2:
                                new_seats[i + 1][j] = 3
                            else:
                                new_seats[i + 1][j] = 2
                        elif seats[i + 1][j] == 2:
                            new_seats[i + 1][j] = 3
                    if j - 1 >= 0:
                        if seats[i][j - 1] == 0:
                            new_seats[i][j - 1] = 3
                        elif seats[i][j - 1] == 1:
                            if new_seats[i][j - 1] == 2:
                                new_seats[i][j - 1] = 3
                            else:
                                new_seats[i][j - 1] = 2
                        elif seats[i][j - 1] == 2:
                            new_seats[i][j - 1] = 3
                    if j + 1 < column_m:
                        if seats[i][j + 1] == 0:
                            new_seats[i][j + 1] = 3
                        elif seats[i][j + 1] == 1:
                            if new_seats[i][j + 1] == 2:
                                new_seats[i][j + 1] = 3
                            else:
                                new_seats[i][j + 1] = 2
                        elif seats[i][j + 1] == 2:
                            new_seats[i][j + 1] = 3

        seats = new_seats

        seconds += 1
    return seconds


if __name__ == "__main__":
    #  You can add more test cases here
    testSeats1 = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 1, 1], [0, 0, 0, 1]]
    testSeats2 = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 1, 1], [0, 0, 0, 1]]
    testSeats3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    testSeats4 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    testSeats5 = [[1]]

    print(solution(4, 4, testSeats1, [2, 2]) == 6)
    print(solution(4, 4, testSeats2, [2, 5]) == 0)
    print(solution(4, 4, testSeats3, [2, 2]) == 4)
    print(solution(4, 4, testSeats4, [2, 2]) == 6)
    print(solution(1, 1, testSeats5, [0, 0]) == 0)
