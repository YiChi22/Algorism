input = 20


def find_prime_list_under_number(number):
    results = []
    for num in range(2, number):
        results.append(num)

    for num in range(2, number):
        for lists in range(2, number):
            n = num * lists
            if n in results:
                results.remove(n)
            else:
                continue

    return results


result = find_prime_list_under_number(input)
print(result)