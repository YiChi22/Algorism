current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
# 1. 현재 위치를 청소한다.
# 2. 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
#   a. 아직 청소하지 않은 공간이 있다면 그 방향으로 회전한 다음 한 칸을 전진하고 1부터 진행
#   b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다
#   c. 네 방향 모두 청소가 이미 되어 있거나 벽인 경우에는 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다
#   b. 네 방향 모두 청소가 이미 되어있거나 벽이면서 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def get_rotate(d):
    return (d + 3) % 4

def get_back(d):
    return (d + 2) % 4

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])
    count = 1
    room_map[r][c] = 2
    queue = list([[r, c, d]])

    while queue:
        r, c, d = queue.pop(0)
        temp_d = d

        for i in range(4):
            temp_d = get_rotate(temp_d)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
                count += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])
                break
            elif i == 3:
                new_r, new_c = r + dr[get_back(d)], c + dc[get_back(d)]
                queue.append([new_r, new_c, d])

                if room_map[new_r][new_c] == 1:
                    return count
# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))