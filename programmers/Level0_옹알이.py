from itertools import combinations, permutations
word = ["aya", "ye", "woo", "ma"]


def solution(babbling):
    answer = 0
    words = []
    for i in range(2, len(word) + 1):
        for j in list(combinations(word, i)):
            words += {''.join(s) for s in permutations(j)}
    for i in babbling:
        if i in word + words:
            answer += 1

    return answer
