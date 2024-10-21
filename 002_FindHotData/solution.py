def solution(nums, k):
    num_dict = {}
    for num in nums:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1

    sorted_dict = dict(sorted(num_dict.items(), key=lambda x: x[1], reverse=True))

    # 返回前k个元素
    return ",".join([str(key) for key in list(sorted_dict.keys())[:k]])


if __name__ == "__main__":
    print(solution( [1,1,1,2,2,3], 2) == "1,2" )
    print(solution( [1], 1) == "1" )