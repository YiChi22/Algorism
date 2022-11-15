input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    lists = []
    add = 0
    dis = 0
    for num in range(len(array)):
        if num + 1 < len(array):
            add = array[num] + array[num + 1]
            dis = array[num] * array[num + 1]
        else:
            continue

        print(add, dis)

        if add < dis:
            lists.append('*')
        elif add == dis:
            lists.append('* = +')
        else:
            lists.append('+')

    return lists


result = find_max_plus_or_multiply(input)
print(result)