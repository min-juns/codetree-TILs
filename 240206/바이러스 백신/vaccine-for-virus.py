from collections import deque
import copy
# N줄의 map, M개의 병원 고르기
N, M = map(int, input().split())
h_map = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs_hos(hospital_list):
    hh_map = copy.deepcopy(h_map)
    queue = deque(hospital_list)
    visited = []
    for hl in queue:
        visited.append(hl)
    while queue:
        c_r, c_c = queue.popleft()
        for d in range(4):
            nr = c_r + dr[d]
            nc = c_c + dc[d]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if hh_map[nr][nc] == 0 or hh_map[nr][nc] == 2:
                if (nr, nc) not in visited:
                    visited.append((nr, nc))
                    queue.append((nr, nc))
                    hh_map[nr][nc] = hh_map[c_r][c_c] + 1
    max_val = -1000000
    invalid = False
    for r in range(N):
        for c in range(N):
            if hh_map[r][c] == 0:
                max_val = -1
                invalid = True
                break
            else:
                if (r, c) not in hos_list:
                    max_val = max(max_val, hh_map[r][c])
        if invalid:
            break
    if invalid:
        return max_val
    else:
        return max_val - 2


min_time = 100000000
hos_list = []
no_virus = True
for i in range(N):
    for j in range(N):
        if h_map[i][j] == 2:
            hos_list.append((i, j))
        if h_map[i][j] == 0:
            no_virus = False

h_list = []
def pick_hos(last_index, count):
    global min_time
    if count == M:
        temp_min = bfs_hos(h_list)
        if temp_min != -1:
            min_time = min(min_time, temp_min)
    if count < M:
        for k in range(last_index, len(hos_list)):
            h_list.append(hos_list[k])
            pick_hos(k+1, count+1)
            h_list.pop()



pick_hos(0, 0)
if no_virus:
    min_time = 0
if min_time == 100000000:
    print(-1)
else:
    print(min_time)