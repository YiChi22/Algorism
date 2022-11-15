s = "(())()"


def is_correct_parenthesis(string):
    lists = list(string)
    count = 0


    for lis in lists:
        if lists[0] == ')':
            return False
        if lis == '(':
            count += 1
        elif lis == ')':
            count -= 1
        else:
            print("올바른 기호가 아닙니다.")
            return
    if count == 0:
        return True
    else:
        return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!