numbers = [2, 3, 1]
target_number = 0
count = 0


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, index, n, target):
    if index == len(array):
        if n == target:
            global count
            count += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, index + 1, n + array[index], target)
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, index + 1, n - array[index], target)


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, 0, 0, target_number)

print(count)
