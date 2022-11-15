input = "abadabac"

def find_not_repeating_character(string):
    dict = {}
    list = []
    for char in string:
        if not char.isalpha():
            continue
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    for num in dict:
        if dict[num] == 1:
            list.append(num)

    print(list)

    return list[0]


result = find_not_repeating_character(input)
print(result)