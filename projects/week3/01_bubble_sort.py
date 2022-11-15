input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    leng = len(array)
    for i in range(leng - 1):
        for j in range(leng - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return


bubble_sort(input)
print(inp.ut)  # [1, 2, 4, 6, 9] 가 되어야 합니다!