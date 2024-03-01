import copy
from collections import deque

dice = [[1], [2, 3, 5, 4], [6]]
def run_dice(direction):
    global dice
    next_dice = copy.deepcopy(dice)
    if direction == 0:
        next_dice[0][0] = dice[1][0]

        next_dice[1][0] = dice[2][0]
        next_dice[1][1] = dice[1][1]
        next_dice[1][2] = dice[0][0]
        next_dice[1][3] = dice[1][3]

        next_dice[2][0] = dice[1][2]

    if direction == 1:
        next_dice[0][0] = dice[1][3]

        next_dice[1][0] = dice[1][0]
        next_dice[1][1] = dice[0][0]
        next_dice[1][2] = dice[1][2]
        next_dice[1][3] = dice[2][0]

        next_dice[2][0] = dice[1][1]

    if direction == 2:
        next_dice[0][0] = dice[1][2]

        next_dice[1][0] = dice[0][0]
        next_dice[1][1] = dice[1][1]
        next_dice[1][2] = dice[2][0]
        next_dice[1][3] = dice[1][3]

        next_dice[2][0] = dice[1][0]
    if direction == 3:
        next_dice[0][0] = dice[1][1]

        next_dice[1][0] = dice[1][0]
        next_dice[1][1] = dice[2][0]
        next_dice[1][2] = dice[1][2]
        next_dice[1][3] = dice[0][0]

        next_dice[2][0] = dice[1][3]

    dice = next_dice


n, m = map(int, input().split())
dice_map = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def get_point(cr, cc):
    point = dice_map[cr][cc]
    queue = deque([(cr, cc)])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[cr][cc] = True
    count = 1
    while queue:
        c_r, c_c = queue.popleft()
        for i in range(4):
            n_r, n_c = c_r + dr[i], c_c + dc[i]
            if n_r < 0 or n_c < 0 or n_r >= n or n_c >= n:
                continue
            if dice_map[n_r][n_c] == point and not visited[n_r][n_c]:
                queue.append((n_r, n_c))
                visited[n_r][n_c] = True
                count += 1
    return count * point


d = 1
r, c = 0, 0
total_point = 0
for _ in range(m):
    nr, nc = r + dr[d], c + dc[d]
    if nr < 0 or nc < 0 or nr >= n or nc >= n:
        d = (d + 2 + 4) % 4
        nr, nc = r + dr[d], c + dc[d]
    r, c = nr, nc
    run_dice(d)

    total_point += get_point(r, c)
    if dice[2][0] > dice_map[r][c]:
        d = (d + 1) % 4
    elif dice[2][0] < dice_map[r][c]:
        d = (d - 1 + 4) % 4
    elif dice[2][0] == dice_map[r][c]:
        d = d

print(total_point)