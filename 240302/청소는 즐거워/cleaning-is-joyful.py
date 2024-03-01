n = int(input())
# 서, 북, 동, 남
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]
dust_percentage = {0: [(-1, 1, 1), (1, 1, 1), (-2, 0, 2), (2, 0, 2), (0, -2, 5), (-1, 0, 7), (1, 0, 7), (-1, -1, 10), (1, -1, 10), (0, -1)],
                1: [(1, 1, 1), (1, -1, 1), (0, 2, 2), (0, -2, 2), (-2, 0, 5), (0, -1, 7), (0, 1, 7), (-1, 1, 10), (-1, -1, 10), (-1, 0)],
                2: [(-1, -1, 1), (1, -1, 1), (-2, 0, 2), (2, 0, 2), (0, 2, 5), (-1, 0, 7), (1, 0, 7), (-1, 1, 10), (1, 1, 10), (0, 1)],
                3: [(-1, 1, 1), (-1, -1, 1), (0, 2, 2), (0, -2, 2), (2, 0, 5), (0, -1, 7), (0, 1, 7), (1, 1, 10), (1, -1, 10), (1, 0)]}
dust_map = [list(map(int, input().split())) for _ in range(n)]
total_run = 4 * (n // 2) + 1

dust = 0
# 이동이 끝난 좌표와 이전 칸에서 이동한 방향
def clean_map(cr, cc, direction, stage_dust):
    global dust_map
    global dust
    dust_move = dust_percentage[direction]
    current_dust = stage_dust
    final_dust = stage_dust
    for k in range(len(dust_move) - 1):
        nr, nc = cr + dust_move[k][0], cc + dust_move[k][1]
        move_dust = current_dust * dust_move[k][2] // 100
        if nr < 0 or nc < 0 or nr >= n or nc >= n:
            dust += move_dust
            final_dust -= move_dust
        else:
            dust_map[nr][nc] += move_dust
            final_dust -= move_dust
    nr, nc = cr + dust_move[9][0], cc + dust_move[9][1]
    if nr < 0 or nc < 0 or nr >= n or nc >= n:
        dust += final_dust
    else:
        dust_map[nr][nc] += final_dust

d = 1
l = 1
count = -1
r, c = n // 2, n // 2
for t in range(total_run):
    d = (d - 1 + 4) % 4
    count += 1
    if count == 2:
        count = 0
        l += 1
    if t == total_run - 1:
        l = n
    nr, nc = r, c
    for _ in range(l):
        nr, nc = nr + dr[d], nc + dc[d]
        c_dust = dust_map[nr][nc]
        clean_map(nr, nc, d, c_dust)
        dust_map[nr][nc] = 0

    r, c = nr, nc
print(dust)