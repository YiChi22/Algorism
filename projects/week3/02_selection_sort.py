input = [4, 6, 2, 9, 1]


def selection_sort(array):
    leng = len(array)

    for i in range(leng - 1):
        num = array[i]
        index = i
        for j in range(i, leng):
            if num > array[j]:
                num = array[j]
                index = j
        array[i], array[index] = array[index], array[i]

    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!