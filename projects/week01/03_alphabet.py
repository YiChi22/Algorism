input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurence_array = [0] * 26
    index = 0;
    max_num = 0

    for str in string:
        if not str.isalpha():
            continue
        else:
            index = (ord(str) - ord('a'))
            alphabet_occurence_array[index] += 1

    for num in range(len(alphabet_occurence_array)):
        if max_num < alphabet_occurence_array[num]:
            max_num = alphabet_occurence_array[num]

    print('기징 믾이 나온 단어는 : ')
    for i, num in enumerate(alphabet_occurence_array):
        if max_num == num:
            print(chr(ord('a') + i))
    print('입니다')

find_max_occurred_alphabet(input)
find_max_occurred_alphabet("aaaa ccc bbbb dke llll")