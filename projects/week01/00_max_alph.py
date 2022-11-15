def find_alphabet_occurrence_array(string):
    lists = []
    dict = {}
    max_num = 0
    max_char = []
    print("이 구문의 최빈 값은 : ")
    for str in string:
        if not str.isalpha():
            continue
        else:
            lists.append(str)
    for list in lists:
        if not list in dict:
            dict[list] = 1
        else:
            dict[list] += 1

    for num in dict.values():
        if max_num < num:
            max_num = num

    for key in dict:
        if max_num == dict[key]:
            max_char.append(key)
    print(max_char)

find_alphabet_occurrence_array("hello my name is sparta")
find_alphabet_occurrence_array("aaaa bbb dddd ef llll")
