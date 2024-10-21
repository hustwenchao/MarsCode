def print_data(data):
    # 如果data[i] < 0, 打印L, 如果data[i] > 0, 打印R, 否则打印.
    print(''.join(['L' if i < 0 else 'R' if i > 0 else '.' for i in data]))

# 用数字形式打印状态
def print_num(data):
    # 每个数字占两个字符的宽度，中间用|分隔
    print('|'.join([f'{i:2}' for i in data]))


def solution(num, data):
    # 初始化状态数组，0表示竖立，-1表示向左倒，1表示向右倒
    state = [0] * num

    # 根据输入字符串更新初始状态
    for i in range(num):
        if data[i] == 'L':
            state[i] = -1
        elif data[i] == 'R':
            state[i] = 1

    # 先统计出当前的L和R的骨牌数量
    card_dict = {}
    for i in range(num):
        if state[i] != 0:
            card_dict[i] = state[i]

    while len(card_dict) > 0:

        # 更新状态
        for card_index, card_state in card_dict.items():
            state[card_index] = card_state

        print(card_dict)
        print_num(state)

        new_card_dict = {}
        for card_index, card_state in card_dict.items():
            if card_state < 0 <= card_index - 1:
               # 向左倒
                if card_index - 1 in card_dict and card_state + card_dict[card_index - 1] >= 0:
                    # 如果左边的骨牌向右倒，且向右倒的趋势大于左倒的趋势
                    pass
                else:
                    if card_index - 1 not in new_card_dict:
                        new_card_dict[card_index - 1] = card_state - 1
                    else:
                        if card_state + new_card_dict[card_index - 1] <= 0:
                            new_card_dict[card_index - 1] = card_state - 1
                        new_card_dict[card_index - 1] = new_card_dict[card_index - 1] + card_state - 1
            if card_state > 0 and card_index + 1 < num:
                # 向右倒
                if card_index + 1 in card_dict and card_state + card_dict[card_index + 1] <= 0:
                    # 如果右边的骨牌向左倒，且向左倒的趋势大于右倒的趋势
                    pass
                else:
                    if card_index + 1 not in new_card_dict:
                        new_card_dict[card_index + 1] = card_state + 1
                    else:
                        new_card_dict[card_index + 1] = new_card_dict[card_index + 1] + card_state + 1

        remove_keys = []
        # 删除掉new_card_dict中值为0的元素
        for card_index in new_card_dict.keys():
            if new_card_dict[card_index] == 0:
                remove_keys.append(card_index)
        for key in remove_keys:
            new_card_dict.pop(key)

        card_dict = new_card_dict

        if len(new_card_dict) == 0:
            break


    # 统计保持竖立的骨牌
    standing_count = state.count(0)
    standing_positions = [i + 1 for i in range(num) if state[i] == 0]

    if standing_count == 0:
        return "0"
    else:
        return f"{standing_count}:{','.join(map(str, standing_positions))}"


if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(5, "R....") == "0")
    print(solution(1, ".") == "1:1")
    print(solution(14, ".L.R...LR..L..") == "4:3,6,13,14")
