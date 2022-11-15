from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

#목표 : 빨간 구슬 10회 이내로 빼내기
#기울이기 왼 오 위 아래
#기울일 때 빨간 구슬 파란 구슬 동시에 움직임
#파란 구슬과 빨간 구슬은 같은 칸에 있을 수 없음
#파란 구슬이 구멍에 빠지면 실패
#    오른쪽 위 왼쪽 아래

dr = [-1, 0, 1, 0]
dc = [0, 1, -1, 0]

def move_until_wall_or_hole(row, col, r, c, game_map):
    move_count = 0
    while game_map[row + r][col + c] != "#" and game_map[row][col] != "O":
        row += r
        col += c
        move_count += 1
    return row, col, move_count

def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])
    visited = [[[[False] * m for _ in range(n)]for _ in range(m)]for _ in range(n)]
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    queue = deque()
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j
            elif game_map[i][j] == "B":
                blue_row, blue_col = i, j

    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()
        if try_count > 10:
            break

        for i in range(4):
            next_red_row, next_red_col, red_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            next_blue_row, next_blue_col, blue_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)

            if game_map[next_blue_row][next_blue_col] == "O":
                continue

            if game_map[next_red_row][next_red_col] == "O":
                return True

            if next_red_row == next_blue_row and next_red_col == next_blue_col:
                if red_count > blue_count:
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dr[i]

            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))

    return False
print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다