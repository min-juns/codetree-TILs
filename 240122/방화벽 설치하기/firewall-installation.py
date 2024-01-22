from collections import deque
import copy

n, m = map(int, input().split())
fire_map = [list(map(int, input().split())) for _ in range(n)]
empty_space = []
fire_list = []

for N in range(n):
    for M in range(m):
        if fire_map[N][M] == 0:
            empty_space.append([N, M])
        if fire_map[N][M] == 2:
            fire_list.append([N, M])


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def fill_fire_count():
    temp_map = copy.deepcopy(fire_map)
    fire_queue = deque(fire_list)
    while fire_queue:
        fire = fire_queue.popleft()
        fire_r = fire[0]
        fire_c = fire[1]
        for i in range(4):
            nr = fire_r + dr[i]
            nc = fire_c + dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue
            if temp_map[nr][nc] == 0:
                temp_map[nr][nc] = 2
                fire_queue.append([nr, nc])

    count = 0
    for r in range(n):
        for c in range(m):
            if temp_map[r][c] == 0:
                count += 1
    return count


max_val = 0


def wall(wall_count, empty_list):
    global max_val
    if wall_count == 3:
        max_val = max(max_val, fill_fire_count())

    else:
        for x in range(len(empty_list)):
            r = empty_list[x][0]
            c = empty_list[x][1]
            fire_map[r][c] = 1
            wall(wall_count + 1, empty_list[x+1:])
            fire_map[r][c] = 0


wall(0, empty_space)
print(max_val)

"""
3 4
0 0 0 0
0 2 0 0
0 0 0 2
"""