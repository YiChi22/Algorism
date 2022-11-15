import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_city_chicken_distance(n, m, city_map):
    min_value = sys.maxsize
    home = []
    chicken = []

    for i in range(len(city_map)):
        for j in range(len(city_map)):
            if city_map[i][j] == 1:
                home.append([i, j])
            elif city_map[i][j] == 2:
                chicken.append([i, j])
    chicken_list = list(itertools.combinations(chicken, m))

    for ch in chicken_list:
        distance = 0
        for r, c in home:
            min_home_chicken_distance = sys.maxsize
            for chicken_location in ch:
                min_home_chicken_distance = min(min_home_chicken_distance, abs(r - chicken_location[0])+abs(c - chicken_location[1]))

            distance += min_home_chicken_distance
        min_value = min(min_value, distance)
    return min_value

# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!

print("깃 확인용")