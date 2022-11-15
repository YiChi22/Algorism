import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    get_stock = {}
    days = 0
    get = 0
    for d in range(len(dates)):
        get_stock[dates[d]] = supplies[d]

    print(get_stock)

    for i in range(0, k):
        stock -= 1
        days += 1
        if stock > i:
            continue

        if days in dates:
            stock += get_stock[days]
            print(get_stock[days])
            get += 1

    return get


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))