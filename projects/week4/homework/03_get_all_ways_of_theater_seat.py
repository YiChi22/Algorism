seat_count = 9
vip_seat_array = [4, 7]
memo = {
    1: 1,
    2: 2,
}

def dynamic_pro(n, memo):
    if n in memo:
        return memo[n]

    nth = dynamic_pro(n - 1, memo) + dynamic_pro(n - 2, memo)
    memo[n] = nth
    return nth


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0

    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        count_of_ways = dynamic_pro(fixed_seat_index - current_index, memo)
        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1

    count_of_ways = dynamic_pro(total_count - current_index, memo)
    all_ways *= count_of_ways
    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))