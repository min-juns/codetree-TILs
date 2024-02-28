import copy
from collections import deque

n, q = map(int, input().split())
N = 2 ** n
game_map = [list(map(int, input().split())) for _ in range(N)]
game_level = list(map(int, input().split()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def melt_ices():
    global game_map
    temp_gmap = copy.deepcopy(game_map)

    for r in range(N):
        for c in range(N):
            if game_map[r][c] == 0:
                continue
            count = 4
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nc < 0 or nr >= N or nc >= N:
                    count -= 1
                    continue
                if game_map[nr][nc] == 0:
                    count -= 1
            if count < 3:
                temp_gmap[r][c] -= 1
    game_map = temp_gmap

def get_start_point(level):
    sp = []
    step = 2 ** level
    for r in range(N // step):
        for c in range(N // step):
            choose_r = r * step
            choose_c = c * step
            sp.append((choose_r, choose_c))
    return sp


def rotate_ices(s_p, l):
    global game_map
    temp_game_map = copy.deepcopy(game_map)

    one_l = l // 2
    for sp in s_p:
        sr, sc = sp
        sr1, sc1 = sr, sc
        sr2, sc2 = sr, sc + one_l
        sr3, sc3 = sr + one_l, sc + one_l
        sr4, sc4 = sr + one_l, sc

        for r in range(one_l):
            for c in range(one_l):
                temp_game_map[sr2 + r][sc2 + c] = game_map[sr1 + r][sc1 + c]
                temp_game_map[sr3 + r][sc3 + c] = game_map[sr2 + r][sc2 + c]
                temp_game_map[sr4 + r][sc4 + c] = game_map[sr3 + r][sc3 + c]
                temp_game_map[sr1 + r][sc1 + c] = game_map[sr4 + r][sc4 + c]

    game_map = temp_game_map

for level in game_level:
    if level != 0:
        s_list = get_start_point(level)
        rotate_ices(s_list, 2 ** level)
    melt_ices()

total_ices = 0
for r in range(N):
    for c in range(N):
        total_ices += game_map[r][c]

visited = [[False for _ in range(N)] for _ in range(N)]
max_val = 0

def find_largest(fr, fc):
    count = 1
    queue = deque([(fr, fc)])
    while queue:
        cr, cc = queue.popleft()
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if (not visited[nr][nc]) and game_map[nr][nc] > 0:
                count += 1
                visited[nr][nc] = True
                queue.append((nr, nc))
    if count == 3:
        print(fr, fc)
    return count

for r in range(N):
    for c in range(N):
        if not visited[r][c] and game_map[r][c] > 0:
            visited[r][c] = True
            max_val = max(max_val, find_largest(r, c))

if max_val == 1:
    max_val = 0
print(total_ices)
print(max_val)