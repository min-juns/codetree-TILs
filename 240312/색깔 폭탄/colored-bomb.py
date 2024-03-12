import copy
from collections import deque
N, M = map(int, input().split())
bomb_map = [list(map(int, input().split())) for _ in range(N)]

def bomb_comb(b_r, b_c):
    visited = []
    queue = deque([(b_r, b_c)])
    visited.append((b_r, b_c))
    current_color = bomb_map[b_r][b_c]
    while queue:
        c_r, c_c = queue.popleft()
        for i in range(4):
            n_r, n_c = c_r + dr[i], c_c + dc[i]
            if n_r < 0 or n_c < 0 or n_r >= N or n_c >= N:
                continue
            if (n_r, n_c) not in visited and (bomb_map[n_r][n_c] == current_color or bomb_map[n_r][n_c] == 0):
                visited.append((n_r, n_c))
                queue.append((n_r, n_c))

    return visited


def find_stand_point(b_list):
    max_r, min_c = -1, N + 1
    standard_bomb = (-1, -1)
    num_red = 0
    for b in b_list:
        bb_r, bb_c = b
        if bomb_map[bb_r][bb_c] > 0:
            if bb_r > max_r:
                max_r, min_c = bb_r, bb_c
                standard_bomb = (bb_r, bb_c)
            elif bb_r == max_r:
                if bb_c < min_c:
                    min_c = bb_c
                    standard_bomb = (bb_r, bb_c)
        elif bomb_map[bb_r][bb_c] == 0:
            num_red += 1
    return standard_bomb, num_red


dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
def find_max_bomb():
    max_bomb = 0
    best_bomb_case = []
    for r in range(N):
        for c in range(N):
            # 빨간색으로 시작하는 것은 제외하고. (빨간색만으로 이루어진 것을 방지)
            if bomb_map[r][c] > 0:
                bomb_list = bomb_comb(r, c)
                temp_max = len(bomb_list)
                if temp_max > max_bomb:
                    max_bomb = temp_max
                    best_bomb_case = bomb_list
                elif temp_max == max_bomb:
                    # 현재 최고점의 빨간색의 갯수와 기준점 찾는다
                    current_max_stand_bomb, current_max_red = find_stand_point(best_bomb_case)
                    temp_max_stand_bomb, temp_max_red = find_stand_point(bomb_list)
                    if current_max_red > temp_max_red:
                        max_bomb = temp_max
                        best_bomb_case = bomb_list
                    elif current_max_red == temp_max_red:
                        if current_max_stand_bomb[0] < temp_max_stand_bomb[0]:
                            max_bomb = temp_max
                            best_bomb_case = bomb_list
                        elif current_max_stand_bomb[0] == temp_max_stand_bomb[0]:
                            if current_max_stand_bomb[1] > temp_max_stand_bomb[1]:
                                max_bomb = temp_max
                                best_bomb_case = bomb_list

    return best_bomb_case


def gravity():
    global bomb_map
    temp_bomb_map = [[-100 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if bomb_map[r][c] == -1:
                temp_bomb_map[r][c] = -1

    for c in range(N):
        temp_list = []
        for r in range(N):
            if bomb_map[r][c] != -1 and bomb_map[r][c] != -100:
                temp_list.append(bomb_map[r][c])
            if bomb_map[r][c] == -1:
                for k in range(len(temp_list)):
                    idx = r - (len(temp_list) - k)
                    temp_bomb_map[idx][c] = temp_list[k]
                temp_list = []
            elif r == N - 1:
                for k in range(len(temp_list)):
                    idx = r - (len(temp_list) - k) + 1
                    temp_bomb_map[idx][c] = temp_list[k]
                temp_list = []
    bomb_map = temp_bomb_map


def turn_90():
    global bomb_map
    turn_map = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            turn_map[N - c - 1][r] = bomb_map[r][c]

    bomb_map = turn_map


points = 0
while True:
    remove_list = find_max_bomb()

    if len(remove_list) < 2:
        break

    # -100인 곳은 비어있는 곳
    for rl in remove_list:
        bomb_map[rl[0]][rl[1]] = -100

    gravity()

    turn_90()

    gravity()

    points += len(remove_list) ** 2

print(points)