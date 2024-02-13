n, m, k = map(int, input().split())

g_map = [[0 for _ in range(m)] for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


for _ in range(k):
    # s: 1초동안 움직이는 거리, d: 이동 방향, b: 곰팡이의 크기
    x, y, s, d, b = map(int, input().split())
    g_map[x-1][y-1] = [[s, d-1, b]]


def g_move():
    global g_map
    next_g_map = [[0 for _ in range(m)] for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if g_map[r][c] != 0:
                s, d, b = g_map[r][c][0]
                nr, nc = r, c
                for _ in range(s):
                    nr = nr + dr[d]
                    nc = nc + dc[d]
                    if nr < 0 or nc < 0 or nr >= n or nc >= m:
                        if d % 2 == 0:
                            d += 1
                        else:
                            d -= 1
                        nr = nr + (dr[d] * 2)
                        nc = nc + (dc[d] * 2)
                if next_g_map[nr][nc] == 0:
                    next_g_map[nr][nc] = [[s, d, b]]
                else:
                    next_g_map[nr][nc].append([s, d, b])

    g_map = next_g_map

res = 0
check_line = 0
count = 0
while True:
    count += 1
    # step 1: 탐색
    search_done = False
    total_break = False
    for r in range(n):
        if g_map[r][check_line] != 0:
            res += g_map[r][check_line][0][2]
            g_map[r][check_line] = 0
            break
    """
    while True:
        for r in range(n):
            if g_map[r][check_line] != 0:
                res += g_map[r][check_line][0][2]
                g_map[r][check_line] = 0
                search_done = True
                break
        if search_done:
            break
        else:
            check_line += 1
            if check_line >= m:
                total_break = True
                break
    if total_break:
        break
    """
    # step 2: 곰팡이 이동
    g_move()
    # step 3: 곰팡이 융합
    for r in range(n):
        for c in range(m):
            if g_map[r][c] != 0:
                if len(g_map[r][c]) >= 2:
                    # s: 1초동안 움직이는 거리, d: 이동 방향, b: 곰팡이의 크기
                    max_s, max_d, max_b = 0, 0, 0
                    for i in range(len(g_map[r][c])):
                        c_s, c_d, c_b = g_map[r][c][i]
                        if max_b < c_b:
                            max_s, max_d, max_b = c_s, c_d, c_b
                    g_map[r][c] = [[max_s, max_d, max_b]]

    check_line += 1
    if check_line >= m:
        break

print(res)