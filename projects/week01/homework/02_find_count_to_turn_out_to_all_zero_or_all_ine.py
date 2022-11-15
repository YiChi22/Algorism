input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    lists = list(string)
    strs = 0

    if lists[0] == '0':
        strs = string.replace('1', '0')
    else:
        strs = string.replace('0', '1')
    return strs


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
