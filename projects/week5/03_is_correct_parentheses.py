from collections import deque

balanced_parentheses_string = "()))((()"

def is_corrct_parenthese(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0

def separate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""

    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break

    v = ''.join(list(queue))
    return u, v


def reverse_parentheses(string):
    reversed_string = ''
    for char in string:
        if char == '(':
            reversed_string += ')'
        else:
            reversed_string += '('
    return reversed_string


def charge_to_correct_parenthese(string):
    if string == '':
        return ''
    u, v = separate_to_u_v(string)
    if is_corrct_parenthese(u):
        return u + charge_to_correct_parenthese(v)
    else:
        return '(' + charge_to_correct_parenthese(v) + ')' + reverse_parentheses(u[1:-1])


def get_correct_parentheses(balanced_parentheses_string):
    if is_corrct_parenthese(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return charge_to_correct_parenthese(balanced_parentheses_string)



print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!