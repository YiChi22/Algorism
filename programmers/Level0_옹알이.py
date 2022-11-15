word = ["aya", "ye", "woo", "ma"]


def solution(babbling):
    answer = 0
    if 1 <= len(babbling) <= 100:
        for i in range(len(babbling)):
            if len(babbling[i]) > 16:
                continue
            for j in range(len(word)):
                if babbling[i].find(word[j]) > 0:
                    answer += 1
                    break

    return answer