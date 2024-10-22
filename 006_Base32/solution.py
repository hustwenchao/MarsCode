def base32_encode(raw_str):
    # Base32 字符表
    base32_chars = "9876543210mnbvcxzasdfghjklpoiuyt"
    # 将字符串转换为二进制表示
    binary_str = ''.join(f'{ord(c):08b}' for c in raw_str)
    # 补 0 使其长度为 5 的倍数
    while len(binary_str) % 5 != 0:
        binary_str += '0'
    # 每 5 位一组进行分组
    groups = [binary_str[i:i+5] for i in range(0, len(binary_str), 5)]
    # 将每组转换为十进制索引
    indices = [int(group, 2) for group in groups]
    # 根据索引在字符表中查找对应的字符
    encoded_str = ''.join(base32_chars[index] for index in indices)
    # 根据原始二进制数据的长度确定末尾需要补 `+` 的数量
    remainder = len(raw_str) * 8 % 40
    if remainder == 0:
        pass
    elif remainder == 8:
        encoded_str += '++++++'
    elif remainder == 16:
        encoded_str += '++++'
    elif remainder == 24:
        encoded_str += '+++'
    elif remainder == 32:
        encoded_str += '+'
    return encoded_str

def base32_decode(encoded_str):
    # Base32 字符表
    base32_chars = "9876543210mnbvcxzasdfghjklpoiuyt"
    # 去除末尾的 `+`
    plus_count = encoded_str.count('+')
    encoded_str = encoded_str.rstrip('+')
    # 将字符串转换为对应的索引
    indices = [base32_chars.index(char) for char in encoded_str]
    # 将索引转换为 5 位二进制表示
    binary_str = ''.join(f'{index:05b}' for index in indices)
    # # 去除末尾的 0
    binary_str = binary_str[:len(binary_str) // 8 * 8]
    # 每 8 位一组进行分组
    groups = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    # 将每组转换为 ASCII 字符
    raw_str = ''.join(chr(int(group, 2)) for group in groups)
    return raw_str

def solution(rawStr, encodedStr):
    encoded_result = base32_encode(rawStr)
    decoded_result = base32_decode(encodedStr)
    return f"{encoded_result}:{decoded_result}"

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("foo", "b0zj5+++") == "bljhy+++:bar" )
    print(solution("The encoding process represents 40-bit groups of input bits as output strings of 8 encoded characters.  Proceeding from left to right, a 40-bit input group is formed by concatenating 5 8bit input groups. These 40 bits are then treated as 8 concatenated 5-bit groups, each of which is translated into a single character in the base 32 alphabet.  When a bit stream is encoded via the base 32 encoding, the bit stream must be presumed to be ordered with the most-significant- bit first. That is, the first bit in the stream will be the high- order bit in the first 8bit byte, the eighth bit will be the low- order bit in the first 8bit byte, and so on.", "bljhykd8c1++++++") == "maf3m164vlahyl60vlds9i6svuahmiod58l3mi6sbglhmodfcbz61b8vb0fj1162c0jjmi6d58jhb160vlk2mu89b0fj1il9b4ls9oogcak2mu89cvp25pncbuls9oo359i79lncbvjh1ln558ahzknsb4aj1lnscbj7917zc0jh3ln4bafhill9bll3yo09vashbu89cajs9id0buf21n89b5z61b8vb0fj1160vlk2mu89bul3yunz58fj3163vul3pln558a2s166vuj33knfbgj37u60vlds9v0928a3su89v4j29unf58dj5oogc8lsi17fv8sj3l093zk79kd0cals9knsbfz21p64vkz21id4b4p3ml89b4ls9c89bvjhiko8cashiknfbgs79v0vb0fj1162c0jjmi6d4zz3mkn6v9z3yla9cuf3sko158fj316fc0zhiiobb4p3ml89v4j21ol9b5z23pncbuh3m166v8zj5kn6casj5160vkz21p6458a37io459ld5168vak3zkn7bgp7i189muf3moa9b5z35pnf58lj1id4b4hs9pnd58shikoxbash116hv4zs9u61bfz35kndbfz63ba9bgj33oo5v4j3cn89caf3m167v4p79iofc0sh7o09vgpj3u89b0ss9i6sbgljmon4bzz21ol9b0ss9oosbasj5ln558ohsu6158p3zl09vgjj3u8vcvfhcod0blfh3kncczhs9kd0czz3bpnscvp7i17fv8zj1160cbh79u61bfz3bpnscvp79kd0czz3soa9caf3m16dcal3mknv58ohso6b58a3m16fv8ss9p60buf7p16xc0s3mia9b0fj1160vkz21p6458d3siddczz6zkd0czz35ynfbfh79u61bfz3mpn2v8p3z167v4p79uo0vah79kd458p3zl09vajjcn09vul31lns58a3su89v4j79u61bfz3bpnscvp79c67v4p79kdlcassk168vls79iox58jhinz+:foobar" )