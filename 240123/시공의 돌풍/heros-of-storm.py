import copy
N, M, T = map(int, input().split())
wind_map = [list(map(int, input().split())) for _ in range(N)]
# -1은 돌풍을 의미함

wind = []

for n in range(N):
    if wind_map[n][0] == -1:
        wind.append(n)

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

r1 = [0, -1, 0, 1]
c1 = [1, 0, -1, 0]

r2 = [0, 1, 0, -1]
c2 = [1, 0, -1, 0]

def spread_dust(r, c, w_map):
    global wind_map
    reduce_val = (wind_map[r][c] // 5)
    count = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nc < 0 or nr >= N or nc >= M:
            continue
        if wind_map[nr][nc] != -1:
            count += 1
            w_map[nr][nc] += reduce_val
    wind_map[r][c] -= (reduce_val * count)
    return w_map


for t in range(T):
    w_map = [[0 for _ in range(M)] for _ in range(N)]
    # 먼지 확산
    for n in range(N):
        for m in range(M):
            if wind_map[n][m] != -1:
                w_map = spread_dust(n, m, w_map)

    for n in range(N):
        for m in range(M):
            if wind_map[n][m] != -1:
                wind_map[n][m] = wind_map[n][m] + w_map[n][m]
    # 청소 시작
    # 1. 반시계
    copy_wind_map = copy.deepcopy(wind_map)
    cr = wind[0]
    cc = 0
    step1 = 0
    while True:
        nr = cr + r1[step1]
        nc = cc + c1[step1]
        if nr < 0 or nc < 0 or nr >= N or nc >= M:
            step1 += 1
            continue
        if nr == wind[0] and nc == 0:
            break
        if cr == wind[0] and cc == 0:
            wind_map[nr][nc] = 0
        else:
            wind_map[nr][nc] = copy_wind_map[cr][cc]
        cc = nc
        cr = nr

    # 1. 시계
    cr = wind[1]
    cc = 0
    step2 = 0
    while True:
        nr = cr + r2[step2]
        nc = cc + c2[step2]
        if nr < 0 or nc < 0 or nr >= N or nc >= M:
            step2 += 1
            continue
        if nr == wind[1] and nc == 0:
            break
        if cr == wind[1] and cc == 0:
            wind_map[nr][nc] = 0
        else:
            wind_map[nr][nc] = copy_wind_map[cr][cc]
        cc = nc
        cr = nr


total_dust = 0
for n in range(N):
    for m in range(M):
        if wind_map[n][m] != -1:
            total_dust += wind_map[n][m]

print(total_dust)